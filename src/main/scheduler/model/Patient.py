import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
sys.path.append("../model/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
from model.Availability import Availability
from model.Appointment import Appointment
from model.Vaccine import Vaccine
import pymssql


class Patient:
    def __init__(self, username, password=None, salt=None, hash=None):
        self.username = username
        self.password = password
        self.salt = salt
        self.hash = hash

    # getters
    def get(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor(as_dict=True)

        get_caregiver_details = "SELECT Salt, Hash FROM Patients WHERE Username = %s"
        try:
            cursor.execute(get_caregiver_details, self.username)
            for row in cursor:
                curr_salt = row['Salt']
                curr_hash = row['Hash']
                calculated_hash = Util.generate_hash(self.password, curr_salt)
                if not curr_hash == calculated_hash:
                    # print("Incorrect password")
                    cm.close_connection()
                    return None
                else:
                    self.salt = curr_salt
                    self.hash = calculated_hash
                    cm.close_connection()
                    return self
        except pymssql.Error as e:
            raise e
        finally:
            cm.close_connection()
        return None

    def get_username(self):
        return self.username

    def get_salt(self):
        return self.salt

    def get_hash(self):
        return self.hash

    def save_to_db(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        add_patients = "INSERT INTO Patients VALUES (%s, %s, %s)"
        try:
            cursor.execute(add_patients, (self.username, self.salt, self.hash))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            raise
        finally:
            cm.close_connection()

    def reserve(self, caregiver, vaccine, date):
        if self.is_reserved(date):
            print('Already reserved, Please try again!')
            return

        vaccine.decrease_available_doses(1)
        appointment = Appointment(self.username, caregiver, vaccine.get_vaccine_name(), date)
        appointment.save_to_db()
        print("Appointment ID: {appointment_id}, Caregiver username: {username}".format(
            appointment_id = appointment.ID,
            username = self.username
        ))

    def is_reserved(self, date):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        is_reserved = "SELECT Patient_Name FROM Appointment WHERE Patient_Name = '%s' and Time = '%s'"
        try:
            cursor.execute(is_reserved % (self.username, date))
            for _ in cursor:
                return True
            return False
        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()

    def show_appointment(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        searchavailability = "SELECT ID, Vaccine_Name, Time, Caregiver_Name From Appointment WHERE Patient_Name = '%s' order by ID"
        try:
            cursor.execute(searchavailability % (self.username, ))
            print("Appointment listed below:")
            has = False
            for row in cursor:
                print("appointment ID: %s, vaccine name: %s, date: %s, caregiver name: %s" % row)
                has = True

            if not has:
                print('No appointment yet!')

        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()
