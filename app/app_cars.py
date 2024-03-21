import tkinter as tk
from tkinter import END, messagebox, ttk
from func.customers import Customers
from func.users import Users
from func.cars import Cars


class AppCars(tk.Tk):
    # Constructor y ventana de vehículos
    def __init__(self, username, profile):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.customer = Customers()
        self.user = Users()
        self.car = Cars()

        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App cars")
        self.actual_user = self.user.lookForUserUsername(username)
     
        # Casilla buscar matrícula
        tk.Label(self, text="Enter Car Plate:").place(x=105, y=10)
        self.txSearchPlate=tk.Entry(self, width=20)
        self.txSearchPlate.place(x=200, y=10)

        # Casilla matrícula
        tk.Label(self,text="Car Plate:").place(x=50,y=50)
        self.txCarPlate=tk.Entry(self)
        self.txCarPlate.place(x=140,y=50)
        self.txCarPlate.config(state="disabled")

        # Casilla auto ID
        tk.Label(self, text="ID:").place(x=355, y=50)
        self.txCarID = tk.Label(self, text="")
        self.txCarID.place(x=410, y=50)

        # Lista nombres clientes
        client_list = []
        for client in self.customer.showListClients():
            client_list.append(client[2]+" "+client[1])
        client_list.sort()

        # Combobox nombres clientes
        tk.Label(self,text="Client Name:").place(x=50, y=100)
        self.cbClientNames = ttk.Combobox(self, state="disabled", width=casilla_width+9, values=client_list)
        self.cbClientNames.place(x=140,y=100)
        self.cbClientNames.bind("<<ComboboxSelected>>", self.select_client)

        # Casilla cliente ID
        tk.Label(self,text="Client ID:").place(x=355, y=100)
        self.txClientID = tk.Label(self, text="")
        self.txClientID.place(x=410, y=100)

        # Casilla Marca
        tk.Label(self,text="Brand:").place(x=50, y=150)
        self.txCarBrand = tk.Entry(self, width=casilla_width)
        self.txCarBrand.place(x=140, y=150)
        self.txCarBrand.config(state="disabled")

        # Casilla Modelo
        tk.Label(self,text="Model:").place(x=300, y=135)
        self.txCarModel = tk.Entry(self, width=casilla_width)
        self.txCarModel.place(x=300, y=155)
        self.txCarModel.config(state="disabled")
    
        
        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0)
        
        # Boton Buscar
        self.btnSearchCar=tk.Button(self,text="Search", 
                                     command=self.searchCar)
        self.btnSearchCar.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNewCar=tk.Button(self,text="New", 
                                  width=8, 
                                  command=self.newCar)
        self.btnNewCar.config(state="normal")
        self.btnNewCar.place(x=70,y=220)

        # Guardar
        self.btnSaveCar=tk.Button(self,text="Create", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("save"))
        self.btnSaveCar.config(state="disabled")
        self.btnSaveCar.place(x=150,y=220)

        # Cancelar
        self.btnCancelCar=tk.Button(self,text="Cancel", 
                                     width=8, 
                                     command=self.cancelCar)
        self.btnCancelCar.config(state="disabled")
        self.btnCancelCar.place(x=230,y=220)

        # Editar
        self.btnEditCar=tk.Button(self,text="Edit", 
                                   width=8, 
                                   command=self.editCar)
        self.btnEditCar.config(state="disabled")
        self.btnEditCar.place(x=310,y=220)
        
        if self.profile == "Admin":
            # Eliminar
            self.btnDeleteCar=tk.Button(self,text="Delete", 
                                        width=8, 
                                        command=self.deleteCar)
            self.btnDeleteCar.config(state="disabled")
            self.btnDeleteCar.place(x=390,y=220)





    def exit(self):
        print("Exit")
        import app.app_home
        app.app_home.Home(self.username)
        self.destroy()
    
    def searchCar(self):
        print(f"Search car: <Plate: {self.txSearchPlate.get()}>")

        plate = self.txSearchPlate.get()
        result = self.car.lookForCarPlate(plate)
        if result:
            # [0]=car_plate, [1]=client_ID, [2]=brand, [3]=model, [4]=id
            self.cleanCar()
            self.actCar()

            self.txCarPlate.insert(0, result[0])
            self.txCarID.config(text=result[4])
            self.txClientID.config(text=result[1])
            client_name = self.customer.lookForClientId(result[1])[1]
            self.cbClientNames.config(state="normal")
            self.cbClientNames.insert(0, client_name)
            self.cbClientNames.config(state="readonly")
            self.txCarBrand.insert(0, result[2])
            self.txCarModel.insert(0, result[3])

            self.deactCar()

            self.btnEditCar.config(state="normal")
            if self.profile == "Admin":
                self.btnDeleteCar.config(state="normal")
        
        else:
            messagebox.showwarning("Error", "Car plate doesn't exist")


    def newCar(self):
        print("New car")

        self.cleanCar()
        self.txSearchPlate.delete(0, END)
        self.actCar()

        self.txCarID.config(text=f"{self.car.getLastId()+1}")

        self.btnSearchCar.config(state="disabled")
        self.txSearchPlate.config(state="disabled")
        self.btnNewCar.config(state="disabled")
        self.btnSaveCar.config(state="normal")
        self.btnCancelCar.config(state="normal")
        self.btnEditCar.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteCar.config(state="disabled")


    def saveCar(self):
        print("Save car")


        if self.btnSaveCar.cget("text") == "Create":
            self.car.newCar(
                self.txCarPlate.get(), 
                self.txClientID.cget("text"),
                self.txCarBrand.get(),
                self.txCarModel.get()
            )
            messagebox.showinfo("Created", "Car has been created")
            self.cancelCar()
        elif self.btnSaveCar.cget("text") == "Save":
            edited = self.car.editCar(
                self.txCarPlate.get(),
                self.txClientID.cget("text"),
                self.txCarBrand.get(),
                self.txCarModel.get(), 
                self.txCarID.cget("text")
            )
            self.btnSaveCar.config(text="Create")
            messagebox.showinfo("Edited", f"Car: {self.txCarPlate.get()} has been edited")
            self.deactCar()


    def cancelCar(self):
        print("Cancel car")

        self.cleanCar()
        self.btnCancelCar.config(state="disabled")
        self.btnSaveCar.config(state="disabled")
        self.btnEditCar.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteCar.config(state="disabled")
        self.btnNewCar.config(state="normal")
        self.txSearchPlate.config(state="normal")
        self.btnSearchCar.config(state="normal")
        self.btnSaveCar.config(text="Create")


    def editCar(self):
        print("Edit car")
        
        self.actCar()
        self.btnCancelCar.config(state="normal")
        self.btnEditCar.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteCar.config(state="normal")
        self.btnSaveCar.config(state="normal")
        self.btnSaveCar.config(text="Save")


    def deleteCar(self):  
        yesno = messagebox.askyesno("Warning","You want to delete this car?")
        if yesno:
            print("Delete car")
            car = self.txCarPlate.get()
            self.car.deleteCar(car)
            messagebox.showinfo("Deleted", f"The car {car} has been deleted")
            self.cancelCar()



    def cleanCar(self):
        self.actCar()
        self.txCarPlate.delete(0, END)
        self.txCarID.config(text="")
        self.cbClientNames.delete(0, END)
        self.txCarBrand.delete(0, END)
        self.txClientID.config(text="")
        self.txCarModel.delete(0, END)
        self.deactCar()

    def actCar(self):
        self.txCarPlate.config(state="normal")
        self.cbClientNames.config(state="normal")
        self.txCarBrand.config(state="normal")
        self.txCarModel.config(state="normal")

    def deactCar(self):
        self.txCarPlate.config(state="disabled")
        self.cbClientNames.config(state="disabled")
        self.txCarBrand.config(state="disabled")
        self.txCarModel.config(state="disabled")

        
    # Ventana de errores
    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")
            
        if funct == "save":
            if not self.txCarPlate.get() or not self.txClientID.cget("text") or not self.txCarBrand.get() or not self.txCarModel.get():
                warnings()
            else:
                self.saveCar()

    def select_client(self, event):
        selected_name = self.cbClientNames.get()
        for client in self.customer.showListClients():
            if (client[2]+" "+client[1]) == selected_name:
                self.select_client = client
                self.txClientID.config(text=str(client[0]))
                break
