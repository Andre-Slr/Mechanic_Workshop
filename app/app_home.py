import tkinter as tk
from tkinter import END, messagebox, ttk
from func.users import Users
from app.app_users import AppUsers
from app.app_customers import AppClients
from app.app_cars import AppCars
from app.app_parts import AppParts
from app.app_repairs import AppRepairs
from app.app_report import AppReport


class Home(tk.Tk):
    # Constructor y ventana de inicio
    def __init__(self, username):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.user = Users()

        self.username = username
        
        # Mensaje de bienvenida (y comprobación de que es el usuario correcto)
        self.actual_user = self.user.lookForUserUsername(username)

        print(f"App home:   <User: {self.actual_user[2]},  Name: {self.actual_user[1]},  Profile: {self.actual_user[4]}>")

        tk.Label(
            self, text=f"Welcome, {self.actual_user[1]}",
        ).pack()


        # Acceso solamente al administrador y a lxs secretarixs
        if self.actual_user[4] == "Admin" or self.actual_user[4] == "Secretary":
            # Botón Users
            self.users_button = tk.Button(self, text="Users", padx=10, pady=10, width=15, command=self.users_funct)
            self.users_button.pack()

        # Botón Costumers
        self.customers_button = tk.Button(self, text="Customers", padx=10, pady=10, width=15, command=self.customers_funct)
        self.customers_button.pack()

        # Acceso solamente al administrador y a lxs mecánicxs
        if self.actual_user[4] == "Admin" or self.actual_user[4] == "Mechanic":
            # Botón Cars
            self.cars_button = tk.Button(self, text="Cars",padx=10, pady=10, width=15, command=self.cars_funct)
            self.cars_button.pack()

        # Botón Parts
        self.parts_button = tk.Button(self, text="Parts",padx=10, pady=10, width=15, command=self.parts_funct)
        self.parts_button.pack()
        
        # Botón Repairs
        self.repairs_button = tk.Button(self, text="Repairs",padx=10, pady=10, width=15, command=self.repairs_funct)
        self.repairs_button.pack()

        # Botón Report
        self.report_button = tk.Button(self, text="Report",padx=10, pady=10, width=15, command=self.report_funct)
        self.report_button.pack()
        

        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0, width=50)

        # Boton Cambiar Usuario
        self.btnLogout=tk.Button(self,text="Log out", 
                               command=self.confirm)
        self.btnLogout.place(x=0,y=20, width=50)
        
        if self.actual_user[4] == "discharged":
            messagebox.showwarning("Warning", "User already discharged. No permission to log in.")
            self.logout()


    # Función a llamar por el botón Users
    def users_funct(self):
        self.app_user = AppUsers(self.username, self.actual_user[4])
        self.destroy()

    
    # Función a llamar por el botón Customers
    def customers_funct(self):
        self.app_client = AppClients(self.username, self.actual_user[4])
        self.destroy()

    
    # Función a llamar por el botón Cars
    def cars_funct(self):
        self.app_car = AppCars(self.username, self.actual_user[4])
        self.destroy()

        
    # Función a llamar por el botón Parts
    def parts_funct(self):
        self.app_part = AppParts(self.username, self.actual_user[4])
        self.destroy()

        
    # Función a llamar por el botón Repairs
    def repairs_funct(self):
        self.app_repair = AppRepairs(self.username, self.actual_user[4])
        self.destroy()

        
    # Función a llamar por el botón Report
    def report_funct(self):
        self.app_report = AppReport(self.username, self.actual_user[4])
        self.destroy()

    
    # Función a llamar por el botón Exit
    def exit(self):
        print("Exit")
        self.destroy()
            
    # Función a llamar por el botón Logout
    def logout(self):
        print(f"Logged out:   <User: {self.actual_user[2]},  Name: {self.actual_user[1]},  Profile: {self.actual_user[4]}>")
        import app.app_login
        app.app_login.AppLogin()
        self.destroy()

    def confirm(self):
        yesno = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if yesno:
            self.logout()


if __name__ == "__main__":
    home = Home(username="andre_slr")
    home.mainloop()