from logica import historico

def imprimir_historicos(historico):
    print("\nCPF: ", historico[0])
    print("Código do filme: ", historico[1])
    print()


def menu_adicionar():
    run=True
    while run==True:
        cpf = input("CPF: ")
        while len(cpf) != 11:
            cpf_1 = input("CPF incorreto! - Digite novamente: ")
        cpf=int(cpf)
        cod_filme = input("Código do filme ")
        historico.adicionar_historico(cpf,cod_filme)
        op = int(input(("\n----------------\n" +
                        "(1) Adiconar mais histórico de filmes\n" +
                        "(0) Sair \n" +
                        "\n----------------\n"+
                        "Digite sua escolha: ")))
        while op != 1 and op!= 0:
            op = int(input("Opção Incorreta! - Digite novamente: "))
        if op ==0:
            run=False
    return


def menu_listar():
    print("\nListar histórico de filmes \n")
    historicos = historico.listar_historicos()
    for h in historicos:
       imprimir_historicos(h)



def menu_buscar():
    run = True
    while run == True:
        cpf = int(input("Buscar por CPF: "))
        historico = historico.buscar_historico(cpf)
        if historico == False:
            print("Historico nao encontrado\n")
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



def menu_remover():
    run = True
    while run == True:
        cpf = int(input("Remover historico por CPF: "))
        ind = historico.remover_historico(cpf)
        if ind == False:
            print("Cliente nao encontrado \n")
            op = int(input("\nTentar de novo? \n(1) Sim\n(0) Não "))
            if op == 0:
                run = False
        else:
            print("Histórico do Cliente removido \n")
            op = int(input(("\n----------------\n" +
                            "\n(1) Remover mais clientes\n" +
                            "(0) Sair \n" +
                            "\n----------------\n"+
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False


def mostrar_menu():
    run = True
    menu_historico = ("\n----------------\n" +
            "(1) Registrar Filme assistido \n" +
            "(2) Listar filmes assistidos \n" +
            "(3) Buscar filme assistido por CPF \n" +
            "(4) Remover filme assistido \n" +
            "(0) Voltar\n" +
            "----------------")


    while (run):
        print(menu_historico)
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
