from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(self, biblioteca, genere):
        if biblioteca == "Nessun filtro" or not biblioteca:
            biblioteca = None
        if genere == "Nessun filtro" or not genere:
            genere = None

        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Connessione fallita!")
            return []

        cursor = cnx.cursor(dictionary=True)

        query = """
                    SELECT DISTINCT l.* 
                    FROM libro l
                    JOIN biblioteca b ON l.id_biblioteca = b.id
                """
        conditions = []
        params = []

        if biblioteca is not None:
            conditions.append("b.nome = %s")
            params.append(biblioteca)

        if genere is not None:
            conditions.append("l.genere = %s")
            params.append(genere)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        libri = []
        try:
            cursor.execute(query, tuple(params))
            for row in cursor.fetchall():
                libro = Libro(
                    id=row.get("id"),
                    titolo=row.get("titolo"),
                    autore=row.get("autore"),
                    genere=row.get("genere"),
                    anno_pubblicazione=row.get("anno_pubblicazione"),  # Aggiunto
                    id_biblioteca=row.get("id_biblioteca")  # Aggiunto
                )
                libri.append(libro)
            cursor.close()
            cnx.close()
            return libri
        except Exception as e:
            print(f"Errore nella query dei libri: {e}")
            cursor.close()
            cnx.close()
            return []

    def get_generi(self):
        """Recupera tutti i generi distinti dei libri"""
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"

        generi = []
        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                generi.append(row["genere"])
            cursor.close()
            cnx.close()
            return generi
        except Exception as e:
            print(f"Errore nella query dei generi: {e}")
            cursor.close()
            cnx.close()
            return []