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
        print('\n*** Operação realizada com sucesso.\n')
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
    os.system('cls')
    vid = input('Digite o ID do registro a ser deletado: ')

    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO={vid}"

    query(vcon, vsql)
    vcon.close()


def menu_atualizar():
    # indicar o ID do registro que eu quero atualizar, colher os dados e dps indicar qual atualizar
    os.system('cls')
    r = consultar(vcon, "SELECT * FROM tb_contatos")
    print('\n\tLISTA ATUAL')
    for i in r:
        print(i)

    vid = input('\nDigite o ID do registro a ser alterado: ')

    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO={vid}")
    rnome = r[0][1]
    rtelefo = r[0][2]
    remail = r[0][3]

    vnome = input('\nDigite o novo nome: ')
    vtelefo = input('Digite o novo telefone: ')
    vemail = input('Digite o novo email: ')

    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefo) == 0:
        vtelefo = rtelefo
    if len(vemail) == 0:
        vemail = remail

    vsql = f"UPDATE tb_contatos SET T_NOMECONTATO='{vnome}', T_TELEFONECONTATO='{vtelefo}', T_EMAILCONTATO='{vemail}' WHERE N_IDCONTATO={vid}"

    query(vcon, vsql)


def menu_consultar():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0

    print('\n\tLISTA ATUAL\n')
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(r[0], r[1], r[2], r[3]))
        vcont += 1
        if vcont >= vlim:
            vcont = 0

    print('\nFim da lista')
    os.system('pause')

def menu_consultar_nomes():
    vnome = input('\nDigite o nome: ')  # não precisa ser o nome exato
    vsql = f"SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%{vnome}%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0

    print('\n\tLISTA ATUAL\n')
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(r[0], r[1], r[2], r[3]))
        vcont += 1
        if vcont >= vlim:
            vcont = 0

    print('\nFim da lista')
    os.system('pause')
