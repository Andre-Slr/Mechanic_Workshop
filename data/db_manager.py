# Manejo de la base de datos para el programa de taller mecánico

# python -m pip install mysql-connector-python
# python.exe -m pip install --upgrade pip
from mysql.connector import connect, Error



class DB():
    def __init__(self, host="localhost", user="root", password="", database="taller_db"):
        self.host    = host
        self.user    = user
        self.password= password
        self.database= database

        # Conexión a la base de datos "taller_db" en MySQL
        try:
            self.connection = connect(
                host    = self.host,
                user    = self.user,
                password= self.password
            )

            # Cursor para manipular funciones 
            self.cursor = self.connection.cursor()

            # Crea automáticamente la base de datos si no existiera
            create_db = f"CREATE DATABASE IF NOT EXISTS {self.database}"
            self.execute(create_db)
            
            # Vuelve a hacer la conexión ahora en la base de datos
            self.connection = connect(
                host    = self.host,
                user    = self.user,
                password= self.password,
                database= self.database
            )
            # Cursor para manipular funciones 
            self.cursor = self.connection.cursor()

            # Creación de tablas a usar
            self.create_if_not_exist()
            
        # Verificación de conexión
        except Error as e:
            print(e)


    # Función para crear las tablas necesarias si es que no se han creado
    def create_if_not_exist(self):

        # Crear tabla de usuarios, en caso de que no exista
        create_table_users = """
        CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25) NOT NULL,
                    username VARCHAR(25) NOT NULL,
                    password VARCHAR(25) NOT NULL, 
                    profile VARCHAR(25) NOT NULL
        );
        """
        
        # Crear tabla de clientes, en caso de que no exista
        create_table_clients = """
        CREATE TABLE IF NOT EXISTS clients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25) NOT NULL,
                    lastname VARCHAR(25) NOT NULL,
                    phone VARCHAR(25),
                    user_id int(11), 
                    date_enter DATE NOT NULL,
                    time_enter VARCHAR(25) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
         
        # Crear tabla de vehículos, en caso de que no exista
        create_table_cars = """
        CREATE TABLE IF NOT EXISTS cars (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    car_plate VARCHAR(25) NOT NULL,
                    client_ID int(11) NOT NULL,
                    brand VARCHAR(25) NOT NULL,
                    model VARCHAR(25) NOT NULL, 
                    date_enter DATE NOT NULL,
                    time_enter VARCHAR(25) NOT NULL,
                    FOREIGN KEY (client_ID) REFERENCES clients(id)
        );
        """

        # Crear tabla de piezas, en caso de que no exista
        create_table_parts = """
        CREATE TABLE IF NOT EXISTS parts (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    description VARCHAR(64) NOT NULL, 
                    stock int(11) NOT NULL, 
                    date_enter DATE NOT NULL,
                    time_enter VARCHAR(25) NOT NULL
        );
        """

        # Crear tabla de detalles de reparacion, en caso de que no exista
        create_table_detRepairs = """
        CREATE TABLE IF NOT EXISTS det_repairs (
                    folio_detail VARCHAR(60),
                    folio int(11) NOT NULL PRIMARY KEY,
                    part_id int(11),
                    amount int(11),
                    FOREIGN KEY (folio) REFERENCES repairs(folio),
                    FOREIGN KEY (part_id) REFERENCES parts(id)
        )
        """
        
        # Crear tabla de reparacion, en caso de que no exista
        create_table_Repairs = """
        CREATE TABLE IF NOT EXISTS repairs (
                    folio int(11) AUTO_INCREMENT PRIMARY KEY,
                    car_id int(11) NOT NULL, 
                    date_enter DATE NOT NULL,
                    time_enter VARCHAR(25) NOT NULL,
                    date_out DATE NOT NULL,
                    FOREIGN KEY (car_id) REFERENCES cars(id)
        )
        """


        self.execute(create_table_users)
        self.execute(create_table_clients)
        self.execute(create_table_cars)
        self.execute(create_table_parts)
        self.execute(create_table_Repairs)
        self.execute(create_table_detRepairs)
    
    # Manejo del "cursor.execute()" de manera más sencilla
    def execute(self, command):
        try:
            self.cursor.execute(command)
            self.connection.commit()
        except Error as e:
            print(e)

    # Manejo del "cursor.fetchall()" de manera más sencilla
    def fetchall(self, command):
        try:
            self.cursor.execute(command)
            rows = self.cursor.fetchall() 
            return rows
        except Error as e:
            print(e)