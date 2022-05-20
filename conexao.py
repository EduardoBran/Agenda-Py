import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = r'C:\cursopython\CFB_Cursos\Banco\agenda_proj.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as e:
        print(e)
    return con