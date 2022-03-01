class ParkingLot():
    def __init__(self):
        self.parking_lot_vacancies = []
        self.valets = ['Roberto', 'João', 'Carlos', 'Bruno']
        
    # retorna True se a vaga está disponível 
    def verifyParkingLot(self, vacancy):
        if len(self.parking_lot_vacancies) > 0:
            for vehicle in self.parking_lot_vacancies:
                if vacancy == vehicle.vacancy:
                    return False
                else:
                    return True
        else:
            return True
    
    def verifyValet(self, valet_name):
        if valet_name in self.valets:
            return True
        else:
            return False
        
    def verifyVacancy(self, vacancy, vacancy_floor):
        if vacancy in range(1,200) and vacancy_floor in [1,2]:
            return True
        else:
            return False

    # Verifies if vehicle is in parking lot
    def verifyVehicleObject(self, license_plate):
        for vehicle in self.parking_lot_vacancies:
            if license_plate == vehicle.license_plate:
                return True
            else:
                return False
        
    def returnParkingLot(self):
        for vehicle in self.parking_lot_vacancies:
            print(vehicle)



