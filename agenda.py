import os
from CFB_Cursos._Projeto_Agenda.conexao import ConexaoBanco
from CFB_Cursos._Projeto_Agenda.menu import menu_principal
from CFB_Cursos._Projeto_Agenda.funcoes_CRUD import menu_inserir, menu_deletar
from CFB_Cursos._Projeto_Agenda.funcoes_CRUD import menu_atualizar, menu_consultar_ID, menu_consultar_nomes

vcon = ConexaoBanco()

op = ''
while op != '6':
    menu_principal()
    op = input('Digite uma opção: ')

    if op == '1':
        menu_inserir()
    elif op == '2':
        menu_deletar()
    elif op == '3':
        menu_atualizar()
    elif op == '4':
        menu_consultar_ID()
    elif op == '5':
        menu_consultar_nomes()
    elif op == '6':
        os.system('cls')
        print('Saindo do app Agenda...')
    else:
        os.system('cls')
        print('Opção inválida!!!')
        os.system('pause')

os.system('pause')
print('\n***Programa Encerrado')
vcon.close()
