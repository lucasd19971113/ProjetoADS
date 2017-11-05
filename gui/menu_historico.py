from logica import historico
from gui import menu_usuario
from gui import menu_filme
global cpf
global cod_filme


def imprimir_historicos(historico):
    print("CPF: ", historico[0])
    print("Código do filme: ",historico[1])
    print()


def menu_adicionar():
    run=True
    while run==True:
        cpf_1 = input("CPF: ")
        while len(cpf_1) != 11:
            cpf_1 = input("CPF incorreto! - Digite novamente: ")
        cpf = int(cpf_1)
        cod_filme =int (input("Digite o código do filme: "))
        ind=historico.registrar_filme_assistido(cpf, cod_filme)
        if ind==False:
            print("Não foi possível assistir filme")
        else:
            print("Operação realizada")
            run=False
        op = int(input(("\n----------------\n" +
                        "(1) Assistir mais \n" +
                        "(0) Sair \n" +
                        "\n----------------\n" +
                        "Digite sua escolha: ")))
        while op != 1 and op != 0:
            op = int(input("Opção Incorreta! - Digite novamente: "))
        if op == 1:
            run = True
        else:
            run=False
    return


def menu_listar():
    print("\nListar histórico de filmes assistidos de usuário por cpf: \n")
    cpf_1 = input("CPF: ")
    while len(cpf_1) != 11:
        cpf_1 = input("CPF incorreto! - Digite novamente: ")
    cpf = int(cpf_1)
    historicos = historico.listar_filmes_assistidos(cpf)
    if historicos == True:
        print(historicos)






def mostrar_menu():
    run = True
    menu_historico = ("\n----------------\n" +
            "(1) Assistir \n" +
            "(2) Listar filmes assistidos \n" +
            "(0) Voltar\n" +
            "----------------")


    while (run):
        print(menu_historico)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif (op == 2):
            menu_listar()
        elif (op == 0):
            run = False

if __name__ == "__main__":
    principal()
