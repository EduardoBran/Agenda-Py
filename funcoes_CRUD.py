import os
from CFB_Cursos._Projeto_Agenda.conexao import ConexaoBanco
from sqlite3 import Error

vcon = ConexaoBanco()


def query(conexao, sql):  # insert, update, delete
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)
    finally:
        print('\n*** Operação realizada com sucesso.')
        os.system('pause')


def consultar(conexao, sql):
    global res
    try:
        c = conexao.cursor()
        c.execute(sql)
        res = c.fetchall()
    except Error as e:
        print(e)
    return res


def menu_inserir():
    os.system('cls')
    vnome = input('Digite o nome: ')
    vtelefo = input('Digite o telefone: ')
    vemail = input('Digite o email: ')

    vsql = f""" INSERT INTO tb_contatos (
                    T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
                    VALUES ('{vnome}', '{vtelefo}', '{vemail}') 
            """

    query(vcon, vsql)
    vcon.close()


def menu_deletar():
    ...


def menu_atualizar():
    ...


def menu_consultar_ID():
    ...


def menu_consultar_nomes():
    ...
