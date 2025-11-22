# Import Flask framework and related functions for web app
from flask import Flask,render_template,request,redirect,url_for

# Import JSON library to read/write workout data
import json


# Exercise database organized by muscle group
# This dictionary contains all available exercises for each muscle
EXERCISES = {
    "Quadriceps": [
        "Back Squat",
        "Front Squat",
        "Leg Press",
        "Lunges",
        "Leg Extensions",
        "Bulgarian Split Squat"
    ],
    "Glutes": [
        "Hip Thrust",
        "Romanian Deadlift",
        "Glute Bridge",
        "Bulgarian Split Squat",
        "Cable Kickbacks"
    ],
    "Back": [
        "Pull-ups",
        "Barbell Row",
        "Lat Pulldown",
        "Deadlift",
        "Cable Row",
        "T-Bar Row"
    ],
    "Chest": [
        "Bench Press",
        "Incline Press",
        "Dips",
        "Push-ups",
        "Cable Flies",
        "Dumbbell Press"
    ],
    "Shoulders": [
        "Overhead Press",
        "Lateral Raises",
        "Front Raises",
        "Arnold Press",
        "Face Pulls",
        "Upright Row"
    ],
    "Traps": [
        "Barbell Shrugs",
        "Dumbbell Shrugs",
        "Face Pulls",
        "Farmer's Walk"
    ],
    "Hamstrings": [
        "Romanian Deadlift",
        "Leg Curl",
        "Good Mornings",
        "Nordic Curls"
    ],
    "Biceps": [
        "Barbell Curl",
        "Hammer Curl",
        "Preacher Curl",
        "Concentration Curl",
        "Cable Curl"
    ],
    "Triceps": [
        "Close-grip Bench Press",
        "Skull Crushers",
        "Rope Pushdown",
        "Dips",
        "Overhead Extension"
    ],
    "Forearms": [
        "Wrist Curl",
        "Reverse Wrist Curl",
        "Farmer's Walk",
        "Dead Hang"
    ],
    "Calves": [
        "Standing Calf Raise",
        "Seated Calf Raise",
        "Jump Rope"
    ],
    "Abs": [
        "Crunches",
        "Planks",
        "Russian Twists",
        "Leg Raises",
        "Cable Crunches",
        "Ab Wheel"
    ]
}

app = Flask(__name__)
DATA_FILE = 'workouts.json'

# Load workouts from JSON file
# Structure: {"workouts": [{"id": int, "user_id": int, "date": str, ...}]}
def get_workouts():
    try:
        f = open(DATA_FILE,'r')
        data = json.load(f)
        f.close()
        return data
    except:
        return []
# Save workout data to JSON
def save_workouts(wlist):
    f = open(DATA_FILE,'w')
    json.dump(wlist,f,indent=4)
    f.close()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/create",methods=["GET","POST"])
def create():
    if request.method == "POST":
        # Get form inputs
        name = request.form['name']
        date = request.form.get('date')
        muscles = request.form.getlist("muscle_groups")
        notes = request.form.get("notes")
        # Build exercise list for each muscle
        exs = {}
        for m in muscles:
            selected = request.form.getlist(f"exercises_{m}")
            if len(selected) > 0:
                exs[m] = []
                for ex in selected:
                    s = request.form.get(f"sets_{m}_{ex}")
                    r = request.form.get(f"reps_{m}_{ex}")
                    exs[m].append({"name": ex,"sets": s,"reps": r})
        # Create new workout with ID
        wlist = get_workouts()
        wid = 1
        if len(wlist) > 0:
            wid = wlist[-1]["id"] + 1
        new_w = {"id": wid,"name": name,"date": date,"muscle_groups": muscles,"exercises": exs,"notes": notes}
        wlist.append(new_w)
        save_workouts(wlist)
        print(f"Created: {name} on {date}")
        return redirect(url_for("workouts"))
    else:
        return render_template("create.html",all_exercises=EXERCISES)
@app.route("/workouts")
def workouts():
    wlist = get_workouts()
    return render_template("workouts.html",workouts=wlist)
@app.route("/workout/<int:wid>")
def workout_detail(wid):
    wlist = get_workouts()
    found = None
    for w in wlist:
        if w["id"] == wid:
            found = w
            break
    if found != None:
        return render_template("workout_detail.html",workout=found)
    else:
        return "Workout not found",404
@app.route("/delete/<int:wid>")
def delete_workout(wid):
    # Remove workout from list
    wlist = get_workouts()
    new = []
    for w in wlist:
        if w["id"] != wid:
            new.append(w)
    save_workouts(new)
    print(f"Deleted workout: {wid}")
    return redirect(url_for("workouts"))
@app.route("/stats")
def stats():
    # Calculate workout statistics
    wlist = get_workouts()
    total = len(wlist)
    mcounts = {}
    for w in wlist:
        for m in w["muscle_groups"]:
            if m in mcounts:
                mcounts[m] = mcounts[m] + 1
            else:
                mcounts[m] = 1
    top = "N/A"
    bottom = "N/A"
    maxval = 1
    if len(mcounts) > 0:
        top = max(mcounts,key=mcounts.get)
        bottom = min(mcounts,key=mcounts.get)
        maxval = mcounts[top]
    return render_template("stats.html",total_workouts=total,most_trained=top,least_trained=bottom,muscle_stats=mcounts,max_count=maxval)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)