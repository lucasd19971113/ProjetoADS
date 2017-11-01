from gui import menu_usuario
from logica import usuario

from gui import menu_filme
from logica import filme

def inicializar_dados():
    filme.iniciar_filmes()
    usuario.iniciar_clientes()
def mostrar_menu():
    inicializar_dados()
    run_menu = True


    menu = ("\n----------------\n" +
            "(1) Menu Usuário \n" +
            "(2) Menu Filme \n" +
            "(3) Menu Histórico \n" +
            "(0) Sair\n" +
            "----------------")

    while (run_menu):
        print(menu)

        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_usuario.mostrar_menu()
        elif (op == 2):
            menu_filme.mostrar_menu()
        elif (op == 3):
            pass
        elif (op == 0):
            print("Saindo do programa...")
            run_menu = False
        else:
            run_menu=True
            print("Valor invalido")




