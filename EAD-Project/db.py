from datetime import datetime
from Interest import Interest
import pymysql
import traceback
import random
from datetime import timedelta, date,datetime
from collections import Counter
class SMDBHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database
        self.deleted_record_id = None
    def login(self,user,pwd):
        mydb = None
        mydbCursor = None
        login = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "select username,password from login where username=%s and password=%s"
            args = (user,pwd)
            mydbCursor.execute(sql, args)
            row=mydbCursor.fetchone()
            if row!= None:
                login=True
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
            return login
    def addInterest(self, obj):
        mydb = None
        mydbCursor = None
        login = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            
            # Exclude 'id' from the INSERT statement if it's an auto-increment column
            sql = "INSERT INTO interest(RollNo, Name, Email, Gender, Dob, City, Interest, Department, Degree, Subject, StartDate, EndDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            arg = (obj.RollNo, obj.Name, obj.Email, obj.Gender, obj.Dob, obj.City, obj.Interest, obj.Department, obj.Degree, obj.Subject, obj.StartDate, obj.EndDate)
            mydbCursor.execute(sql, arg)
            
            mydb.commit()
            login = True
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()
            print(login)
            return login
    def getInterests(self):
        mydb = None
        mydbCursor = None
        interests = []

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch interests from the database
            sql = "SELECT DISTINCT Interest FROM interest"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()

            interests = [row[0] for row in rows]

        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return interests
    def show_all(self):

        mydb = None
        mydbCursor = None
        flag = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "select * from interest"
            mydbCursor.execute(sql)
            row = mydbCursor.fetchall()
            # if len(row) > 0:
            #     flag = row
            flag = row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
            return flag
    def show_data(self):

        mydb = None
        mydbCursor = None
        flag = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "select * from interest"
            mydbCursor.execute(sql)
            row = mydbCursor.fetchall()
            flag = row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
            return flag
    def get_record_by_id(self, record_id):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM interest WHERE id=%s"
            mydbCursor.execute(sql, (record_id,))
            row = mydbCursor.fetchone()
            return row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    def update_record(self, record_id, updated_rollNo, updated_name, updated_email, updated_gender, updated_dob,
                      updated_city, updated_interest, updated_department, updated_degree, updated_subject,
                      updated_startDate, updated_endDate):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Update the record
            sql = """UPDATE interest 
                     SET RollNo=%s, Name=%s, Email=%s, Gender=%s, Dob=%s, City=%s, Interest=%s, 
                         Department=%s, Degree=%s, Subject=%s, StartDate=%s, EndDate=%s
                     WHERE id=%s"""
            args = (updated_rollNo, updated_name, updated_email, updated_gender, updated_dob, updated_city,
                    updated_interest, updated_department, updated_degree, updated_subject, updated_startDate,
                    updated_endDate, record_id)
            mydbCursor.execute(sql, args)

            mydb.commit()

        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()
    def delete_record(self, record_id):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "DELETE FROM interest WHERE id=%s"
            mydbCursor.execute(sql, (record_id,))
            mydb.commit()
            self.deleted_record_id = record_id
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    def get_provincial_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT City, COUNT(*) as city_count FROM interest GROUP BY City"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            distribution_data = [{"label": row[0], "count": row[1]} for row in rows]
            return distribution_data
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_age_distribution(self):
        # Fetch age distribution data from the database
        # (You'll need to calculate age based on Date of Birth)
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT YEAR(CURDATE()) - YEAR(Dob) - (RIGHT(CURDATE(), 5) < RIGHT(Dob, 5)) as age, COUNT(*) as age_count FROM interest GROUP BY age"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            age_distribution = [{"age": row[0], "count": row[1]} for row in rows]
            return age_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    # Example get_department_distribution() method in db.py
    def get_department_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Department, COUNT(*) as department_count FROM interest GROUP BY Department"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            distribution_data = [{"label": row[0], "count": row[1]} for row in rows]
            return distribution_data
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()


    def get_degree_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Degree, COUNT(*) as degree_count FROM interest GROUP BY Degree"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            degree_distribution = [{"degree": row[0], "count": row[1]} for row in rows]
            return degree_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()


    def get_gender_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Gender, COUNT(*) as gender_count FROM interest GROUP BY Gender"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            gender_distribution = [{"gender": row[0], "count": row[1]} for row in rows]
            return gender_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_top_interests(self, limit):
        mydb = None
        mydbCursor = None
        interests = []

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch top interests excluding the deleted row
            if self.deleted_record_id is not None:
                deleted_ids = [int(id) for id in self.deleted_record_id.split(",")]
                deleted_ids_str = ",".join(map(str, deleted_ids))
                sql = f"SELECT DISTINCT id, Interest FROM interest WHERE id NOT IN ({deleted_ids_str}) ORDER BY id ASC LIMIT {limit}"
            else:
                sql = f"SELECT DISTINCT id, Interest FROM interest ORDER BY id ASC LIMIT {limit}"

            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()

            interests = [row[1] for row in rows]

        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return interests

    
    
    def get_bottom_interests(self, limit):
        mydb = None
        mydbCursor = None
        interests = []

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch bottom interests excluding the deleted row
            if self.deleted_record_id is not None:
                deleted_ids = [int(id) for id in self.deleted_record_id.split(",")]
                deleted_ids_str = ",".join(map(str, deleted_ids))
                sql = f"SELECT DISTINCT id, Interest FROM interest WHERE id NOT IN ({deleted_ids_str}) ORDER BY id DESC LIMIT {limit}"
            else:
                sql = f"SELECT DISTINCT id, Interest FROM interest ORDER BY id DESC LIMIT {limit}"

            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()

            interests = [row[1] for row in rows]  

        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return interests

    def get_distinct_interests_count(self):
        mydb = None
        mydbCursor = None
        count = 0

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch distinct interests count
            sql = "SELECT COUNT(DISTINCT Interest) FROM interest"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count
   
    def get_recently_enrolled_count(self):
        mydb = None
        mydbCursor = None
        count = 0

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch count of recently enrolled students
            sql = "SELECT COUNT(*) FROM interest WHERE StartDate >= CURDATE() - INTERVAL 1 MONTH"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count

    def get_about_to_graduate_count(self):
        mydb = None
        mydbCursor = None
        count = 0

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch count of students about to graduate
            sql = "SELECT COUNT(*) FROM interest WHERE EndDate >= CURDATE() AND EndDate <= CURDATE() + INTERVAL 1 MONTH"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count

    def get_graduated_count(self):
        mydb = None
        mydbCursor = None
        count = 0

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch count of graduated students
            sql = "SELECT COUNT(*) FROM interest WHERE EndDate < CURDATE()"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count

    # Add this method to your SMDBHandler class in db.py

    def get_studying_count(self):
        mydb = None
        mydbCursor = None
        count = 0

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Fetch count of students currently studying
            sql = "SELECT COUNT(*) FROM interest WHERE StartDate <= CURDATE() AND (EndDate >= CURDATE() OR EndDate IS NULL)"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count
    def get_user_activity(self, username):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connection.cursor()

            # Fetch user activity data
            self.cursor.execute("SELECT * FROM user_activity WHERE username=%s", (username,))
            user_activity_data = self.cursor.fetchone()

            if user_activity_data:
                # If user activity data exists, return it as a dictionary
                columns = [desc[0] for desc in self.cursor.description]
                user_activity_dict = dict(zip(columns, user_activity_data))
                return user_activity_dict
            else:
                # If no user activity data exists, return a dictionary with zero counts
                return {'show_count': 0, 'dashboard_count': 0, 'logout_count': 0}

        except Exception as e:
            print(f"Error getting user activity: {e}")

        finally:
            # Close the database connection
            if self.cursor is not None:
                self.cursor.close()

            if self.connection is not None:
                self.connection.close()
    def store_user_activity(self, username, show_count, dashboard_count, logout_count, submit_count):
        try:
            # Generate random counts for view, delete, and update
            view_count = random.randint(0, 3)
            delete_count = random.randint(0, 3)
            update_count = random.randint(0, 3)

            # Connect to the database
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connection.cursor()
            query = """
            INSERT INTO user_activity (username, show_count, dashboard_count, logout_count, activity_date, login_count, submit_count, view_count, delete_count, update_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Use placeholders to insert values into the query
            self.cursor.execute(query, (username, show_count, dashboard_count, logout_count, datetime.now(), logout_count, submit_count, view_count, delete_count, update_count))

            self.connection.commit()
            return True

        except Exception as e:
            print(f"Error storing user activity: {e}")
            traceback.print_exc()
            self.connection.rollback()
            return False

        finally:
            # Close the database connection
            if self.cursor is not None:
                self.cursor.close()

            if self.connection is not None:
                self.connection.close()
    
    def get_submission_chart_data(self, days):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connection.cursor()

            # Calculate the start date (30 days ago from today)
            start_date = date.today() - timedelta(days=days)

            # Query to get the count of form submissions each day in the last 30 days
            query = """
                SELECT DATE(activity_date) as submission_date, COUNT(*) as submission_count
                FROM user_activity
                WHERE submit_count > 0
                    AND activity_date >= %s
                GROUP BY submission_date
                ORDER BY submission_date
            """
            self.cursor.execute(query, (start_date,))
            rows = self.cursor.fetchall()

            # Format the data for submission chart
            submission_chart_data = [{"date": str(row[0]), "count": row[1]} for row in rows]

            return submission_chart_data

        except Exception as e:
            print(f"Error fetching submission chart data: {e}")

        finally:
            # Close the database connection
            if self.cursor is not None:
                self.cursor.close()

            if self.connection is not None:
                self.connection.close()

    def get_last_30_days_activity(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Calculate the date 30 days ago from today
            thirty_days_ago = datetime.now() - timedelta(days=30)

            # Use SUM() to get the total count of activities for each day
            sql = f"""
                SELECT DATE(activity_date) as date, 
                    SUM(show_count + dashboard_count + logout_count + login_count + submit_count + view_count + delete_count + update_count) as total_count
                FROM user_activity 
                WHERE activity_date >= '{thirty_days_ago}' 
                GROUP BY DATE(activity_date)
            """
            mydbCursor.execute(sql)

            rows = mydbCursor.fetchall()
            last_30_days_activity = [{"date": row[0], "count": row[1]} for row in rows]

            return last_30_days_activity
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    
    def get_last_24_hours_activity(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Calculate the datetime 24 hours ago from now
            twenty_four_hours_ago = datetime.now() - timedelta(hours=24)

            sql = f"""
                SELECT
                    DATE_FORMAT(activity_date, '%Y-%m-%d %H:%i:00') as datetime_interval,
                    SUM(show_count + dashboard_count + logout_count + login_count + submit_count + view_count + delete_count + update_count) as total_count
                FROM
                    user_activity
                WHERE
                    activity_date >= '{twenty_four_hours_ago}'
                GROUP BY
                    datetime_interval, HOUR(activity_date), MINUTE(activity_date) div 15
                """
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            last_24_hours_activity = [{"datetime_interval": row[0], "total_count": row[1]} for row in rows]

            return last_24_hours_activity
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_most_active_hours_last_30_days(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            thirty_days_ago = datetime.now() - timedelta(days=30)

            sql = """
                SELECT
                    DATE_FORMAT(activity_date, '%Y-%m-%d %H:00:00') as datetime_interval,
                    SUM(show_count + dashboard_count + logout_count + login_count + submit_count + view_count + delete_count + update_count) as total_count
                FROM
                    user_activity
                WHERE
                    activity_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY
                    datetime_interval
                ORDER BY
                    total_count DESC
                LIMIT 10;
                """
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            most_active_hours = [{"hour": row[0], "activity_count": row[1]} for row in rows]

            return most_active_hours
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    def get_least_active_hours_last_30_days(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = """
                    SELECT
                    DATE_FORMAT(activity_date, '%Y-%m-%d %H:00:00') as datetime_interval,
                    SUM(show_count + dashboard_count + logout_count + login_count + submit_count + view_count + delete_count + update_count) as total_count
                FROM
                    user_activity
                WHERE
                    activity_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY
                    datetime_interval
                ORDER BY
                    total_count ASC
                    LIMIT 10;
                """
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            least_active_hours_last_30_days = [{"hour": row[0], "activity_count": row[1]} for row in rows]

            return least_active_hours_last_30_days
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()


    def get_dead_hours_last_30_days(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            sql = """
                SELECT
                    DISTINCT DATE_FORMAT(date_range.datetime, '%Y-%m-%d %H:00:00') as datetime_interval
                FROM
                    (
                        SELECT
                            DATE_ADD(CURDATE(), INTERVAL - (a.a + (10 * b.a) + (100 * c.a)) DAY_HOUR) AS datetime
                        FROM
                            (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS a
                            CROSS JOIN (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS b
                            CROSS JOIN (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS c
                    ) date_range
                LEFT JOIN
                    user_activity ON DATE_FORMAT(user_activity.activity_date, '%Y-%m-%d %H:00:00') = DATE_FORMAT(date_range.datetime, '%Y-%m-%d %H:00:00')
                WHERE
                    date_range.datetime >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND
                    user_activity.activity_date IS NULL;
            """

            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            dead_hours_last_30_days = [{"datetime_interval": row[0]} for row in rows]

            return dead_hours_last_30_days
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
