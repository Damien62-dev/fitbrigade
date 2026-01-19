from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

def utcnow():
    return datetime.now(timezone.utc)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)

    workouts = db.relationship('Workout', back_populates='user')
    goals = db.relationship('Goal', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'
    
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)

    user = db.relationship('User', back_populates='workouts',  )  
    workout_muscle_groups = db.relationship('WorkoutMuscleGroup', back_populates='workout')
    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')

    def __repr__(self):
        return f'<Workout {self.name} on {self.date}>'
    
class MuscleGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    exercises = db.relationship('Exercise', back_populates='muscle_group',  )
    workout_muscle_groups = db.relationship('WorkoutMuscleGroup', back_populates='muscle_group')

    def __repr__(self):
        return f'<MuscleGroup {self.name}>'

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_group.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    muscle_group = db.relationship('MuscleGroup', back_populates='exercises',  )
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')
    goals = db.relationship('Goal', back_populates='exercise',  )

    def __repr__(self):
        return f'<Exercise {self.name}>'

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    target_weight = db.Column(db.Float, nullable=True)
    target_reps = db.Column(db.Integer, nullable=True)
    deadline = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=utcnow, nullable=False)

    user = db.relationship('User', back_populates='goals')
    exercise = db.relationship('Exercise', back_populates='goals')

    def __repr__(self):
        return f'Goal(id={self.id}, name="{self.name}", user_id={self.user_id})'

# Table between workoutd and muscle groups
class WorkoutMuscleGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_group.id'), nullable=False)

    workout = db.relationship('Workout', back_populates='workout_muscle_groups')
    muscle_group = db.relationship('MuscleGroup', back_populates='workout_muscle_groups') 

    def __repr__(self):
        return f'<WorkoutMuscleGroup Workout ID: {self.workout_id}, MuscleGroup ID: {self.muscle_group_id}>'


# Table between workouts and exercises
class WorkoutExercise (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.String(20), nullable=False)

    workout = db.relationship('Workout', back_populates='workout_exercises') 
    exercise = db.relationship('Exercise', back_populates='workout_exercises') 

    def __repr__(self):
        return f'<WorkoutExercise Workout ID: {self.workout_id}, Exercise ID: {self.exercise_id}>'