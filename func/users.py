from data.db_manager import DB
from tkinter import messagebox

# Clase usuarios
# Key, name, username, pw, profile (admin, secretary, mechanic)
class Users():
    # Constructor de Users mas una instancia a la base de datos
    def __init__(self, key=None, name=None, username=None, password=None, profile=None):
        self.key = key
        self.name = name
        self.username = username
        self.password = password
        self.profile = profile
        self.db = DB()
        

    # Creación de usuario, se usará como "Guardar" en el programa
    def newUser(self, name, username, password, profile):
        if not self.verify_username(username):
            insert_user = f"""
            INSERT INTO 
                users 
                    (name, username, password, profile) 
            VALUES 
                ('{name}', '{username}', '{password}', '{profile}');
            """ 
            self.db.execute(insert_user)
        else:
            messagebox.showwarning("Error","Username already exists")
    
    # Editar usuario
    def editUser(self, key, name, username, password, profile):
        # Edita todos los atributos del usuario que tenga el id "key"
        actualUser = self.lookForUserUsername(username)

        if not self.verify_username(username) or actualUser[1] == self.lookForUserId(key)[1]:
            edit_user = f"""
                UPDATE
                    users
                SET
                    name ='{name}', 
                    username = '{username}',
                    password = '{password}',
                    profile = '{profile}'
                WHERE
                    id = {key}
            """

            self.db.execute(edit_user)

            # Regresa el usuario editado 
            return self.lookForUserId(key)
        else:
            messagebox.showwarning("Error","Username already exists")
    

    # Eliminar usuario PERMANENTEMENTE
    def deleteUser(self, key):
        delete_user = f"DELETE FROM users WHERE id = {key}"

        self.db.execute(delete_user)

    # "Elimina" al usuario (lo da de baja del sistema) dejando sus datos
    def unableUser(self, key):
        unable_user = f"""
            UPDATE
                users
            SET
                profile = 'discharged'
            WHERE
                id = {key}
        """

        self.db.execute(unable_user)

    # Busca un usuario por su id
    def lookForUserId(self, key):
        try:
            search_user = f"""
                SELECT 
                    id, 
                    name, 
                    username, 
                    password, 
                    profile 
                FROM 
                    users 
                WHERE 
                    id = {key} 
            """
            found_user = self.db.fetchall(search_user)[0]

            # Se regresa el usuario encontrado de forma
            # [0]=id, [1]=nombre, [2]=usuario, [3]=contraseña, [4]=perfil
            return found_user
        except:
            return False
    
    # Busca un usuario por su usuario (para el login)
    def lookForUserUsername(self, username):
        try:
            search_user = f"""
                SELECT 
                    id, 
                    name, 
                    username, 
                    password, 
                    profile 
                FROM 
                    users 
                WHERE 
                    username = '{username}' 
            """
            found_user = self.db.fetchall(search_user)[0]

            # Se regresa el usuario encontrado de forma
            # [0]=id, [1]=nombre, [2]=usuario, [3]=contraseña, [4]=perfil
            return found_user
        except:
            return False


    # Mostrar lista de usuarios
    def showListUsers(self):
        show_user = """
            SELECT 
                id, 
                name,  
                username, 
                password, 
                profile 
            FROM 
                users
        """
        list_users = []
        list_users = self.db.fetchall(show_user)

        # Se regresa como matriz de usuarios [m][n] donde 
            # m = usuarios registrados
            # n = atributos ([0]=id, [1]=nombre, [2]=usuario, [3]=contraseña, [4]=perfil)
        return list_users
    
    # Verificar si existe el nombre de usuario
    def verify_username(self, username):
        user_exists = False
        
        try:
            data = self.showListUsers()
            for usr in data:
                if usr[2] == username:
                    user_exists = True
                    return True
        except:
            print("Error")
            pass

        if not user_exists:
            return False
        
    # Verificar si la contraseña es del usuario
    def verify_password(self, username, password):
        password_exists = False
        
        try:
            data = self.showListUsers()
            for pw in data:
                if pw[3] == password and pw[2] == username:
                    password_exists = True
                    return True
        except:
            print("Error")
            pass

        if not password_exists:
            return False
        
    
    # Último id ingresado
    def getLastId(self):
        command = "SELECT MAX(id) FROM users"
        result = self.db.fetchall(command)[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0