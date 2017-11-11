from gui import menu_geral
from logica import usuario
from gui import menu_usuario

from logica import filme



def inicializar_dados():
    filme.iniciar_filmes()
    usuario.iniciar_clientes()




def menu_login_usuario():
    global email
    email = input("Seu email: ")
    global senha
    senha = input("Sua senha: ")
    ind = usuario.login_cliente(email,senha)
    if ind == False:
        print("Login ou senha inválidos. Tente novamente -----")
    else:
        return menu_geral.mostrar_menu_cliente()


def menu_login_admin():
    global email_a
    email_a = input("Seu email: ")
    global senha_a
    senha_a =input("Sua senha: ")
    ind = usuario.login_admin(email_a,senha_a)
    if ind == False:
        print("Login ou senha inválidos. Tente novamente -----")
    else:
        return menu_geral.mostrar_menu_admin()

def mostrar_menu():
    inicializar_dados()
    run_menu = True

    menu = ("\n----------------\n" +
            "(1) Login Usuário \n" +
            "(2) Login Admin \n" +
            "(3) Cadastre-se \n" +
            "(0) Sair\n" +
            "----------------")

    while (run_menu):
        print(menu)

        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_login_usuario()
        elif (op == 2):
            menu_login_admin()
        elif (op == 3):
            menu_usuario.menu_adicionar()
        elif (op == 0):
            print("Saindo do programa...")
            run_menu = False
        else:
            run_menu=True
            print("Valor invalido")