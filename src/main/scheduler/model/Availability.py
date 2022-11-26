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

# TBD in part 2