from data.db_manager import DB
from func.users import Users
from tkinter import messagebox

# Clase para el inicio de sesión
class Login():
    # Instancias para la verificación y el usuario
    def __init__(self):
        self.user = Users()

    # Darse de alta en el sistema
    def signup(self, username):
        if self.user.verify_username(username):
            # Si existe el usuario, cancela la operación
            self.warnings("User already exists, maybe login?")
        else:
            return True
        

    # Ingresar al sistema
    def login(self, username, password):
        if self.user.verify_username(username):
            if self.user.verify_password(username, password):
                return True
            else:
                self.warnings("Incorrect password")
        else:
            self.warnings("User doesn't exist")
        
    
    # Una vez registrado, se piden llenar los datos del usuario
    def fill_info(self, username, password, name, profile):
        self.user.newUser(name, username, password, profile)

    
    # Validar que la contraseña tenga ciertos requerimientos
    def good_password(self, password=""):
        
        if len(password) < 5:
            self.warnings("Password must be > 5 characters")
        else:
            return True
    
    # Errores
    def warnings(self, text=""):
        messagebox.showwarning("Error", text)