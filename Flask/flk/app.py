from flask import Flask, render_template, request, redirect, url_for, session
from ml_models import models, model_accuracies, model_display_names, linear_model
import json
import os

app = Flask(__name__)
app.secret_key = "change_this_to_something_random"

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = load_users()
        if username in users:
            return render_template('signup.html', error="Username already exists")

        users[username] = password
        save_users(users)
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = load_users()
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'user' not in session:
        return redirect(url_for('login'))

    name = request.form.get("name")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    alternate_mobile = request.form.get("alternate_mobile")
    date_of_birth = request.form.get("date_of_birth")
    age = request.form.get("age")
    gender = request.form.get("gender")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    pincode = request.form.get("pincode")
    qualification = request.form.get("qualification")
    college = request.form.get("college")
    department = request.form.get("department")
    course = request.form.get("course")
    year = request.form.get("year")
    cgpa = request.form.get("cgpa")
    languages = request.form.get("languages")
    skills = request.form.get("skills")
    blood_group = request.form.get("blood_group")
    emergency_contact = request.form.get("emergency_contact")
    guardian_name = request.form.get("guardian_name")

    print("\n===== STUDENT DETAILS =====")
    print("Name:", name)
    print("Email:", email)
    print("Mobile:", mobile)
    print("Alternate Mobile:", alternate_mobile)
    print("Date of Birth:", date_of_birth)
    print("Age:", age)
    print("Gender:", gender)
    print("City:", city)
    print("State:", state)
    print("Country:", country)
    print("Pincode:", pincode)
    print("Qualification:", qualification)
    print("College:", college)
    print("Department:", department)
    print("Course:", course)
    print("Year of Passout:", year)
    print("CGPA:", cgpa)
    print("Languages Known:", languages)
    print("Skills:", skills)
    print("Bloodgroup:", blood_group)
    print("Emergency Contact Number:", emergency_contact)
    print("Guardian Name:", guardian_name)

    return render_template(
        'result.html',
        name=name,
        email=email,
        mobile=mobile,
        alternate_mobile=alternate_mobile,
        date_of_birth=date_of_birth,
        age=age,
        gender=gender,
        city=city,
        state=state,
        country=country,
        pincode=pincode,
        qualification=qualification,
        college=college,
        department=department,
        course=course,
        year=year,
        cgpa=cgpa,
        languages=languages,
        skills=skills,
        blood_group=blood_group,
        emergency_contact=emergency_contact,
        guardian_name=guardian_name
    )

@app.route('/select-model')
def select_model():
    return render_template(
        'select_model.html',
        accuracies=model_accuracies,
        display_names=model_display_names
    )

@app.route('/predict', methods=['POST'])
def predict():
    model_key = request.form.get('model')
    cgpa = float(request.form.get('cgpa'))

    chosen_model = models[model_key]
    result = chosen_model.predict([[cgpa]])[0]
    output = "PLACED" if result == 1 else "NOT PLACED"

    return render_template(
        'predict_result.html',
        model_name=model_display_names[model_key],
        cgpa=cgpa,
        result=output
    )

@app.route('/predict-package', methods=['GET', 'POST'])
def predict_package():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = None
    cgpa = None

    if request.method == 'POST':
        cgpa = float(request.form.get('cgpa'))
        prediction = linear_model.predict([[cgpa]])[0]
        result = round(prediction, 2)

    return render_template('predict_package.html', result=result, cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
