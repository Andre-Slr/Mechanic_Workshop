# main ejecutable del programa

##      TALLER MECÁNICO
## Márquez Cervantes, Luis Enrique
## Solórzano Maldonado, André

### Para correr el programa se necesita ejecutar en cmd:
###     python -m pip install mysql-connector-python
###     python.exe -m pip install --upgrade pip
###     python -m pip install tkinter
###     python -m pip install tkcalendar

### Todos los print() son para verificar la ejecución del código

from data.db_manager import DB
from app.app_login import AppLogin


import time

if __name__ == "__main__":
    start = time.time()
    print("Executing...\n")

    db = DB()
    print("connected: ", db.connection)

    login = AppLogin()
    login.mainloop()

    print("\nFinishing...")
    end = time.time()
    print(f"\nProgram working during {(end-start):.2f} seconds\n")