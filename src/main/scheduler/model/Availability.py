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

        search_availability = "SELECT av.Username From Availabilities as av left join Appointment as ap " \
                              "on av.Time = ap.Time and av.Username = ap.Caregiver_Name " \
                              "where av.Time = '%s' and ap.Caregiver_Name is null order by av.Username"

        try:
            cursor.execute(search_availability % date)
            result = []
            for row in cursor:
                result.append(row[0])
            return result
        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()

    @staticmethod
    def get_available_caregiver(date):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        search_availability = "SELECT top 1 av.Username From Availabilities as av left join Appointment as ap " \
                              "on av.Time = ap.Time and av.Username = ap.Caregiver_Name " \
                              "where av.Time = '%s' and ap.Caregiver_Name is null order by av.Username "
        try:
            cursor.execute(search_availability % date)
            for row in cursor:
                return row[0]
            return
        except pymssql.Error:
            # print("Error occurred when updating vaccine availability")
            raise
        finally:
            cm.close_connection()

# TBD in part 2