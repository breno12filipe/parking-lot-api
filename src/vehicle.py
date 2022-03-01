import hashlib
from random import randint
from datetime import datetime
from src.parkingLot import ParkingLot

class Vehicle():
    # NOTE: Class Constructor
    def __init__(self, cpf, license_plate, vacancy_floor, vacancy, valet_name):
        # NOTE: Protected attributes
        self._cpf = cpf
        self._license_plate = license_plate
        self.vacancy_floor = vacancy_floor
        self.vacancy = vacancy
        self.valet_name = valet_name
        self.parking_time = datetime.now()
        self.parking_time_value = 5.0
        self.ticket = self.generateTicket()
    
    # NOTE: Generate ticket
    def generateTicket(self):
        # TODO: Must verify if it's unique before returning
        random_int = str(randint(1,200))
        random_int_bytes = str.encode(random_int)
        hash_object = hashlib.sha1(random_int_bytes)
        pbHash = hash_object.hexdigest()
        return pbHash
        
    def generateParkingValue(self):
        #TODO: Pegar apenas a hora
        sub_time_val = self.parking_time - datetime.now()
        return sub_time_val * self.parking_time_value
    

