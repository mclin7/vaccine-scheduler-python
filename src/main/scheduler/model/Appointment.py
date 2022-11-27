import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql


class Appointment:
    def __init__(self, patient_name, caregiver_name, vaccines_name, time):
        self.ID = None
        self.patient_name = patient_name
        self.caregiver_name = caregiver_name
        self.vaccines_name = vaccines_name
        self.time = time


# TBD in part 2