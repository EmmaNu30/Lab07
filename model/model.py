from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        if biblioteca == "Nessun filtro" or not biblioteca:
            biblio_param = None
        else:
            biblio_param = biblioteca

        if genere == "Nessun filtro" or not genere:
            genere_param = None
        else:
            genere_param = genere

        return self._libro_dao.get_libri_filtrati(biblio_param, genere_param)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteche()
