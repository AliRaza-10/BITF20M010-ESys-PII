
from flask import Flask, redirect ,render_template, request,make_response ,session,jsonify,json
from flask import redirect
from flask_session import Session
from Interest import Interest
from db import SMDBHandler  # Import the SMDBHandler class
app = Flask(__name__)
app.secret_key="bsjvhusdhg5565645"
@app.route('/')
def defaultPage(): 
    return render_template("login.html")
@app.route("/loggin",methods=["POST"])
def login():
    try:
        name=request.form["uname"]
        pwd = request.form["pwd"]
        dhlr=SMDBHandler("localhost","root","1234","std_interest_sys")
        interests = dhlr.getInterests()
        login=dhlr.login(name,pwd)
        if login:
            session['user_name'] = name
            session['show'] = 0
            session['dashboard'] = 0
            session['logout'] = 0
            session['submit'] = 0
            session['view']=0
            session['update'] = 0
            session['delete'] = 0
            return render_template("addStudent.html", interests=interests)
        else:
            return render_template("login.html", error="login failed")

    except Exception as e:
        return render_template("login.html",error="Login error"+str(e))
@app.route('/addStudent')
def render_add_student():
    try:
        # Fetch interests from the database
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        interests = dhlr.getInterests()

        return render_template("addStudent.html", interests=interests)

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/addInterest",methods=["POST"])
def addInterest():
    try:
       if request.method == 'POST':
        rollNo = request.form['rollNo']
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        dob = request.form['dob']
        city = request.form['city']
        interest = request.form['interest']
        department = request.form['department']
        degree = request.form['degree']
        subject = request.form['subject']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        if interest == "other":
                new_interest = request.form['newInterest']
                interest = new_interest
        interest= Interest(rollNo, name, email, gender, dob, city, interest, department, degree, subject, startDate, endDate)
        dhlr=SMDBHandler("localhost","root","1234","std_interest_sys")
        intrst=dhlr.addInterest(interest)
        print(intrst)
        if intrst == True:
            return render_template("addStudent.html",error="Interest Added SuccessFully")
        else :
              return render_template("addStudent.html", error="Interest Not Added SuccessFully")
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
# Add this route to your app.py
@app.route('/provincial_distribution_data')
def provincial_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        provincial_distribution = dhlr.get_provincial_distribution()
        return jsonify(provincial_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route("/age_distribution_data")
def age_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        age_distribution_data = dhlr.get_age_distribution()
        return jsonify(age_distribution_data)

    except Exception as e:
        return jsonify(error=str(e))
# Add a new route to get department distribution data
@app.route('/department_distribution_data')
def get_department_distribution_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        department_distribution = dhlr.get_department_distribution()
        return jsonify(department_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/gender_distribution_data')
def dashboard_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        gender_distribution = dhlr.get_gender_distribution()
        return jsonify(gender_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/degree_distribution_data')
def degree_distribution_chart():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        degree_distribution = dhlr.get_degree_distribution()
        return jsonify(degree_distribution)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/submission_chart_data')
def submission_chart_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        submission_chart_data = dhlr.get_submission_chart_data(30)
        return jsonify(submission_chart_data)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/last_30_days_activity_data')
def last_30_days_activity_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        
        # Fetch last 30 days activity data
        last_30_days_activity = dhlr.get_last_30_days_activity()
        
        return jsonify(last_30_days_activity)
    except Exception as e:
        return jsonify({'error': str(e)})  
# Add a new route to get last 24 hours activity data
@app.route('/last_24_hours_activity_data')
def get_last_24_hours_activity_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        last_24_hours_activity = dhlr.get_last_24_hours_activity()
        return jsonify(last_24_hours_activity)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/most_active_hours_last_30_days')
def get_most_active_hours_last_30_days():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        most_active_hours = dhlr.get_most_active_hours_last_30_days()
        return jsonify(most_active_hours)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/least_active_hours_last_30_days')
def get_least_active_hours_last_30_days():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        least_active_hours_last_30_days = dhlr.get_least_active_hours_last_30_days()
        return jsonify(least_active_hours_last_30_days)
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route('/dead_hours_last_30_days_data')
def get_dead_hours_last_30_days_data():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        dead_hours_last_30_days = dhlr.get_dead_hours_last_30_days()
        return jsonify(dead_hours_last_30_days)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/showalll")
def showalll():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        data_list = []

        pizza = dhlr.show_all()

        for id in pizza:
            data_list.append({
                "id": id[0],
                "RollNo": id[1],
                "Name": id[2],
                "Department": id[8],
                "Degree": id[9],
                "Dob": id[5],
                "City": id[6],
                "Interest": id[7],
            })

        return jsonify(data_list)  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)})
@app.route("/showall")
def showall():

    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")

        pizza = dhlr.show_all()
        if pizza != None:
            # print("hey")
            return render_template("ajex.html", pizzas=pizza)
        else:
            er = "Hello you didn't add any pizza "
            return render_template("ajex.html", error=er)
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/view/<int:id>")
def view_detail(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        pizza = dhlr.get_record_by_id(id)  # Replace with your method to fetch a specific record by ID
        if pizza:
            return render_template("viewStudentDetail.html", pizza=pizza)
        else:
            return "Record not found."
    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_record(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
        record = dhlr.get_record_by_id(id)

        if request.method == 'POST':
            # Get updated data from the form
            updated_rollNo = request.form['rollNo']
            updated_name = request.form['name']
            updated_email = request.form['email']
            updated_gender = request.form['gender']
            updated_dob = request.form['dob']
            updated_city = request.form['city']
            updated_interest = request.form['interest']
            updated_department = request.form['department']
            updated_degree = request.form['degree']
            updated_subject = request.form['subject']
            updated_startDate = request.form['startDate']
            updated_endDate = request.form['endDate']

            # Update the record
            dhlr.update_record(id, updated_rollNo, updated_name, updated_email, updated_gender, updated_dob,
                               updated_city, updated_interest, updated_department, updated_degree, updated_subject,
                               updated_startDate, updated_endDate)

            # Redirect to the showall route after updating
            return redirect("/showall")

        return render_template("updateStudent.html", record=record)

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/delete/<int:id>")
def delete_record(id):
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")

        # Delete the record
        dhlr.delete_record(id)

        # Redirect to the showall route after deleting
        return redirect("/showall")

    except Exception as e:
        return render_template("addStudent.html", error=str(e))
@app.route("/alih", methods=["GET", "POST"])
def dashboard():
    try:
        dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")

        # Fetch data for the dashboard
        top_interests = dhlr.get_top_interests(5)
        bottom_interests = dhlr.get_bottom_interests(5)
        distinct_interests_count = dhlr.get_distinct_interests_count()
        provincial_distribution = dhlr.get_provincial_distribution()
        submission_chart_data = dhlr.get_submission_chart_data(30)
        age_distribution = dhlr.get_age_distribution()
        department_distribution = dhlr.get_department_distribution()
        degree_distribution = dhlr.get_degree_distribution()
        gender_distribution = dhlr.get_gender_distribution()
        studying_count = dhlr.get_studying_count()
        recently_enrolled_count = dhlr.get_recently_enrolled_count()
        about_to_graduate_count = dhlr.get_about_to_graduate_count()
        graduated_count = dhlr.get_graduated_count()


        return render_template(
            "dashboard.html",
            top_interests=top_interests,
            bottom_interests=bottom_interests,
            distinct_interests_count=distinct_interests_count,
            provincial_distribution=provincial_distribution,
            submission_chart_data=submission_chart_data,
            age_distribution=age_distribution,
            department_distribution=department_distribution,
            degree_distribution=degree_distribution,
            gender_distribution=gender_distribution,
            studying_count=studying_count,
            recently_enrolled_count=recently_enrolled_count,
            about_to_graduate_count=about_to_graduate_count,
            graduated_count=graduated_count
        )

    except Exception as e:
        return render_template("addStudent.html", error=str(e))

@app.route('/user_activity', methods=['POST'])
def user_activity():
    try:
        # Get the type of user activity and user name from the request
        activity_type = request.form.get('activity_type')
        user_name = session.get('user_name')

        # Initialize counts when the user logs in
        if 'show' not in session:
            session['show'] = 0
        if 'dashboard' not in session:
            session['dashboard'] = 0
        if 'logout' not in session:
            session['logout'] = 0
        if 'submit' not in session:
            session['submit'] = 0
        if 'view' not in session:
            session['View'] = 0
        if 'update' not in session:
            session['Update'] = 0
        if 'delete' not in session:
            session['Delete'] = 0
        # Increment the corresponding count in the session
        if activity_type == 'show':
            session['show'] += 1
        elif activity_type == 'dashboard':
            session['dashboard'] += 1
        elif activity_type == 'View':
            session['View'] += 1
        elif activity_type == 'Update':
            session['Update'] += 1
        elif activity_type == 'Delete':
            session['Delete'] += 1
        elif activity_type == 'logout':
            session['logout'] += 1
            # Store all user activity counts in the database when the user logs out
            dhlr = SMDBHandler("localhost", "root", "1234", "std_interest_sys")
            dhlr.store_user_activity(
                user_name,
                session['show'],
                session['dashboard'],
                session['logout'],
                session['submit']
            )

        elif activity_type == 'submit':
            session['submit'] += 1
        
        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/logout')
def Logout(): 
    return render_template("login.html")

if __name__ == '__main__':
    app.run()