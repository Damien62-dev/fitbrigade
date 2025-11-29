# FitBrigade 🏋️

A simple workout tracking web application built with Flask.

## 🔗 Links

- **Live Demo:** https://fitbrigade.onrender.com/
- **GitHub Repository:** https://github.com/Damien62-dev/fitbrigade

## About

FitBrigade is a workout tracking application that allows users to create, view, and manage their fitness workouts. The application helps users track exercises by muscle group, monitor their training progress, and view statistics about their workout history.

## Features

- **Create Workouts**: Add new workouts with custom names, dates, and exercises
- **Track Exercises**: Organize exercises by muscle groups (Chest, Back, Legs, etc.)
- **View Workout Details**: See complete information about each workout including sets and reps
- **Statistics Dashboard**: View your workout statistics and most/least trained muscle groups
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Delete Workouts**: Remove workouts you no longer need

## Technologies Used

- **Python 3.x**: Backend programming language
- **Flask**: Web framework for building the application
- **HTML5/CSS3**: Frontend structure and styling
- **JavaScript**: Interactive features (mobile navigation)
- **JSON**: Data storage for workouts

## Installation

### Prerequisites

- Python 3.x installed on your computer
- Basic knowledge of command line/terminal

### Setup Instructions

1. **Navigate to the project folder**
   ```bash
   cd "Python final project"
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   
   Navigate to: `http://localhost:5000`

## Project Structure

```
FitBrigade/
├── app.py                  # Main Flask application
├── workouts.json          # Workout data storage
├── static/
│   ├── css/
│   │   └── style.css      # Custom CSS styling
│   ├── images/            # Image assets
│   └── js/
│       └── script.js      # JavaScript for mobile menu
└── templates/
    ├── about.html         # About page
    ├── base.html          # Base template
    ├── create.html        # Create workout form
    ├── index.html         # Homepage
    ├── stats.html         # Statistics page
    ├── workout_detail.html # Individual workout view
    └── workouts.html      # All workouts list
```

## How to Use

### Creating a Workout

1. Click on **"Create Workout"** in the navigation menu
2. Fill in the workout name and date
3. Select muscle groups you want to train
4. Choose exercises for each muscle group
5. Enter sets and reps for each exercise
6. Add optional notes about your workout
7. Click **"Save Workout"** to create it

### Viewing Workouts

1. Click on **"My Workouts"** in the navigation
2. Browse all your saved workouts
3. Click **"View Details"** on any workout card to see full information
4. Click **"Delete"** to remove a workout

### Checking Statistics

1. Click on **"Statistics"** in the navigation
2. View your total number of workouts
3. See which muscle groups you train most/least
4. Review detailed breakdown by muscle group

## Muscle Groups Available

The application supports tracking exercises for the following muscle groups:

- Quadriceps
- Glutes
- Back
- Chest
- Shoulders
- Traps
- Hamstrings
- Biceps
- Triceps
- Forearms
- Calves
- Abs

## Data Storage

Workouts are stored in `workouts.json` in the following format:

```json
[
    {
        "id": 1,
        "name": "Leg Day",
        "date": "2024-11-22",
        "muscle_groups": ["Quadriceps", "Glutes"],
        "exercises": {
            "Quadriceps": [
                {
                    "name": "Back Squat",
                    "sets": "4",
                    "reps": "8"
                }
            ]
        },
        "notes": "Great workout!"
    }
]
```

## Author

Created as a student project for the Full Stack Developer course at UCD Professional Academy.

## License

This project is created for educational purposes.

## Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
- Google Fonts (Barlow & Oswald): https://fonts.google.com/