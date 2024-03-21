from data.db_manager import DB
from datetime import date, datetime

###### CADA CLIENTE VA LIGADO A UN USUARIO ######

class Customers():
    # Constructor de Customers mas una instancia a la base de datos
    def __init__(self, id=None, client_name=None, client_lastname=None, phone_number=None, id_user=None):
        self.id = id
        self.client_name = client_name
        self.client_lastname = client_lastname
        self.phone_number = phone_number
        
        # id_user son los datos del usuario que registra al cliente
        self.id_user = id_user

        self.db = DB()


    # Creación de cliente, se usará como "Guardar" en el programa
    def newClient(self, client_name, client_lastname, phone_number,  id_user):
        now_date = date.today().strftime("%Y-%m-%d")
        now_time = datetime.now().strftime("%H:%M:%S")
        insert_client = f"""
        INSERT INTO 
            clients 
                (name, lastname, phone, user_id, date_enter, time_enter) 
        VALUES 
            ('{client_name}', '{client_lastname}', '{phone_number}', {id_user}, '{now_date}', '{now_time}');
        """ 
        self.db.execute(insert_client)

    # Editar cliente
    def editClient(self, id, client_name, client_lastname, phone_number,  id_user):
        # Edita todos los atributos del usuario que tenga el id "id"
        edit_client = f"""
            UPDATE
                clients
            SET
                name = '{client_name}', 
                lastname = '{client_lastname}', 
                phone = {phone_number}, 
                user_id = {id_user}
            WHERE
                id = {id}
        """

        self.db.execute(edit_client)

        # Regresa el cliente editado
        # [0]=id, [1]=nombre, [2]=apellidos, [3]=telefono, [4]=id_usuario
        return self.lookForClientId(id)
    
    # Eliminar cliente PERMANENTEMENTE
    def deleteClient(self, id):
        self.editClient(id, '', '', 'null', 'null')
        #delete_client = f"DELETE FROM clients WHERE id = {id}"

        #self.db.execute(delete_client)

    # Busca un cliente por su id
    def lookForClientId(self, id):
        try:
            search_client = f"""
                SELECT
                    id, 
                    name,
                    lastname,
                    phone,
                    user_id
                FROM
                    clients
                WHERE
                    id = {id}
            """
            found_client = self.db.fetchall(search_client)[0]

            # Se regresa el cliente encontrado de forma
            # [0]=id, [1]=nombre, [2]=apellidos, [3]=telefono, [4]=id_usuario
            return found_client
        except:
            return False
        
    # Busca un cliente por su nombre
    def lookForClientName(self, name):
        try:
            search_client = f"""
                SELECT
                    id, 
                    name,
                    lastname,
                    phone,
                    user_id
                FROM
                    clients
                WHERE
                    name = '{name}'
            """
            found_client = self.db.fetchall(search_client)[0]

            # Se regresa el cliente encontrado de forma
            # [0]=id, [1]=nombre, [2]=apellidos, [3]=telefono, [4]=id_usuario
            return found_client
        except:
            return False
        
    # Mostrar lista de clientes
    def showListClients(self):
        show_clients = """
            SELECT
                id, 
                name,
                lastname,
                phone,
                user_id
            FROM
                clients
        """
        list_clients = []
        list_clients = self.db.fetchall(show_clients)

        # Se regresa una matriz de clientes [m][n] donde
            # m = clientes registrados
            # n = ([0]=id, [1]=nombre, [2]=apellidos, [3]=telefono, [4]=id_usuario
        return list_clients
    
    # Ultimo id ingresado
    def getLastId(self):
        command = "SELECT MAX(id) FROM clients"
        result = self.db.fetchall(command)[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0