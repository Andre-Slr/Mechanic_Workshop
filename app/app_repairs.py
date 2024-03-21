import tkinter as tk
from tkinter import END, messagebox, ttk
from tkcalendar import DateEntry
import time

from func.repairs import Repairs
from func.cars import Cars
from func.parts import Parts
from app.app_report import AppReport


class AppRepairs(tk.Tk):
    # Constructor y ventana de reparaciones
    def __init__(self, username, profile):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.car = Cars()
        self.part = Parts()
        self.repair = Repairs()
        
        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App repairs")

        # Casilla buscar reparacion
        tk.Label(self, text="Enter folio:").place(x=105, y=10)
        self.txSearchRepair=tk.Entry(self, width=20)
        self.txSearchRepair.place(x=200, y=10)

        # Texto folio
        tk.Label(self,text="Folio:").place(x=50,y=50)
        self.txRepairFolio=tk.Label(self)
        self.txRepairFolio.place(x=140,y=50)

        # Botón Report
        self.report_button = tk.Button(self, text="Report", command=self.report_funct)
        self.report_button.place(x=500, y=0)


        # Lista de matrículas
        car_plates_list = []
        for car in self.car.showListCars():
            car_plates_list.append(car[0])
        car_plates_list.sort()

        # Combobox matrículas 
        # (se guarda el ID del auto)
        tk.Label(self, text="Car Plate:").place(x=50, y=75)
        self.cbCarPlates = ttk.Combobox(self, state="normal", width=casilla_width-5, values=car_plates_list)
        self.cbCarPlates.place(x=140,y=75)
        self.cbCarPlates.bind("<<ComboboxSelected>>", self.select_car)

        # Casilla auto ID
        tk.Label(self, text="Car ID:").place(x=280, y=75)
        self.txCarID = tk.Label(self, text="")
        self.txCarID.place(x=355, y=75)


        # Casilla fecha entrada
        tk.Label(self,text="Date In:").place(x=50, y=100)
        self.txDateIn=DateEntry(self, selectmode='day', date_pattern='yyyy-MM-dd', width=casilla_width-5)
        self.txDateIn.place(x=140,y=100)

        # Casilla fecha salida
        tk.Label(self,text="Date Out:").place(x=280, y=100)
        self.txDateOut=DateEntry(self, selectmode='day', date_pattern='yyyy-MM-dd', width=casilla_width-5)
        self.txDateOut.place(x=355, y=100)


        # Lista de piezas
        parts_list = []
        for part in self.part.showListParts():
            parts_list.append(part[1])
        parts_list.sort()

        # Combobox piezas
        # (se guarda el ID de la pieza)
        tk.Label(self, text="Select a Part:").place(x=50, y=125)
        self.cbParts = ttk.Combobox(self, state="normal", width=casilla_width+5, values=parts_list)
        self.cbParts.place(x=140,y=125)
        self.cbParts.bind("<<ComboboxSelected>>", self.select_part)

        # Texto ID piezas
        tk.Label(self, text="Part ID:").place(x=50, y=150)
        self.txPartID = tk.Label(self, text="")
        self.txPartID.place(x=140, y=150)


        # Casilla cantidad piezas
        tk.Label(self, text="Quantity:").place(x=280, y=150)
        self.txAmount = tk.Entry(self, width=casilla_width-2)
        self.txAmount.place(x=355, y=150)

        # Casilla falla (descripcion)
        tk.Label(self,text="Problem:").place(x=50,y=175)
        self.txRepairProblem=tk.Entry(self)
        self.txRepairProblem.place(x=140,y=175, width= 330, height=30)


        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0)
        
        # Boton Buscar
        self.btnSearchRepair=tk.Button(self,text="Search", 
                                     command=self.searchRepair)
        self.btnSearchRepair.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNewRepair=tk.Button(self,text="New", 
                                  width=8, 
                                  command=self.newRepair)
        self.btnNewRepair.config(state="normal")
        self.btnNewRepair.place(x=70,y=220)

        # Guardar
        self.btnSaveRepair=tk.Button(self,text="Create", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("save"))
        self.btnSaveRepair.config(state="disabled")
        self.btnSaveRepair.place(x=150,y=220)

        # Cancelar
        self.btnCancelRepair=tk.Button(self,text="Cancel", 
                                     width=8, 
                                     command=self.cancelRepair)
        self.btnCancelRepair.config(state="disabled")
        self.btnCancelRepair.place(x=230,y=220)

        # Editar
        self.btnEditRepair=tk.Button(self,text="Edit", 
                                   width=8, 
                                   command=self.editRepair)
        self.btnEditRepair.config(state="disabled")
        self.btnEditRepair.place(x=310,y=220)
        
        
        if self.profile == "Admin":
            # Eliminar
            self.btnDeleteRepair=tk.Button(self,text="Delete", 
                                        width=8, 
                                        command=self.deleteRepair)
            self.btnDeleteRepair.config(state="disabled")
            self.btnDeleteRepair.place(x=390,y=220)

        self.cleanRepair()
        self.deactRepair()



    def exit(self):
        print("Exit")
        import app.app_home
        app.app_home.Home(self.username)
        self.destroy()


    def searchRepair(self):
        print(f"Search repair: <Folio: {self.txSearchRepair.get()}>")

        folio = self.txSearchRepair.get()
        result = self.repair.lookForRepairFolio(folio)
        if result:
            #  [0][0]=folio, [0][1]=car_id, [0][2]=date_enter, [0][3]=time_enter, [0][4]=date_out, [0][5]=time_out, [1][0]=folio_detail, [1][1]=folio(otra vez), [1][2]=part_id, [1][3]=amount
            self.cleanRepair()
            self.actRepair()
            car_plate = self.car.lookForCarID(result[0][1])[0]
            part_description = self.part.lookForPartId(result[1][2])[1]

            self.txRepairFolio.config(text=result[0][0])
            self.cbCarPlates.set(car_plate)
            self.txCarID.config(text=result[0][1])
            self.txDateIn.insert(0, result[0][2])
            self.txDateOut.insert(0, result[0][4])
            self.cbParts.set(part_description)
            self.txPartID.config(text=result[1][2])
            self.txAmount.insert(0, result[1][3])
            self.txRepairProblem.insert(0, result[1][0])

            self.deactRepair()

            self.btnEditRepair.config(state="normal")
            if self.profile == "Admin":
                self.btnDeleteRepair.config(state="normal")
        
        else:
            messagebox.showwarning("Error", "Repair folio doesn't exist")

    

    def newRepair(self):
        print("New repair")

        self.cleanRepair()
        self.txSearchRepair.delete(0, END)
        self.actRepair()

        self.txRepairFolio.config(text=f"{self.repair.getLastId()+1}")

        self.btnSearchRepair.config(state="disabled")
        self.txSearchRepair.config(state="disabled")
        self.btnNewRepair.config(state="disabled")
        self.btnSaveRepair.config(state="normal")
        self.btnCancelRepair.config(state="normal")
        self.btnEditRepair.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteRepair.config(state="disabled")
    

    def saveRepair(self):
        print("Save repair")

        folio = self.txRepairFolio.cget("text")
        date_in = self.txDateIn.get_date()
        date_out = self.txDateOut.get_date()
        part_id = self.txPartID.cget("text")


        if self.btnSaveRepair.cget("text") == "Create":
            self.repair.newRepair(
                folio,
                self.txCarID.cget("text"),
                date_in.strftime("%Y-%m-%d"),
                date_out.strftime("%Y-%m-%d"),
                self.txRepairProblem.get(),
                part_id,
                self.txAmount.get()
            )
            taken = self.part.takePart(part_id, self.txAmount.get())
            messagebox.showinfo("Added", "Repair has been added")
            self.cancelRepair()
        elif self.btnSaveRepair.cget("text") == "Save":
            edited = self.repair.editRepair(
                folio,
                self.txCarID.cget("text"),
                date_in.strftime("%Y-%m-%d"),
                date_out.strftime("%Y-%m-%d"),
                self.txRepairProblem.get(),
                self.txPartID.cget("text"),
                self.txAmount.get()
            )
            self.btnSaveRepair.config(text="Create")
            messagebox.showinfo("Edited", f"Repair folio: {folio} has been edited")
            self.deactRepair()


    def cancelRepair(self):
        print("Cancel repair")

        self.cleanRepair()
        self.btnCancelRepair.config(state="disabled")
        self.btnSaveRepair.config(state="disabled")
        self.btnEditRepair.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteRepair.config(state="disabled")
        self.btnNewRepair.config(state="normal")
        self.txSearchRepair.config(state="normal")
        self.btnSearchRepair.config(state="normal")
        self.btnSaveRepair.config(text="Create")


    def editRepair(self):
        print("Edit car")
        
        self.actRepair()
        self.btnCancelRepair.config(state="normal")
        self.btnEditRepair.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteRepair.config(state="normal")
        self.btnSaveRepair.config(state="normal")
        self.btnSaveRepair.config(text="Save")
    

    def deleteRepair(self):
        yesno = messagebox.askyesno("Warning","You want to delete this repair folio?")
        if yesno:
            print("Delete repair")
            folio = self.txRepairFolio.cget("text")
            self.repair.deleteRepair(folio)
            messagebox.showinfo("Deleted", f"The folio {folio} has been deleted")
            self.cancelRepair()


    def cleanRepair(self):
        self.actRepair()
        self.txRepairFolio.config(text="")
        self.cbCarPlates.set('')
        self.txCarID.config(text="")
        self.txDateIn.delete(0, END)
        self.txDateOut.delete(0, END)
        self.cbParts.set('')
        self.txPartID.config(text="")
        self.txAmount.delete(0, END)
        self.txRepairProblem.delete(0, END)
        self.deactRepair()

    def actRepair(self):
        self.cbCarPlates.config(state="normal")
        self.txDateIn.config(state="normal")
        self.txDateOut.config(state="normal")
        self.cbParts.config(state="normal")
        self.txAmount.config(state="normal")
        self.txRepairProblem.config(state="normal")

    def deactRepair(self):
        self.cbCarPlates.config(state="disabled")
        self.txDateIn.config(state="disabled")
        self.txDateOut.config(state="disabled")
        self.cbParts.config(state="disabled")
        self.txAmount.config(state="disabled")
        self.txRepairProblem.config(state="disabled")


    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")
            
        print("Cheking errors")

        if funct == "save":
            # Si no están llenos los campos obligatorios
            if not self.cbCarPlates.get() or not self.txDateIn.get_date() or not self.txDateOut.get_date() or not self.cbParts.get() or not self.txAmount.get() or not self.txRepairProblem.get():
                print("Error 1")
                warnings()

            # Si se quieren usar cantidades negativas
            elif int(self.txAmount.get()) < 0:
                print("Error 2")
                print(f"Error, unable to save negative numbers")
                messagebox.showwarning("Error", "Unable to save negative numbers")

            # Si la fecha no es coherente
            elif self.txDateOut.get_date() < self.txDateIn.get_date():
                print("Error 3")
                messagebox.showwarning("Error", "Date out can't be before the date in.")

            else:
                part_id = self.txPartID.cget("text")
                part_description = self.part.lookForPartId(part_id)[1]
                if not self.part.verifyStock(part_id, self.txAmount.get()):
                    messagebox.showwarning("Error", f"Insufficient stock of {part_description} available")
                else:
                    print("No errors")
                    self.saveRepair()


    def select_car(self, event):
        selected_plate = self.cbCarPlates.get()
        for car in self.car.showListCarsFull():
            if (car[1]) == selected_plate:
                self.select_car = car
                self.txCarID.config(text=str(car[0]))
                break
            
    def select_part(self, event):
        selected_part = self.cbParts.get()
        for part in self.part.showListParts():
            if (part[1]) == selected_part:
                self.select_part = part
                self.txPartID.config(text=str(part[0]))
                break
            
    # Función a llamar por el botón Report
    def report_funct(self):
        self.app_report = AppReport(self.username, self.profile)
        self.destroy()