import tkinter as tk
from tkinter import END, messagebox, ttk
from func.users import Users


class AppUsers(tk.Tk):
    # Constructor y ventana de usuarios
    def __init__(self, username, profile):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Mechanic Workshop")
        self.geometry(f"{self.width}x{self.height}")
        self.user = Users()

        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App users")
        
        # Casilla buscar usuario
        tk.Label(self,text="Enter User ID:").place(x=110, y=10)
        self.txSearchUser=tk.Entry(self, width=20)
        self.txSearchUser.place(x=200, y=10)
        
        # Texto key 
        tk.Label(self,text="Key:").place(x=50,y=50)
        self.txKeyUser=tk.Label(self)
        self.txKeyUser.place(x=140,y=50)
        
        # Casilla nombre 
        tk.Label(self,text="Name:").place(x=300,y=35)
        self.txNameUser=tk.Entry(self, width=casilla_width)
        self.txNameUser.place(x=300,y=55)
        self.txNameUser.config(state="disabled")
        
        # Casilla username
        tk.Label(self,text="Username:").place(x=50,y=100)
        self.txUsername=tk.Entry(self, width=casilla_width)
        self.txUsername.place(x=140,y=100)
        self.txUsername.config(state="disabled")

        # Casilla password
        tk.Label(self,text="Password:").place(x=50,y=150)
        self.txPassword=tk.Entry(self, width=casilla_width, show='*')
        self.txPassword.place(x=140,y=150)
        self.txPassword.config(state="disabled")

        profiles_values = ["Secretary", "Mechanic"]
        if self.profile == "Admin":
            profiles_values.append("Admin")

        # Casilla perfil
        tk.Label(self,text="Profile:").place(x=300,y=85)
        self.cbProfileUser=ttk.Combobox(self, width=casilla_width-3, values=profiles_values)
        self.cbProfileUser.place(x=300,y=105)
        self.cbProfileUser.config(state="disabled")



        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.place(x=0,y=0)
        
        # Boton Buscar
        self.btnSearchUser=tk.Button(self,text="Search", 
                                     command=self.searchUser)
        self.btnSearchUser.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNewUser=tk.Button(self,text="New", 
                                  width=8, 
                                  command=self.newUser)
        self.btnNewUser.config(state="normal")
        self.btnNewUser.place(x=70,y=220)

        # Guardar
        self.btnSaveUser=tk.Button(self,text="Create", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("save"))
        self.btnSaveUser.config(state="disabled")
        self.btnSaveUser.place(x=150,y=220)

        # Cancelar
        self.btnCancelUser=tk.Button(self,text="Cancel", 
                                     width=8, 
                                     command=self.cancelUser)
        self.btnCancelUser.config(state="disabled")
        self.btnCancelUser.place(x=230,y=220)

        # Editar
        self.btnEditUser=tk.Button(self,text="Edit", 
                                   width=8, 
                                   command=self.editUser)
        self.btnEditUser.config(state="disabled")
        self.btnEditUser.place(x=310,y=220)
        
        
        if self.profile == "Admin":
            # Eliminar
            self.btnDeleteUser=tk.Button(self,text="Delete", 
                                        width=8, 
                                        command=self.deleteUser)
            self.btnDeleteUser.config(state="disabled")
            self.btnDeleteUser.place(x=390,y=220)



    def exit(self):
        print("Exit")
        import app.app_home
        app.app_home.Home(self.username)
        self.destroy()

    def searchUser(self):
        id = self.txSearchUser.get()
        result = self.user.lookForUserId(id)

        print(f"Search user: <ID: {id}>")
        if result:
            #[0]=id, [1]=nombre, [2]=usuario, [3]=contraseña, [4]=perfil
            self.cleanUser()
            self.actUser()

            self.txKeyUser.config(text=result[0])
            self.txNameUser.insert(0, result[1])
            self.txUsername.insert(0, result[2])
            self.txPassword.insert(0, result[3])
            self.cbProfileUser.config(state="normal")
            self.cbProfileUser.insert(0, result[4])
            self.cbProfileUser.config(state="readonly")

            self.deactUser()

            self.btnEditUser.config(state="normal")
            if self.profile == "Admin":
                self.btnDeleteUser.config(state="normal")

        else:
            messagebox.showwarning("Error", "User ID doesn't exist")


    def newUser(self):
        print("New user")

        self.cleanUser()
        self.txSearchUser.delete(0, END)
        self.actUser()

        self.txKeyUser.config(text= self.user.getLastId()+1)

        self.btnSearchUser.config(state="disabled")
        self.txSearchUser.config(state="disabled")
        self.btnNewUser.config(state="disabled")
        self.btnSaveUser.config(state="normal")
        self.btnCancelUser.config(state="normal")
        self.btnEditUser.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteUser.config(state="disabled")

    def saveUser(self):
        print("Save user")
        
        if self.btnSaveUser.cget("text") == "Create":
            self.user.newUser(
                self.txNameUser.get(),
                self.txUsername.get(),
                self.txPassword.get(),
                self.cbProfileUser.get()
            )
            messagebox.showinfo("Created",f"User has been created")
            self.cancelUser()
        elif self.btnSaveUser.cget("text") == "Save":
            try:
                edited = self.user.editUser(
                    self.txKeyUser.cget("text"),
                    self.txNameUser.get(),
                    self.txUsername.get(),
                    self.txPassword.get(),
                    self.cbProfileUser.get()
                )
                self.btnSaveUser.config(text="Create")
                messagebox.showinfo("Edited",f"User ID: {edited[0]} has been edited")
                self.deactUser()
            except:
                pass

    def cancelUser(self):
        print("Cancel user")
        
        self.cleanUser()
        self.btnCancelUser.config(state="disabled")
        self.btnSaveUser.config(state="disabled")
        self.btnEditUser.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteUser.config(state="disabled")
        self.btnNewUser.config(state="normal")
        self.txSearchUser.config(state="normal")
        self.btnSearchUser.config(state="normal")
        self.btnSaveUser.config(text="Create")

    def editUser(self):
        print("Edit user")
        
        self.actUser()
        if self.username != self.txUsername.get():
            self.txPassword.config(state="disabled")
        self.btnCancelUser.config(state="normal")
        self.btnEditUser.config(state="disabled")
        if self.profile == "Admin":
            self.btnDeleteUser.config(state="normal")
        self.btnSaveUser.config(state="normal")
        self.btnSaveUser.config(text="Save")

    def deleteUser(self):        
        yesno = messagebox.askyesno("Warning","You want to discharge this user?")
        if yesno:
            print("Delete user")
            self.user.unableUser(self.txKeyUser.cget("text"))
            user = self.txKeyUser.cget("text")
            messagebox.showinfo("Discharged", f"The user {user} has been discharged")
            self.cancelUser()


    
    def cleanUser(self):        
        self.actUser()
        self.txKeyUser.config(text="")
        self.txNameUser.delete(0, END)
        self.txUsername.delete(0, END)
        self.txPassword.delete(0, END)
        self.cbProfileUser.set('')
        self.deactUser()
    
    def actUser(self):        
        self.txNameUser.config(state="normal")
        self.txUsername.config(state="normal")
        self.txPassword.config(state="normal")
        self.cbProfileUser.config(state="readonly")

    def deactUser(self):        
        self.txNameUser.config(state="disabled")
        self.txUsername.config(state="disabled")
        self.txPassword.config(state="disabled")
        self.cbProfileUser.config(state="disabled")

        
    # Ventana de errores
    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")

        if funct == "save":
            if not self.txNameUser.get() or not self.txPassword.get() or not self.txUsername.get() or not self.cbProfileUser.get():
                warnings()
            else:
                self.saveUser()


if __name__ == "__main__":
    user = AppUsers(username="andre_Slr", profile="Admin")
    user.mainloop()