import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql


class Appointment:
    def __init__(self, patient_name, caregiver_name, vaccine_name, time):
        self.ID = None
        self.patient_name = patient_name
        self.caregiver_name = caregiver_name
        self.vaccine_name = vaccine_name
        self.time = time

    def save_to_db(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        add_appointment = "INSERT INTO Appointment (Patient_Name, Caregiver_Name, Vaccine_Name, Time)VALUES ('%s', '%s', '%s', '%s')"
        try:
            app_id = cursor.execute(add_appointment % (self.patient_name, self.caregiver_name, self.vaccine_name, self.time))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
            self.ID = cursor.lastrowid
        except pymssql.Error:
            raise
        finally:
            cm.close_connection()
# TBD in part 2