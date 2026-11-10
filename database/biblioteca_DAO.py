from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        """Recupera tutte le biblioteche presenti nel database"""
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT nome FROM biblioteca ORDER BY nome"

        biblioteche = []
        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                biblioteche.append(row["nome"])
            cursor.close()
            cnx.close()
            return biblioteche
        except Exception as e:
            print(f"Errore nella query delle biblioteche: {e}")
            cursor.close()
            cnx.close()
            return []
