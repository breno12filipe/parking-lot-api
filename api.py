from distutils.log import debug
from flask import Flask, request
from flask_restful import Resource, Api
from src.parkingLot import ParkingLot
from src.vehicle import Vehicle


app = Flask(__name__)
api = Api(app)
prkLt = ParkingLot()

# TODO: Estudar a junção das duas classes Vehicle() e VehicleOps()
# TODO: Existe uma redundância de nomes entre as classes Vehicle(src.vehicle) e Vehicle(api.py)
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#endpoints
class Vehicle(Resource):
    # Post method is equivalent to park vehicle 
    def post(self):
        data = request.json
        try:
        # TODO: Verificar se a placa já não está registrada e o cpf também
            if prkLt.verifyVacancy(data['vacancy'], data['vacancy_floor']):
                if prkLt.verifyParkingLot(data['vacancy']):
                    if prkLt.verifyValet(data['valet_name']):
                        v0 = Vehicle(data["cpf"],
                                    data["license_plate"],
                                    data["vacancy_floor"],
                                    data["vacancy"],
                                    data["valet_name"])
                            
                        prkLt.parking_lot_vacancies.append(v0)
                        return v0.ticket
                    else:
                        return 'This valet is not registered on system'
                else:
                    return 'Sorry, this vacancy is already filled'
            else:
                return 'Error, this vacancy does not exists'
        except:
            return 'Sorry, It was not possible to park the vehicle'
        
    # NOTE: Returns all vehicles
    def get(self):
        return [
            {'cpf':vehicle._cpf,
             'license_plate':vehicle._license_plate,
             'vacancy_floor': vehicle.vacancy_floor,
             'vacancy': vehicle.vacancy,
             'valet_name': vehicle.valet_name,
             'parking_time': str(vehicle.parking_time),
             'parking_time_value': vehicle.parking_time_value,
             'ticket': vehicle.ticket
            }
            for vehicle in prkLt.parking_lot_vacancies]
            
# NOTE: Classes must follow Pascal case
class VehicleOps(Resource):
    # delete method is equivalent to release vehicle
    def delete(self, ticket):
        for vehicle in prkLt.parking_lot_vacancies:
            if ticket == vehicle.ticket:
                prkLt.parking_lot_vacancies.remove(vehicle)
                del vehicle
                
                return 'Vehicle Released'
            else:
                return 'Invalid Ticket'
    
# NOTE: Resource names (URN) must follow kebab-case
api.add_resource(Vehicle, '/vehicles')
api.add_resource(VehicleOps, '/vehicle-operations/<string:ticket>')

if __name__ == '__main__':
    app.run(debug=True)