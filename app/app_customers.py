import tkinter as tk
from tkinter import END, messagebox, ttk
from func.customers import Customers
from func.users import Users


class AppClients(tk.Tk):
    # Constructor y ventana de clientes
    def __init__(self, username, profile):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.customer = Customers()
        self.user = Users()

        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App clients")
        self.actual_user = self.user.lookForUserUsername(username)
        
        # Casilla buscar cliente
        tk.Label(self,text="Enter Client:").place(x=105, y=10)
        self.txSearchClient=tk.Entry(self, width=20)
        self.txSearchClient.place(x=200, y=10)
        
        # Text id
        tk.Label(self,text="Client ID:").place(x=50,y=50)
        self.txIdClient=tk.Label(self)
        self.txIdClient.place(x=140,y=50)
        
        # Casilla nombre 
        tk.Label(self,text="Client Name:").place(x=50,y=100)
        self.txNameClient=tk.Entry(self, width=casilla_width)
        self.txNameClient.place(x=140,y=100)
        self.txNameClient.config(state="disabled")
        
        # Casilla apellidos
        tk.Label(self,text="Last Name:").place(x=50,y=150)
        self.txLastNClient=tk.Entry(self, width=casilla_width)
        self.txLastNClient.place(x=140,y=150)
        self.txLastNClient.config(state="disabled")

        # Texto Usuario ID.
        tk.Label(self,text="User:").place(x=300,y=50)
        self.txUserID=tk.Label(self)
        self.txUserID.place(x=335,y=50)
        self.txUserName=tk.Label(self)
        self.txUserName.place(x=355,y=50)
        
        # Casilla Numero Tel.
        tk.Label(self,text="Phone Number:").place(x=300,y=85)
        self.txPhoneNumb=tk.Entry(self, width=casilla_width)
        self.txPhoneNumb.place(x=300,y=105)
        self.txPhoneNumb.config(state="disabled")


        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0)
        
        # Boton Buscar
        self.btnSearchClient=tk.Button(self,text="Search", 
                                     command=self.searchClient)
        self.btnSearchClient.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNewClient=tk.Button(self,text="New", 
                                  width=8, 
                                  command=self.newClient)
        self.btnNewClient.config(state="normal")
        self.btnNewClient.place(x=70,y=220)

        # Guardar
        self.btnSaveClient=tk.Button(self,text="Create", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("save"))
        self.btnSaveClient.config(state="disabled")
        self.btnSaveClient.place(x=150,y=220)

        # Cancelar
        self.btnCancelClient=tk.Button(self,text="Cancel", 
                                     width=8, 
                                     command=self.cancelClient)
        self.btnCancelClient.config(state="disabled")
        self.btnCancelClient.place(x=230,y=220)

        if self.profile == "Admin" or self.profile == "Secretary":
            # Editar
            self.btnEditClient=tk.Button(self,text="Edit", 
                                    width=8, 
                                    command=self.editClient)
            self.btnEditClient.config(state="disabled")
            self.btnEditClient.place(x=310,y=220)
        
        
        if self.profile == "Admin":
            ### Creo que no se utilizará en clientes
            # Eliminar
            self.btnDeleteClient=tk.Button(self,text="Delete", 
                                         width=8, 
                                         command=self.deleteClient)
            self.btnDeleteClient.config(state="disabled")
            self.btnDeleteClient.place(x=390,y=220)



    def exit(self):
        print("Exit")
        import app.app_home
        app.app_home.Home(self.username)
        self.destroy()

    def searchClient(self):
        print(f"Search client: <Name: {self.txNameClient.get()}>")

        name = self.txSearchClient.get()
        result = self.customer.lookForClientName(name)
        if result:
            # [0]=id, [1]=nombre, [2]=apellidos, [3]=telefono, [4]=id_usuario
            self.cleanClient()
            self.actClient()

            self.txIdClient.config(text= result[0])
            self.txNameClient.insert(0, result[1])
            self.txLastNClient.insert(0, result[2])
            self.txUserID.config(text=f"{result[4]}")
            self.txUserName.config(text=self.getUserName(result[4]))
            self.txPhoneNumb.insert(0, result[3])

            self.deactClient()

            if self.profile == "Admin" or self.profile == "Secretary":
                self.btnEditClient.config(state="normal")
            if self.profile == "Admin":
                self.btnDeleteClient.config(state="normal")

        else:
            messagebox.showwarning("Error", "Client name doesn't exist")


    def newClient(self):
        print("New client")

        self.cleanClient()
        self.txSearchClient.delete(0, END)
        self.actClient()

        self.txIdClient.config(text=f"{self.customer.getLastId()+1}")

        self.txUserID.config(text=f"{self.actual_user[0]}")
        self.txUserName.config(text=f"{self.actual_user[1]}")

        self.btnSearchClient.config(state="disabled")
        self.txSearchClient.config(state="disabled")
        self.btnNewClient.config(state="disabled")
        self.btnSaveClient.config(state="normal")
        self.btnCancelClient.config(state="normal")
        if self.profile == "Admin" or self.profile == "Secretary":
            self.btnEditClient.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteClient.config(state="disabled")

    def saveClient(self):
        print("Save client")
        
        if self.btnSaveClient.cget("text") == "Create":
            self.customer.newClient(
                self.txNameClient.get(),
                self.txLastNClient.get(),
                self.txPhoneNumb.get(),
                self.txUserID.cget("text")
            )
            messagebox.showinfo("Created","Client has been created")
            self.cancelClient()
        elif self.btnSaveClient.cget("text") == "Save":
            edited = self.customer.editClient(
                self.txIdClient.cget("text"),
                self.txNameClient.get(),
                self.txLastNClient.get(),
                self.txPhoneNumb.get(),
                self.txUserID.cget("text")
            )
            self.btnSaveClient.config(text="Create")
            messagebox.showinfo("Edited",f"Client: {edited[1]} {edited[2]} has been edited")
            self.deactClient()

    def cancelClient(self):
        print("Cancel client")
        
        self.cleanClient()
        self.btnCancelClient.config(state="disabled")
        self.btnSaveClient.config(state="disabled")
        if self.profile == "Admin" or self.profile == "Secretary":
            self.btnEditClient.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteClient.config(state="disabled")
        self.btnNewClient.config(state="normal")
        self.txSearchClient.config(state="normal")
        self.btnSearchClient.config(state="normal")
        self.btnSaveClient.config(text="Create")

    def editClient(self):
        print("Edit client")
        
        self.actClient()
        self.btnCancelClient.config(state="normal")
        if self.profile == "Admin" or self.profile == "Secretary":
            self.btnEditClient.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteClient.config(state="normal")
        self.btnSaveClient.config(state="normal")
        self.btnSaveClient.config(text="Save")

    def deleteClient(self):        
        yesno = messagebox.askyesno("Warning","You want to delete this user?")
        if yesno:
            print("Delete client")
            customer = self.txIdClient.cget("text")
            self.customer.deleteClient(customer)
            messagebox.showinfo("Deleted", f"The client {customer} has been deleted")
            self.cancelClient()


    
    def cleanClient(self):        
        self.actClient()
        self.txIdClient.config(text="")
        self.txNameClient.delete(0, END)
        self.txLastNClient.delete(0, END)
        self.txUserID.config(text="")
        self.txUserName.config(text="")
        self.txPhoneNumb.delete(0, END)
        self.deactClient()
    
    def actClient(self):        
        self.txNameClient.config(state="normal")
        self.txLastNClient.config(state="normal")
        self.txPhoneNumb.config(state="normal")

    def deactClient(self):        
        self.txNameClient.config(state="disabled")
        self.txLastNClient.config(state="disabled")
        self.txPhoneNumb.config(state="disabled")

        
    # Ventana de errores
    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")

        if funct == "save":
            if not self.txNameClient.get() or not self.txLastNClient.get() or not self.txPhoneNumb.get():
                warnings()
            else:
                self.saveClient()

    def getUserName(self, id):
        userName = self.user.lookForUserId(id)[1]
        return userName