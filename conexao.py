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


# def criar_tabela(conexao, sql):
#     try:
#         c = conexao.cursor()
#         c.execute(sql)
#         print('Tabela criada')
#     except Error as e:
#         print(e)
#
#
# vsql = """
#     CREATE TABLE tb_contatos(
#         N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
#         T_NOMECONTATO VARCHAR(30),
#         T_TELEFONECONTATO VARCHAR(14),
#         T_EMAILCONTATO VARCHAR(30)
#     );
# """
# vcon = ConexaoBanco()
# criar_tabela(vcon, vsql)
