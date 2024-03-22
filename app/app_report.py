import tkinter as tk
from tkinter import END, messagebox, ttk
from tkinter.ttk import *
from tkcalendar import DateEntry

from func.repairs import Repairs
from func.parts import Parts


class AppReport(tk.Tk):
    # Ventana de reporte (sólo se va a ver, no habrá un archivo ni nada aún)
    def __init__(self, username, profile):
        super().__init__()
        self.width = 700
        self.height = 550
        self.title("Generate Report")
        self.geometry(f"{self.width}x{self.height}")
        self.repair = Repairs()
        self.part = Parts()

        self.username = username
        self.profile = profile
        casilla_width = 20

        print("App report")

        # Casilla fecha inicio (buscar)
        tk.Label(self,text="From:").grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 2)
        self.txFromDate=DateEntry(self, selectmode='day', date_pattern='yyyy-MM-dd', width=casilla_width-5)
        self.txFromDate.grid(row = 0, column = 2, pady = 2)

        # Casilla fecha final (buscar)
        tk.Label(self,text="To:").grid(row = 1, column = 1, sticky="W",padx = 15, pady = 2)
        self.txToDate=DateEntry(self, selectmode='day', date_pattern='yyyy-MM-dd', width=casilla_width-5)
        self.txToDate.grid(row = 1, column = 2, pady = 2)

        # Boton Buscar
        self.btnSearchRepair=tk.Button(self,text="Search", 
                                     command=self.searchReport)
        self.btnSearchRepair.grid(row = 0, column = 3, rowspan=2,padx=10)
      

        # Tabla (o grid, o como sea) de reporte
        self.report_table = tk.Frame(self)
        self.report_headers = tk.Frame(self.report_table)
        self.report_content = tk.Frame(self.report_table)
        

        
        # Boton Salir
        self.btnExit=tk.Button(self,text="Exit", 
                               command=self.exit)
        self.btnExit.grid(row = 0, column = 0, padx = 10, pady = 2)



        self.report_table.place(x=10, y=75, width=680, height=465)
        self.report_headers.grid(row=0, column=0)
        self.report_content.grid(row=0, column=0)
        


    def exit(self):
        print("Exit")
        import app.app_repairs
        app.app_repairs.AppRepairs(self.username, self.profile)
        self.destroy()

    def searchReport(self):
        print("Search report")

        from_date = self.txFromDate.get_date()
        to_date = self.txToDate.get_date()

        if from_date <= to_date:

            repairs = self.repair.getFoliosInDateRange(from_date, to_date)
            
            self.clear_table()

            tk.Label(self.report_content, text="Folio").grid(row=0, column=0, sticky="W", padx=10, pady=2)
            tk.Label(self.report_content, text="Date").grid(row=0, column=1, sticky="W", padx=30, pady=2)
            tk.Label(self.report_content, text="Detail").grid(row=0, column=2, sticky="W", padx=150, pady=2)
            tk.Label(self.report_content, text="Part").grid(row=0, column=3, sticky="W", padx=50, pady=2)
            tk.Label(self.report_content, text="Amount").grid(row=0, column=4, sticky="W", padx=5, pady=2)
            
            # Comenzar desde la segunda fila
            row = 1  

            # Muestra cada folio encontrado
            for repair in repairs:
                
                part_desc = self.part.lookForPartId(repair[1][2])[1]

                tk.Label(self.report_content, text=repair[0][0]).grid(row=row, column=0, sticky="W", padx=20, pady=10)
                tk.Label(self.report_content, text=repair[0][2]).grid(row=row, column=1, sticky="W", padx=10, pady=2)
                tk.Label(self.report_content, text=repair[1][0]).grid(row=row, column=2, sticky="W", padx=10, pady=2)
                tk.Label(self.report_content, text=part_desc).grid(row=row, column=3, sticky="W", padx=10, pady=2)
                tk.Label(self.report_content, text=repair[1][3]).grid(row=row, column=4, sticky="W", padx=30, pady=2)
                row += 1
        else:
            messagebox.showwarning("Error", "Unvalid date range")
        
    def clear_table(self):
        for widget in self.report_content.winfo_children():
            widget.destroy()