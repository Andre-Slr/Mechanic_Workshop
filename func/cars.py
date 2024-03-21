from data.db_manager import DB
from tkinter import messagebox
from datetime import date, datetime

###### CADA VEHÍCULO VA LIGADO A UN CLIENTE ######

class Cars():
    def __init__(self, car_plate=None, client_ID=None, brand=None, model=None):
        self.car_plate = car_plate
        self.client_ID = client_ID
        self.brand = brand
        self.model = model

        self.db = DB()

    # Creación de vehículo, se usará como "Guardar" en el programa
    def newCar(self, car_plate, client_ID, brand, model):
        if not self.verify_plates(car_plate):
            now_date = date.today().strftime("%Y-%m-%d")
            now_time = datetime.now().strftime("%H:%M:%S")
            insert_car = f"""
            INSERT INTO 
                cars    
                    (car_plate, client_ID, brand, model, date_enter, time_enter)
            VALUES
                ('{car_plate}', {client_ID}, '{brand}', '{model}', '{now_date}', '{now_time}');
            """
            self.db.execute(insert_car)
        else:
            messagebox.showwarning("Error","Car plate already exists")


    # Editar vehículo
    def editCar(self, car_plate, client_ID, brand, model, car_id):
        # Edita todos los atributos del vehículo que tenga la placa "car_plate"
        edit_car = f"""
            UPDATE
                cars
            SET
                car_plate = '{car_plate}',
                client_ID = {client_ID},
                brand = '{brand}',
                model = '{model}'
            WHERE
                id = '{car_id}'
        """
        
        self.db.execute(edit_car)

        # Se regresa el vehículo encontrado de forma
        # [0]=car_plate, [1]=client_ID, [2]=brand, [3]=model, [4]=id
        return self.lookForCarPlate(car_plate)


    # Eliminar vehículo PERMANENTEMENTE
    def deleteCar(self, car_plate):
        delete_client = f"DELETE FROM cars WHERE car_plate = {car_plate}"

        self.db.execute(delete_client)

    # Busca un vehículo por su placa
    def lookForCarPlate(self, car_plate):
        try:
            search_car = f"""
                SELECT
                    car_plate,
                    client_ID, 
                    brand,
                    model,
                    id
                FROM
                    cars
                WHERE
                    car_plate = '{car_plate}'
            """
            found_car = self.db.fetchall(search_car)[0]

            # Se regresa el vehículo encontrado de forma
            # [0]=car_plate, [1]=client_ID, [2]=brand, [3]=model, [4]=id
            return found_car
        except:
            return False
        
    # Busca un vehículo por su id
    def lookForCarID(self, id):
        try:
            search_car = f"""
                SELECT
                    car_plate,
                    client_ID, 
                    brand,
                    model
                FROM
                    cars
                WHERE
                    id = '{id}'
            """
            found_car = self.db.fetchall(search_car)[0]

            # Se regresa el vehículo encontrado de forma
            # [0]=car_plate, [1]=client_ID, [2]=brand, [3]=model
            return found_car
        except:
            return False

    # Mostrar lista de vehículos
    def showListCars(self):
        show_cars = """
            SELECT
                car_plate,
                client_ID,
                brand,
                model
            FROM
                cars
        """
        list_cars = []
        list_cars = self.db.fetchall(show_cars)

        # Se regresa una matriz de vehículos [m][n] donde
            # m = vehículos registrados
            # n = ([0]=car_plate, [1]=client_ID, [2]=brand, [3]=model)
        return list_cars


    # Mostrar lista de vehículos
    def showListCarsFull(self):
        show_cars = " SELECT * FROM cars "
        list_cars = []
        list_cars = self.db.fetchall(show_cars)

        # Se regresa una matriz de vehículos [m][n] donde
            # m = vehículos registrados
            # n = ([0]=id, [1]=car_plate, [2]=client_ID, [3]=brand, [4]=model, [5]=date_enter, [6]=time_enter)
        return list_cars
    

    # Ultimo ID ingresado
    def getLastId(self):
        command = "SELECT MAX(id) FROM cars"
        result = self.db.fetchall(command)[0]

        if result[0] is not None:
            return result[0]
        else:
            return 0
        
    
    # Verificar si existen las placas ingresadas
    def verify_plates(self, car_plate):
        plate_exists = False

        try:
            data = self.showListCars()
            for car in data:
                if car[0] == car_plate:
                    plate_exists = True
                    return True
        except:
            print("Error")
            pass

        if not plate_exists:
            return False        
        