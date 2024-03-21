import tkinter as tk
from tkinter import END, messagebox, ttk
from func.parts import Parts


class AppParts(tk.Tk):
    # Constructor y ventana de piezas 
    def __init__(self, username, profile):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.part = Parts()

        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App parts")

        # Casilla buscar pieza
        tk.Label(self,text="Enter Part ID:").place(x=110, y=10)
        self.txSearchPart=tk.Entry(self, width=20)
        self.txSearchPart.place(x=200, y=10)
        
        # Texto ID 
        tk.Label(self,text="ID:").place(x=50,y=50)
        self.txKeyId=tk.Label(self)
        self.txKeyId.place(x=140,y=50)
        
        # Casilla descripción 
        tk.Label(self,text="Description:").place(x=50,y=100)
        self.txPartDescription=tk.Entry(self)
        self.txPartDescription.place(x=140,y=100, width= 300, height=50)
        self.txPartDescription.config(state="disabled")
        
        # Casilla stock
        tk.Label(self,text="Stock:").place(x=50,y=175)
        self.txPartStock=tk.Entry(self, width=casilla_width)
        self.txPartStock.place(x=140,y=175)
        self.txPartStock.config(state="disabled")


        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0)
        
        # Boton Buscar
        self.btnSearchPart=tk.Button(self,text="Search", 
                                     command=self.searchPart)
        self.btnSearchPart.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNewPart=tk.Button(self,text="New", 
                                  width=8, 
                                  command=self.newPart)
        self.btnNewPart.config(state="normal")
        self.btnNewPart.place(x=70,y=220)

        # Guardar
        self.btnSavePart=tk.Button(self,text="Create", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("save"))
        self.btnSavePart.config(state="disabled")
        self.btnSavePart.place(x=150,y=220)

        # Cancelar
        self.btnCancelPart=tk.Button(self,text="Cancel", 
                                     width=8, 
                                     command=self.cancelPart)
        self.btnCancelPart.config(state="disabled")
        self.btnCancelPart.place(x=230,y=220)

        # Editar
        self.btnEditPart=tk.Button(self,text="Edit", 
                                   width=8, 
                                   command=self.editPart)
        self.btnEditPart.config(state="disabled")
        self.btnEditPart.place(x=310,y=220)
        
        
        if self.profile == "Admin":
            # Eliminar
            self.btnDeletePart=tk.Button(self,text="Delete", 
                                        width=8, 
                                        command=self.deletePart)
            self.btnDeletePart.config(state="disabled")
            self.btnDeletePart.place(x=390,y=220)



    def exit(self):
        print("Exit")
        import app.app_home
        app.app_home.Home(self.username)
        self.destroy()


    def searchPart(self):
        print(f"Search part: <ID: {self.txSearchPart.get()}>")

        part = self.txSearchPart.get()
        result = self.part.lookForPartId(part)
        if result:
            # [0]=id, [1]=description, [2]=stock
            self.cleanPart()
            self.actPart()

            self.txKeyId.config(text=result[0])
            self.txPartDescription.insert(0, result[1])
            self.txPartStock.insert(0, result[2])

            self.deactPart()

            self.btnEditPart.config(state="normal")
            if self.profile == "Admin":
                self.btnDeletePart.config(state="normal")

        else:
            messagebox.showwarning("Error", "Part id doesn't exist")
    

    def newPart(self):
        print("New part")

        self.cleanPart()
        self.txSearchPart.delete(0, END)
        self.actPart()

        self.txKeyId.config(text=f"{self.part.getLastId()+1}")

        self.btnSearchPart.config(state="disabled")
        self.txSearchPart.config(state="disabled")
        self.btnNewPart.config(state="disabled")
        self.btnSavePart.config(state="normal")
        self.btnCancelPart.config(state="normal")
        self.btnEditPart.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeletePart.config(state="disabled")
    

    def savePart(self):
        print("Save part")

        # Validación si existe ya la descripción para sumar el stock
        all_parts = self.part.showListParts()
        description = self.txPartDescription.get().lower()

        if self.is_valid_stock(self.txPartStock.get()):
            if self.btnSavePart.cget("text") == "Create":
                for part in all_parts:
                    if description == part[1].lower():
                        add_stock = int(part[2]) + int(self.txPartStock.get())
                        self.part.editPart(part[0], part[1], add_stock)
                        messagebox.showinfo("Updated", f"Stock in part: {part[0]} has been updated")
                        self.cancelPart()
                        return 0
                self.part.newPart(
                    self.txPartDescription.get(),
                    self.txPartStock.get()
                )
                messagebox.showinfo("Created", "Part has been created")
                self.cancelPart()

            elif self.btnSavePart.cget("text") == "Save":
                edited = self.part.editPart(
                    self.txKeyId.cget("text"),
                    self.txPartDescription.get(),
                    self.txPartStock.get()
                )
                self.btnSavePart.config(text="Create")
                part = self.txKeyId.cget("text")
                messagebox.showinfo("Edited", f"Part: {part} has been edited")
                self.cancelPart()


    def cancelPart(self):
        print("Cancel part")
        
        self.cleanPart()
        self.btnCancelPart.config(state="disabled")
        self.btnSavePart.config(state="disabled")
        self.btnEditPart.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeletePart.config(state="disabled")
        self.btnNewPart.config(state="normal")
        self.txSearchPart.config(state="normal")
        self.btnSearchPart.config(state="normal")
        self.btnSavePart.config(text="Create")
    

    def editPart(self):
        print("Edit part")
        
        self.actPart()
        self.btnCancelPart.config(state="normal")
        self.btnEditPart.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeletePart.config(state="normal")
        self.btnSavePart.config(state="normal")
        self.btnSavePart.config(text="Save")
    

    def deletePart(self):
        yesno = messagebox.askyesno("Warning","You want to delete this part?")
        if yesno:
            print("Delete part")
            part = self.txKeyId.cget("text")
            self.part.deletePart(part)
            messagebox.showinfo("Deleted", f"The part {part} has been deleted")
            self.cancelPart()


    def cleanPart(self):
        self.actPart()
        self.txSearchPart.delete(0, END)
        self.txKeyId.config(text="")
        self.txPartDescription.delete(0, END)
        self.txPartStock.delete(0, END)
        self.deactPart()

    def actPart(self):
        self.txPartDescription.config(state="normal")
        self.txPartStock.config(state="normal")

    def deactPart(self):
        self.txPartDescription.config(state="disabled")
        self.txPartStock.config(state="disabled")


    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")
            
        if funct == "save":
            if not self.txPartDescription.get() or not self.txPartStock.get():
                warnings()
            elif int(self.txPartStock.get()) < 0:
                print(f"Error, unable to save negative numbers")
                messagebox.showwarning("Error", "Unable to save negative numbers")
            else:
                self.savePart()

    def is_valid_stock(self, stock):
        try:
            stock_int = int(stock)
            if stock_int >= 0:
                return True
            else:
                messagebox.showwarning("Error", "Stock must be a positive integer")
                return False
        except ValueError:
            messagebox.showwarning("Error", "Stock must be an integer")
            return False