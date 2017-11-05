from gui import menu_usuario

from gui import menu_filme



'''def mostrar_menu():
    run = True
    menu_usuario = ("\n----------------\n" +
            "(1) Adicionar novo Cliente \n" +
            "(2) Listar Cliente \n" +
            "(3) Buscar Cliente por CPF \n" +
            "(4) Remover Cliente \n" +
            "(0) Voltar\n" +
            "----------------")





    while (run):
        print(menu_usuario)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif (op == 2):
            menu_listar()
        elif (op == 3):
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run = False

if __name__ == "__main__":
    principal()'''


def mostrar_menu_admin():
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
            menu_usuario.mostrar_menu_admin()
        elif (op == 2):
            menu_filme.mostrar_menu_admin()
        elif (op == 3):
            pass
        elif (op == 0):
            print("Voltar")
            run_menu = False
        else:
            run_menu = True
            print("Valor invalido")


if __name__ == "__main__":
    principal()

def mostrar_menu_cliente():
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
            menu_usuario.mostrar_menu_cliente()
        elif (op == 2):
            menu_filme.mostrar_menu_cliente()
        elif (op == 3):
            pass
        elif (op == 0):
            print("Voltar")
            run_menu = False
        else:
            run_menu = True
            print("Valor invalido")


if __name__ == "__main__":
    principal()
