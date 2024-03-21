from data.db_manager import DB
from datetime import date, datetime

# Clase Reparaciones

class Repairs():
    # Constructor
    def __init__(self, folio=None, car_id=None, date_enter=None, date_out=None, folio_detail=None, part_id=None, amount=None):
        self.folio = folio
        self.car_id = car_id
        self.date_enter = date_enter
        self.date_out = date_out
        self.folio_detail = folio_detail
        self.part_id = part_id
        self.amount = amount

        self.db = DB()


    def newRepair(self, folio, car_id, date_enter, date_out, folio_detail, part_id, amount):
        now_time = datetime.now().strftime("%H:%M:%S")
        insert_folio = f"""
        INSERT INTO
            repairs
                (folio, car_id,	date_enter,	time_enter,	date_out)
        VALUES
            ({folio}, {car_id}, '{date_enter}', '{now_time}', '{date_out}');
        """
        insert_details = f"""
        INSERT INTO
            det_repairs
                (folio_detail, folio, part_id, amount)
        VALUES
            ('{folio_detail}', {folio}, {part_id}, {amount});
        """

        self.db.execute(insert_folio)
        self.db.execute(insert_details)


    def editRepair(self, folio, car_id, date_enter, date_out, folio_detail, part_id, amount):
        now_time = datetime.now().strftime("%H:%M:%S")
        edit_repair = f"""
            UPDATE
                repairs
            SET
                folio = {folio}, 
                car_id = {car_id},	
                date_enter = '{date_enter}',
                date_out = '{date_out}'
            WHERE 
                folio = {folio}
        """
        edit_details = f"""
            UPDATE
                det_repairs
            SET
                folio_detail = '{folio_detail}', 
                folio = {folio}, 
                part_id = {part_id}, 
                amount = {amount}
            WHERE 
                folio = {folio}
        """
        self.db.execute(edit_repair)
        self.db.execute(edit_details)

        return self.lookForRepairFolio(folio)


    
    def deleteRepair(self, folio):
        delete_repair = f"DELETE FROM repairs WHERE folio = {folio}"
        delete_details = f"DELETE FROM det_repairs WHERE folio = {folio}"

        self.db.execute(delete_details)
        self.db.execute(delete_repair)
    

    def lookForRepairFolio(self, folio):
        try:
            search_folio = f"""
                SELECT * FROM repairs WHERE folio = {folio}
            """
            found_folio = self.db.fetchall(search_folio)[0]
            search_detail = f"""
                SELECT * FROM det_repairs WHERE folio = {folio}
            """
            found_detail = self.db.fetchall(search_detail)[0]
            
            # Se regresa la reparación encontrada de forma
            # [0][0]=folio, [0][1]=car_id, [0][2]=date_enter, [0][3]=time_enter, [0][4]=date_out, [0][5]=time_out, [1][0]=folio_detail, [1][1]=folio(otra vez), [1][2]=part_id, [1][3]=amount
            return found_folio, found_detail
        except:
            return False


    def showListRepairs(self):
        show_repairs = "SELECT * FROM repairs"
        show_details = "SELECT * FROM det_repairs"
        list_repairs = self.db.fetchall(show_repairs)
        list_details = self.db.fetchall(show_details)
        
        
        # Se regresa una matriz de reparaciones[m][n] donde
            # m = reparaciones registradas
            # n = ([0]=folio, [1]=car_id, [2]=date_enter, [3]=time_enter, [4]=date_out, [5]=time_out, [6]=folio_detail, [7]=folio(otra vez), [8]=part_id, [9]=amount
        return list_repairs, list_details
        

    def getLastId(self):
        command = "SELECT MAX(folio) FROM repairs"
        result = self.db.fetchall(command)[0]

        if result[0] is not None:
            return result[0]
        else:
            return 0

    def getFoliosInDateRange(self, from_date, to_date):
        # Convertir las fechas a formato de cadena
        from_date_str = from_date.strftime("%Y-%m-%d")
        to_date_str = to_date.strftime("%Y-%m-%d")
        
        # Consulta SQL para obtener los folios dentro del rango de fechas
        query = f"""
            SELECT DISTINCT folio
            FROM repairs
            WHERE date_enter >= '{from_date_str}' AND date_enter <= '{to_date_str}'
            ORDER BY date_enter
        """
        
        # Ejecutar la consulta y obtener los resultados
        results = self.db.fetchall(query)
        
        # Extraer los folios de los resultados
        folios = [result[0] for result in results]
        repairs = []

        for folio in folios:
            # [0][0]=folio, [0][1]=car_id, [0][2]=date_enter, [0][3]=time_enter, [0][4]=date_out, 
            # [0][5]=time_out, [1][0]=folio_detail, [1][1]=folio(otra vez), 
            # [1][2]=part_id, [1][3]=amount
            repairs.append(self.lookForRepairFolio(folio))
        
        return repairs