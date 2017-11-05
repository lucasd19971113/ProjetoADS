from logica import usuario
from  gui import menu_geral_login

def imprimir_cliente(cliente):
    print("\nCPF: ", cliente[0])
    print("Nome: ", cliente[1])
    print("E-mail: ", cliente[2])
    print("Senha: ", cliente[3])
    print()


def menu_adicionar():
    run=True
    while run==True:
        cpf_1 = input("CPF: ")
        while len(cpf_1) != 11:
            cpf_1 = input("CPF incorreto! - Digite novamente: ")
        cpf=int(cpf_1)
        nome = input("Nome: ")
        email = input("email: ")
        senha = input("Digite sua senha: ")
        while len(senha) < 8:
            senha = input("Sua senha deve ter no minimo 8 caracteres: ")
        senha_1 = input("Confirme sua senha: ")
        while senha_1 != senha:
            senha_1 = input("Confirme sua senha: ")
        usuario.adicionar_usuario(cpf, nome, email ,senha_1)
        op = int(input(("\n----------------\n" +
                        "(1) Cadastrar mais usuários?\n" +
                        "(0) Sair \n" +
                        "\n----------------\n"+
                        "Digite sua escolha: ")))
        while op != 1 and op!= 0:
            op = int(input("Opção Incorreta! - Digite novamente: "))
        if op ==0:
            run=False
    return


def menu_listar():
    print("\nListar Clientes \n")
    clientes = usuario.listar_clientes()
    for c in clientes:
        imprimir_cliente(c)



def menu_buscar():
    run = True
    while run == True:
        cpf = int(input("Buscar por CPF: "))
        clientes = usuario.buscar_usuario(cpf)
        if clientes == False:
            print("Cliente nao encontrado\n")
            op = int(input(("\n----------------\n" +
            "\n(1) Realizar nova busca\n" +
            "(0) Sair \n" +
            "\n----------------\n"+
            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Cliente encontrado\n")
            op = int(input(("\n----------------\n" +
                            "\n(1) Realizar nova busca\n" +
                            "(0) Sair \n" +
                            "\n----------------\n"+
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False


'''def menu_buscar_h(cpf):
    run = True
    while run == True:
        clientes = usuario.buscar_usuario(cpf)
        if clientes == False:
            print("Cliente nao encontrado\n")
            op = int(input(("\n----------------\n" +
            "\n(1) Realizar nova busca\n" +
            "(0) Sair \n" +
            "\n----------------\n"+
            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Cliente encontrado\n")
            op = int(input(("\n----------------\n" +
                            "\n(1) Realizar nova busca\n" +
                            "(0) Sair \n" +
                            "\n----------------\n"+
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False'''



def menu_remover():
    run = True
    while run == True:
        cpf = int(input("Remover por CPF: "))
        ind = usuario.remover_usuario(cpf)
        if ind == False:
            print("Cliente nao encontrado \n")
            op = int(input("\nTentar de novo? \n(1) Sim\n(0) Não "))
            if op == 0:
                run = False
        else:
            print("Cliente removido \n")
            op = int(input(("\n----------------\n" +
                            "\n(1) Remover mais clientes\n" +
                            "(0) Sair \n" +
                            "\n----------------\n"+
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False

#------------- Somente email e senha utilizados no login podem ser modificados ----------------------

def menu_editar_senha():
    senha_0=input("Digite sua senha: ")
    if senha_0!= menu_geral_login.senha:
        print("Senha inválida")
        return
    senha_nova = input("Digite sua nova senha: ")
    while len(senha_nova) < 8:
        senha_nova = input("Sua senha deve ter no minimo 8 caracteres: ")
    senha_1 = input("Confirme sua senha: ")
    while senha_1 != senha_nova:
        senha_nova = input("Confirme sua senha: ")
    nova_senha = usuario.editar_senha(senha_0,senha_nova)
    if nova_senha == False:
        print("Senha inválida. Tente novamente")
    else:
        print("Senha modificada com sucesso!")
        return


def menu_editar_email():
    email_1 = input("Digite seu e-mail: ")
    if email_1!= menu_geral_login.email:
        print("E-mail inválido")
        return
    email_novo = input("Digite seu novo e-mail: ")
    while email_1!= email_novo:
        email_novo = input("Confirme seu e-mail: ")
    email_n=usuario.editar_email(email_1,email_novo)
    if email_n==True:
        print("Email modificado com sucesso!")
        return
    else:
        print("Tente de novo")

#-----------------------------------------------------------------------------------------------------------

def menu_mostrar_cadastro():
    email_1= input("Digite seu e-mail:  ")
    if email_1!= menu_geral_login.email:
        print("E-mail inválido")
        return
    else:
        ind=usuario.mostrar_usuario(email_1)
        return ind


def mostrar_menu_admin():
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
    principal()

def mostrar_menu_cliente():
    run = True
    menu_usuario = ("\n----------------\n" +
            "(1) Editar e-mail \n" +
            "(2) Editar senha \n" +
            "(3) Meu cadastro \n"
            "(0) Voltar\n" +
            "----------------")


    while (run):
        print(menu_usuario)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_editar_email()
        elif (op == 2):
            menu_editar_senha()
        elif (op == 3):
            menu_mostrar_cadastro()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run = False

if __name__ == "__main__":
    principal()

