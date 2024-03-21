import tkinter as tk
from tkinter import END, messagebox, ttk
from func.login import Login
from app.app_home import Home
from func.users import Users

class AppLogin(tk.Tk):
    # Constructor y ventana de inicio
    def __init__(self):
        super().__init__()
        self.width = 550
        self.height = 300
        self.title("Welcome")
        self.geometry(f"{self.width}x{self.height}")
        self.login = Login()
        self.user = Users()

        self.username_label = None
        self.password_entry = None
        self.name_entry = None
        self.profile_cb = None

        print("App log in")

        tk.Label(
            self, 
            text = "Welcome!",
            pady=20
        ).pack()

        # Botón Sign Up
        signup_button = tk.Button(self, text="First Time (Sign up)", padx=10, pady=10, width=15, command=self.signup_w)
        signup_button.pack()

        # Botón Log In
        login_button = tk.Button(self, text="Old User (Log in)", padx=10, pady=10, width=15, command=self.login_w)
        login_button.pack()

        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.pack()

    # Ventana Log In 
    def login_w(self):
        self.login_window = tk.Toplevel(self)
        self.login_window.title("Log In")
        self.login_window.geometry(f"{self.width}x{self.height}")

        width_login = 30
        print("Log in")
        
        tk.Label(
            self.login_window, 
            text = "Enter your account",
        ).pack()
        
        tk.Label(
            self.login_window, 
            text = "Username:",
        ).pack()
        self.username_label = tk.Entry(self.login_window, width=width_login)
        self.username_label.pack()
        
        tk.Label(
            self.login_window, 
            text = "Password:",
        ).pack()
        self.password_entry = tk.Entry(self.login_window, width=width_login, show='*')
        self.password_entry.pack()
        
        tk.Button(
            self.login_window,
            text    = "Submit",
            command = lambda: self.handle_error_window("login")
        ).pack()
        
        tk.Button(
            self.login_window,
            text    = "Go Back",
            command = self.login_window.destroy
        ).pack()

    
    # Ventana Sign Up
    def signup_w(self):
        self.sign_window = tk.Toplevel(self)
        self.sign_window.title("Sign Up")
        self.sign_window.geometry(f"{self.width}x{self.height}")

        width_login = 30

        print("Sign up")

        tk.Label(
            self.sign_window, 
            text = "Create an account",
        ).pack()
        
        tk.Label(
            self.sign_window, 
            text = "Username:",
        ).pack()
        self.username_label = tk.Entry(self.sign_window, width=width_login)
        self.username_label.pack()
        
        tk.Label(
            self.sign_window, 
            text = "Password:",
        ).pack()
        self.password_entry = tk.Entry(self.sign_window, width=width_login, show='*')
        self.password_entry.pack()

        self.signup_btn = tk.Button(
            self.sign_window,
            text    = "Sign Up",
            command =lambda: self.handle_error_window("signup")
        ).pack()
        
        self.goback_btn = tk.Button(
            self.sign_window,
            text    = "Go Back",
            command = self.sign_window.destroy
        ).pack()


    # Función para llenar los datos del usuario y registrarlo
    def fill_data(self, username, password):
        self.fill_window = tk.Toplevel(self)
        self.fill_window.title("New User")
        self.fill_window.geometry(f"{self.width}x{self.height}")

        width_login = 30

        print("Fill data")

        tk.Label(
            self.fill_window, 
            text = "Upload User",
        ).pack()
        
        tk.Label(
            self.fill_window, 
            text = "Username:",
        ).pack()
        self.username_label = tk.Label(self.fill_window, text=username)
        self.username_label.pack()
        
        tk.Label(
            self.fill_window, 
            text = "Password:",
        ).pack()
        self.password_entry = tk.Entry(self.fill_window, width=width_login, show='*')
        self.password_entry.pack()
        self.password_entry.insert(0, password)
        
        tk.Label(
            self.fill_window, 
            text = "Name:",
        ).pack()
        self.name_entry = tk.Entry(self.fill_window, width=width_login)
        self.name_entry.pack()

        profiles_values = ["Secretary", "Mechanic"]
        if self.user.getLastId() == 0:
            profiles_values.append("Admin")

        tk.Label(
            self.fill_window, 
            text = "Profile:",
        ).pack()
        self.profile_cb = ttk.Combobox(self.fill_window, 
                                       state="readonly", 
                                       width=width_login-3, 
                                       values=profiles_values)
        self.profile_cb.pack()

        tk.Button(
            self.fill_window,
            text    = "Sign Up",
            command = lambda: self.handle_error_window("fill")
        ).pack()
        
        tk.Button(
            self.fill_window,
            text    = "Go Back",
            command = self.fill_window.destroy
        ).pack()


    def exit(self):
        print("Exit")
        self.destroy()


    # Función para pasar parámetros a función Login
    def logged(self):
        print("Logged")
        
        if self.username_label is not None and self.password_entry is not None:
            username = self.username_label.get()
            password = self.password_entry.get()

            if self.login.login(username, password):
                self.login_window.destroy()
                self.destroy()
                self.home = Home(username)
            
                return True, username
        return False, None
    

    # Función para pasar parámetros a función Signup
    def signed(self):
        print("Signed")

        if self.username_label is not None and self.password_entry is not None:
            username = self.username_label.get()
            password = self.password_entry.get()

            if self.login.signup(username):
                self.sign_window.destroy()
                self.fill_data(username, password)

                return True, username
        return False, None

    
    # Función para pasar parámetros a función Create User
    def created(self, name, username, password, profile):
        print("Created")

        if self.login.good_password(password):
            self.user.newUser(name=name, 
                            username=username, 
                            password=password, 
                            profile=profile)
            
            for user in self.user.showListUsers():
                print(user)
                
            self.fill_window.destroy()
            
            messagebox.showinfo("Done", "User created, please log in")

            self.destroy()
            AppLogin()


    # Ventana de errores
    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Please fill all blanks")
        

        if funct == "signup":
            if not self.username_label.get():
                warnings()
            elif not self.password_entry.get():
                warnings()
            else:
                self.signed()
        elif funct == "login":
            if not self.username_label.get():
                warnings()
            elif not self.password_entry.get():
                warnings()
            else:
                self.logged()
        elif funct == "fill":
            if not self.password_entry.get():
                warnings()
            elif not self.name_entry.get():
                warnings()
            elif not self.profile_cb.get():
                warnings()
            else:
                self.created(self.name_entry.get(), 
                             self.username_label.cget("text"), 
                             self.password_entry.get(), 
                             self.profile_cb.get())