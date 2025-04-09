from flask import Flask, render_template, request, redirect, url_for, jsonify
from advisor import CourseAdvisor
from datetime import datetime
import json
import os

app = Flask(__name__)
advisor = CourseAdvisor()

# Ensure the data directory exists
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        major = request.form.get('major')
        completed_courses = [c.strip() for c in request.form.getlist('completed') if c.strip()]
        interests = [i.strip().lower() for i in request.form.get('interests', '').split(',') if i.strip()]
        gpa = float(request.form.get('gpa', 0))
        learning_style = request.form.get('learning_style')
        difficulty_preference = request.form.get('difficulty_preference')
        time_commitment = request.form.get('time_commitment')
        career_goals = request.form.get('career_goals', '')
        group_projects = request.form.get('group_projects', 'any').lower()

        student_data = {
            "name": name,
            "major": major,
            "completed": completed_courses,
            "interests": interests,
            "gpa": gpa,
            "learning_style": learning_style,
            "difficulty_preference": difficulty_preference,
            "time_commitment": time_commitment,
            "career_goals": career_goals,
            "group_projects": group_projects
        }
        print("Student Data:", student_data)
        recommendations = advisor.get_recommendations(student_data)
        return render_template('recommendations.html',
                               student=student_data,
                               recommendations=recommendations,
                               courses=advisor.courses,
                               now=datetime.now())

    return render_template('index.html',
                           courses=list(advisor.courses.keys()),
                           difficulties=set(c["difficulty"] for c in advisor.courses.values()))


@app.route('/api/course_descriptions')
def get_course_descriptions():
    try:
        with open(os.path.join(DATA_DIR, 'course_descriptions.json'), 'r') as f:
            descriptions = json.load(f)
        return jsonify(descriptions)
    except FileNotFoundError:
        return jsonify({})
    except json.JSONDecodeError:
        return jsonify({})
    

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)