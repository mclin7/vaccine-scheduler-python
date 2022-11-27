import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql


class Availability:
    def __init__(self, username, patient_name, caregiver_name, vaccine_name, time):
        self.id = id
        self.patient_name = patient_name
        self.caregiver_name = caregiver_name
        self.vaccine_name = vaccine_name
        self.time = time

    @staticmethod
    def get_availabilities(date):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        search_availability = "SELECT Username From Availabilities WHERE Time = %s and isReserved = %s order by Username"
        try:
            cursor.execute(search_availability % (date, 0))
            result = []
            for row in cursor:
                result.append(row[0])
            return result
        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()
            return []

    @staticmethod
    def get_available_caregiver(date):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        search_availability = "SELECT Username From Availabilities WHERE Time = %s and isReserved = %s order by Username limit 1"
        try:
            cursor.execute(search_availability % (date, 0))
            for row in cursor:
                return row[0]
            return
        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()
            return []

    @staticmethod
    def update_availability(name, date):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        reserved = "UPDATE Availabilities SET isReserved = %s WHERE Username = %s and Time = %s"
        try:
            cursor.execute(reserved % (1, name, date))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            raise
        finally:
            cm.close_connection()

# TBD in part 2