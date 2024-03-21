from data.db_manager import DB
from datetime import date, datetime

# Clase Piezas
# Las piezas se descontarán en el archivo de piezas en cada reparacion

class Parts():
    # Constructor
    def __init__(self, id=None, description=None, stock=None):
        self.id = id
        self.description = description
        self.stock = stock

        self.db = DB()

    # Nueva pieza (guardar, en la interface)
    def newPart(self, description, stock):
        now_date = date.today().strftime("%Y-%m-%d")
        now_time = datetime.now().strftime("%H:%M:%S")
        insert_part = f"""
        INSERT INTO
            parts
                (description, stock, date_enter, time_enter)
        VALUES
            ('{description}', {stock}, '{now_date}', '{now_time}')
        """
        self.db.execute(insert_part)


    # Editar pieza
    def editPart(self, id, description, stock):
        # Edita los atributos de la pieza con el id "id"
        edit_part = f"""
            UPDATE
                parts
            SET
                description = '{description}',
                stock = {stock}
            WHERE
                id = {id}
        """
        self.db.execute(edit_part)

        # Se regresa el vehículo encontrado de forma
        # [0]=id, [1]=description, [2]=stock
        return self.lookForPartId(id)
        

    # Eliminar pieza
    def deletePart(self, id):
        delete_part = f"DELETE FROM parts WHERE id = {id}"

        self.db.execute(delete_part)


    # Busca una pieza por su id
    def lookForPartId(self, id):
        try:
            search_part = f"""
                SELECT *
                FROM 
                    parts
                WHERE
                    id = {id}
            """
            found_part = self.db.fetchall(search_part)[0]

            # Se regresa el vehículo encontrado de forma
            # [0]=id, [1]=description, [2]=stock
            return found_part
        except:
            return False
            

    # Muestra la lista de piezas registradas
    def showListParts(self):
        show_parts = "SELECT * FROM parts"
        list_parts = []
        list_parts = self.db.fetchall(show_parts)
        
        # Se regresa una matriz de piezas [m][n] donde
            # m = piezas registradas
            # n = ([0]=id, [1]=description, [2]=stock)
        return list_parts
    

    # Ultimo id ingresado
    def getLastId(self):
        command = "SELECT MAX(id) FROM parts"
        result = self.db.fetchall(command)[0]

        if result[0] is not None:
            return result[0]
        else:
            return 0


    # Verifica si se pueden tomar piezas (sin tomarlas)
    def verifyStock(self, id, amount):
        stock = self.lookForPartId(id)[2]
        description = self.lookForPartId(id)[1]
        if stock >= 0:
            if int(amount) <= stock:
                return True
            else:
                return False
        else:
            return False
        

    # Modifica la cantidad de piezas
    def takePart(self, id, amount):
        stock = self.lookForPartId(id)[2]
        description = self.lookForPartId(id)[1]
        if stock >= 0:
            if int(amount) <= stock:
                self.editPart(id, description, stock-int(amount))

                # [0]=id, [1]=description, [2]=stock
                return self.lookForPartId(id)
            else:
                return False
        else:
            return False
        


    