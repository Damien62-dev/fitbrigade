from flask import Flask, render_template, request, redirect, url_for

from models import db, User, Workout, MuscleGroup, Exercise, WorkoutExercise, WorkoutMuscleGroup, Goal

from datetime import datetime, date

app = Flask(__name__)

app.config.from_object("config")  # Load configuration from config.py
db.init_app(app)


def seed_db_if_needed():
    """
    Populate the database with initial data
    ONLY if it's empty.
    """
    if User.query.count() > 0:
        return  # already seeded

    # Create demo user
    demo_user = User(username="Demo User", email="demo@fitbrigade.com")
    db.session.add(demo_user)
    db.session.commit()  # get user.id

    # Muscle Groups
    quadriceps = MuscleGroup(name="Quadriceps")
    glutes = MuscleGroup(name="Glutes")
    back = MuscleGroup(name="Back")
    chest = MuscleGroup(name="Chest")
    shoulders = MuscleGroup(name="Shoulders")
    traps = MuscleGroup(name="Traps")
    hamstrings = MuscleGroup(name="Hamstrings")
    biceps = MuscleGroup(name="Biceps")
    triceps = MuscleGroup(name="Triceps")
    forearms = MuscleGroup(name="Forearms")
    calves = MuscleGroup(name="Calves")
    abs = MuscleGroup(name="Abs")
    
    db.session.add_all([quadriceps, glutes, back, chest, shoulders, traps, 
                        hamstrings, biceps, triceps, forearms, calves, abs])
    db.session.commit()

    # Exercises for Quadriceps
    back_squat = Exercise(name="Back Squat", muscle_group_id=quadriceps.id)
    front_squat = Exercise(name="Front Squat", muscle_group_id=quadriceps.id)
    leg_press = Exercise(name="Leg Press", muscle_group_id=quadriceps.id)
    lunges = Exercise(name="Lunges", muscle_group_id=quadriceps.id)
    leg_extension = Exercise(name="Leg Extension", muscle_group_id=quadriceps.id)
    
    #Exercises for Glutes
    hip_thrust = Exercise(name="Hip Thrust", muscle_group_id=glutes.id)
    romanian_deadlift = Exercise(name="Romanian Deadlift", muscle_group_id=glutes.id)
    glute_bridge = Exercise(name="Glute Bridge", muscle_group_id=glutes.id)
    bulgarian_split_squat = Exercise(name="Bulgarian Split Squat", muscle_group_id=glutes.id)
    cable_kickbacks = Exercise(name="Cable Kickbacks", muscle_group_id=glutes.id)

    #Exercises for Back
    pull_ups = Exercise(name="Pull-ups", muscle_group_id=back.id)
    barbell_row = Exercise(name="Barbell Row", muscle_group_id=back.id)
    deadlift = Exercise(name="Deadlift", muscle_group_id=back.id)
    Lat_pull_down = Exercise(name="Lat Pull-down", muscle_group_id=back.id)
    seated_cable_row = Exercise(name="Seated Cable Row", muscle_group_id=back.id)
    T_bar_Row = Exercise(name="T-bar Row", muscle_group_id=back.id)
    
    # Exercises for Chest
    bench_press = Exercise(name="Bench Press", muscle_group_id=chest.id)
    incline_press = Exercise(name="Incline Press", muscle_group_id=chest.id)
    push_ups = Exercise(name="Push-ups", muscle_group_id=chest.id)
    dips = Exercise(name="Dips", muscle_group_id=chest.id)
    chest_fly = Exercise(name="Chest Fly", muscle_group_id=chest.id)
    cable_crossovers = Exercise(name="Cable Crossovers", muscle_group_id=chest.id)
    
    # Exercises for Back
    pull_ups = Exercise(name="Pull-ups", muscle_group_id=back.id)
    barbell_row = Exercise(name="Barbell Row", muscle_group_id=back.id)
    deadlift = Exercise(name="Deadlift", muscle_group_id=back.id)
    Lat_pull_down = Exercise(name="Lat Pull-down", muscle_group_id=back.id)
    seated_cable_row = Exercise(name="Seated Cable Row", muscle_group_id=back.id)
    
    # Exercises for Shoulder
    military_press = Exercise(name="Military Press", muscle_group_id=shoulders.id)
    lateral_raises = Exercise(name="Lateral Raises", muscle_group_id=shoulders.id)
    front_raises = Exercise(name="Front Raises", muscle_group_id=shoulders.id)
    arnold_press = Exercise(name="Arnold Press", muscle_group_id=shoulders.id)


    # Exercises for Traps

    barbell_shrugs = Exercise(name="Barbell Shrugs", muscle_group_id=traps.id)
    dumbbell_shrugs = Exercise(name="Dumbbell Shrugs", muscle_group_id=traps.id)
    face_pulls = Exercise(name="Face Pulls", muscle_group_id=traps.id)
    Farmer_walk = Exercise(name="Farmer's Walk", muscle_group_id=traps.id)

    # Exercises for Hamstrings
    romanian_deadlift_hamstrings = Exercise(name="Romanian Deadlift", muscle_group_id=hamstrings.id)
    leg_curl = Exercise(name="Leg Curl", muscle_group_id=hamstrings.id)
    glute_ham_raise = Exercise(name="Glute Ham Raise", muscle_group_id=hamstrings.id)
    good_mornings = Exercise(name="Good Mornings", muscle_group_id=hamstrings.id)
    nordic_curls = Exercise(name="Nordic Curls", muscle_group_id=hamstrings.id)

    # Exercises for Biceps
    barbell_curl = Exercise(name="Barbell Curl", muscle_group_id=biceps.id)
    hammer_curl = Exercise(name="Hammer Curl", muscle_group_id=biceps.id)
    concentration_curl = Exercise(name="Concentration Curl", muscle_group_id=biceps.id)
    preacher_curl = Exercise(name="Preacher Curl", muscle_group_id=biceps.id)
    cable_curl = Exercise(name="Cable Curl", muscle_group_id=biceps.id)

    # Exercises for Triceps
    dips_triceps = Exercise(name="Dips", muscle_group_id=triceps.id)
    close_grip_bench_press = Exercise(name="Close-grip Bench Press", muscle_group_id=triceps.id)
    rope_pushdown = Exercise(name="Rope Pushdown", muscle_group_id=triceps.id)
    overhead_extension = Exercise(name="Overhead Extension", muscle_group_id=triceps.id)
    skull_crushers = Exercise(name="Skull Crushers", muscle_group_id=triceps.id) 

    # Exercises for Forearms
    wrist_curl = Exercise(name="Wrist Curl", muscle_group_id=forearms.id)
    reverse_wrist_curl = Exercise(name="Reverse Wrist Curl", muscle_group_id=forearms.id)
    farmer_walk = Exercise(name="Farmer's Walk", muscle_group_id=forearms.id)
    dead_hang = Exercise(name="Dead Hang", muscle_group_id=forearms.id)

    # Exercises for Calves
    standing_calf_raise = Exercise(name="Standing Calf Raise", muscle_group_id=calves.id)
    seated_calf_raise = Exercise(name="Seated Calf Raise", muscle_group_id=calves.id)
    calf_press_on_leg_machine = Exercise(name="Calf Press on Leg Machine", muscle_group_id=calves.id)
    
    # Exercises for Abs
    crunches = Exercise(name="Crunches", muscle_group_id=abs.id)
    leg_raises = Exercise(name="Leg Raises", muscle_group_id=abs.id)
    planks = Exercise(name="Planks", muscle_group_id=abs.id)
    russian_twists = Exercise(name="Russian Twists", muscle_group_id=abs.id)
    bicycle_crunches = Exercise(name="Bicycle Crunches", muscle_group_id=abs.id)

    db.session.add_all([back_squat, front_squat, leg_press, lunges, leg_extension,
    hip_thrust, romanian_deadlift, glute_bridge, bulgarian_split_squat, cable_kickbacks,
    pull_ups, barbell_row, deadlift, Lat_pull_down, seated_cable_row, T_bar_Row,
    bench_press, incline_press, push_ups, dips, chest_fly, cable_crossovers,
    military_press, lateral_raises, front_raises, arnold_press,
    barbell_shrugs, dumbbell_shrugs, face_pulls, Farmer_walk,
    romanian_deadlift_hamstrings,leg_curl, glute_ham_raise, good_mornings, nordic_curls,
    barbell_curl, hammer_curl, concentration_curl, preacher_curl, cable_curl,
    dips_triceps, close_grip_bench_press, rope_pushdown, overhead_extension, skull_crushers,
    wrist_curl, reverse_wrist_curl, farmer_walk, dead_hang,
    standing_calf_raise, seated_calf_raise, calf_press_on_leg_machine,
    crunches, leg_raises, planks, russian_twists, bicycle_crunches])
    db.session.commit()


with app.app_context():
    db.create_all()
    seed_db_if_needed()

# Helper functions

def get_demo_user():
    """Get the demo user (always user_id = 1)"""
    return User.query.get(1)


def get_user_workouts(user_id):
    """Get all workouts for a specific user"""
    workouts = Workout.query.filter_by(user_id=user_id).all()
    return workouts


def get_workout_exercises(workout_id):
    """Get all exercises for a specific workout"""
    workout_exercises = WorkoutExercise.query.filter_by(workout_id=workout_id).all()
    return workout_exercises


def get_workout_muscle_groups(workout_id):
    """Get all muscle groups for a specific workout"""
    links = WorkoutMuscleGroup.query.filter_by(workout_id=workout_id).all()
    result = []
    for link in links:
        result.append(link.muscle_group)
    return result
# --------------------
# Routes
# --------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/workouts')
def workouts():
    user = get_demo_user()
    user_workouts = get_user_workouts(user.id)
    return render_template('workouts.html', workouts=user_workouts)


@app.route('/workout/<int:workout_id>')
def workout_detail(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    muscle_groups = get_workout_muscle_groups(workout_id)
    workout_exercises = get_workout_exercises(workout_id)
    
    # Group exercises by muscle group
    exercises_by_muscle = {}
    for we in workout_exercises:
        muscle_name = we.exercise.muscle_group.name
        if muscle_name not in exercises_by_muscle:
            exercises_by_muscle[muscle_name] = []
        exercises_by_muscle[muscle_name].append(we)
    
    return render_template('workout_detail.html', 
                         workout=workout, 
                         exercises_by_muscle=exercises_by_muscle)


@app.route('/create_workout', methods=['GET'])
def create_workout_form():
    muscle_groups = MuscleGroup.query.all()
    
    # Get exercises grouped by muscle group
    exercises_by_muscle = {}
    for mg in muscle_groups:
        exercises_by_muscle[mg.name] = Exercise.query.filter_by(muscle_group_id=mg.id).all()
    
    return render_template('create_workout.html', 
                         muscle_groups=muscle_groups,
                         all_exercises=exercises_by_muscle)

@app.route('/create_goal')
def create_goal_form():
    muscle_groups = MuscleGroup.query.all()
    
    # Get exercises grouped by muscle group
    exercises_by_muscle = {}
    for mg in muscle_groups:
        exercises_by_muscle[mg.name] = Exercise.query.filter_by(muscle_group_id=mg.id).all()
    
    return render_template('create_goal.html', 
                         muscle_groups=muscle_groups,
                         all_exercises=exercises_by_muscle)


@app.route('/create_goal', methods=['POST'])
def create_goal():
    user = get_demo_user()
    
    # Get form data
    name = request.form['name'].strip()
    deadline_str = request.form.get('deadline', '').strip()  # CHANGÉ: utilise get() au lieu de ['deadline']
    exercise_id = request.form['exercise']
    target_weight = request.form.get('target_weight', '').strip()
    target_reps = request.form.get('target_reps', '').strip()
    notes = request.form.get('notes', '').strip()
    
    # Minimal validation
    if name == "" or exercise_id == "":  # CHANGÉ: enlevé la vérification de deadline_str
        return "Please fill in all required fields.", 400
    
    # Convert date string to date object (only if provided)
    deadline = None  # AJOUTÉ: initialise à None
    if deadline_str != "":  # AJOUTÉ: vérifie si une date a été fournie
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
    
    # Create goal
    goal = Goal(
        user_id=user.id,
        name=name,
        exercise_id=int(exercise_id),
        target_weight=float(target_weight) if target_weight else None,
        target_reps=int(target_reps) if target_reps else None,
        deadline=deadline,  # deadline peut être None maintenant
        notes=notes if notes else None
    )
    
    db.session.add(goal)
    db.session.commit()
    
    return redirect(url_for('goals_list'))

@app.route('/goals')
def goals_list():
    user = get_demo_user()
    user_goals = Goal.query.filter_by(user_id=user.id).all()
    return render_template('goals.html', goals=user_goals)


@app.route('/goal/<int:goal_id>')
def goal_detail(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    return render_template('goal_detail.html', goal=goal)


@app.route('/delete_goal/<int:goal_id>')
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()
    return redirect(url_for('goals_list'))


@app.route('/create_workout', methods=['POST'])
def create_workout():
    user = get_demo_user()
    
    # Get form data
    name = request.form['name'].strip()
    date_str = request.form['date']
    notes = request.form.get('notes', '').strip()
    
    # Minimal validation
    if name == "" or date_str == "":
        return "Please fill in workout name and date.", 400
    
    # Convert date string to date object
    workout_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Create workout
    workout = Workout(
        user_id=user.id,
        name=name,
        date=workout_date,
        notes=notes if notes else None
    )
    
    db.session.add(workout)
    db.session.commit()  # get workout.id
    
    # Get selected muscle groups
    selected_muscles = request.form.getlist('muscle_groups')
    
    # Add muscle groups to workout
    for muscle_name in selected_muscles:
        muscle_group = MuscleGroup.query.filter_by(name=muscle_name).first()
        if muscle_group:
            wm = WorkoutMuscleGroup(workout_id=workout.id, muscle_group_id=muscle_group.id)
            db.session.add(wm)
    
    # Add exercises to workout
    for muscle_name in selected_muscles:
        selected_exercises = request.form.getlist(f'exercises_{muscle_name}')

        # DEBUG
        print(f"Selected exercises for {muscle_name}: {selected_exercises}")
    
    for exercise_name in selected_exercises:


        # DEBUG: Afficher TOUS les champs du formulaire
        print("=== FORM DATA ===")
        for key, value in request.form.items():
            print(f"{key}: {value}")
        print("=================")
        
        for exercise_name in selected_exercises:
            exercise = Exercise.query.filter_by(name=exercise_name).first()
            if exercise:
                sets = request.form.get(f'sets_{muscle_name}_{exercise_name}', '3')
                reps = request.form.get(f'reps_{muscle_name}_{exercise_name}', '8-10')
                
                we = WorkoutExercise(
                workout_id=workout.id,
                exercise_id=exercise.id,
                sets=int(sets),
                reps=reps
                )
                db.session.add(we)
    
    db.session.commit()

    
    
    return redirect(url_for('workouts'))


@app.route('/delete/<int:workout_id>')
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    
    # Delete related WorkoutMuscleGroup entries
    WorkoutMuscleGroup.query.filter_by(workout_id=workout_id).delete()
    
    # Delete related WorkoutExercise entries
    WorkoutExercise.query.filter_by(workout_id=workout_id).delete()
    
    # Delete the workout
    db.session.delete(workout)
    db.session.commit()
    
    return redirect(url_for('workouts'))


@app.route('/stats')
def stats():
    user = get_demo_user()
    workouts = get_user_workouts(user.id)
    
    total_workouts = len(workouts)
    
    # Count muscle group frequency
    muscle_counts = {}
    for workout in workouts:
        muscle_groups = get_workout_muscle_groups(workout.id)
        for mg in muscle_groups:
            if mg.name in muscle_counts:
                muscle_counts[mg.name] += 1
            else:
                muscle_counts[mg.name] = 1
    
    most_trained = "N/A"
    least_trained = "N/A"
    if len(muscle_counts) > 0:
        most_trained = max(muscle_counts, key=muscle_counts.get)
        least_trained = min(muscle_counts, key=muscle_counts.get)
    
    return render_template('stats.html',
                         total_workouts=total_workouts,
                         most_trained=most_trained,
                         least_trained=least_trained,
                         muscle_stats=muscle_counts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)