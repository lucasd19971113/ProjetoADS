from logica import filme

global teste
codigo_geral_i = 2
def _gerar_codigo():
    global codigo_geral_i
    codigo_geral_i += 1
    return codigo_geral_i

def imprimir_filme(filme):
    print("Código: ", filme[0])
    print("Título: ", filme[1])
    print("Genero: ", filme[2])
    print("Ano: ", filme[3])
    print()
    print()


def menu_adicionar():
    run=True
    while run==True:
        codigo = _gerar_codigo()
        print("Código do Filme: ",codigo)
        titulo = input("Titulo: ")
        genero = input("Gênero: ")
        ano = input("Ano: ")
        while len(ano) != 4:
            ano = input("Ano incorreto! - Digite novamente: ")
        filme.adicionar_filme(codigo,titulo, genero, ano)
        op = int(input(("\n----------------\n" +
                        "(1) Adicionar mais filmes\n" +
                        "(0) Sair \n" +
                        "\n----------------\n" +
                        "Digite sua escolha: ")))
        while op != 1 and op!= 0:
            op = int(input("Opção Incorreta! - Digite novamente: "))
        if op ==0:
            run=False
    return


def menu_listar():
    print("\n----------------\n")
    print("\nListar Filmes\n ")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)



def menu_buscar():
    run = True

    while run == True:
        genero = (input("Buscar por Gênero: "))
        filmes = filme.buscar_filme_g(genero)
        if filmes == False:
            print("Filme nao encontrado\n")
            op = int(input((
                            "\n(1) Buscar mais filmes por Gênero\n" +
                            "(0) Sair \n" +
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Filme encontrado\n")

            op = int(input((
                            "\n(1) Buscar mais filmes por Gênero\n" +
                            "(0) Sair \n" +
                            "Digite sua escolha: ")))


            if op == 0:
                run = False

def menu_buscar_c():
    run = True
    while run == True:
        codigo = int(input("Buscar por Código: "))
        filmes = filme.buscar_filme(codigo)
        if filmes == False:
            print("Filme nao encontrado\n")
            op = int(input((
                "\n(1) Buscar mais filmes por Código\n" +
                "(0) Sair \n" +
                "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Filme encontrado\n")
            op = int(input((
                "\n(1) Buscar mais filmes por Código\n" +
                "(0) Sair \n" +
                "\nDigite sua escolha: ")))

            if op == 0:
                run = False



def menu_buscar_ch(cod_filme):
    run = True
    while run == True:
        filmes = filme.buscar_filme(cod_filme)
        if filmes == False:
            teste = False
            print("Filme nao encontrado\n")
            op = int(input((
                "\n(1) Buscar mais filmes por Código\n" +
                "(0) Sair \n" +
                "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Filme encontrado\n")
            teste = True
            op = int(input((
                "\n(1) Buscar mais filmes por Código\n" +
                "(0) Sair \n" +
                "\nDigite sua escolha: ")))

            if op == 0:
                run = False

def menu_remover():
    run = True
    while run == True:
        codigo = int(input("Remover por código do filme: "))
        ind = filme.remover_filme(codigo)
        if ind == False:
            print("filme nao encontrado \n")
            op = int(input("\nTentar de novo? \n(1) Sim\n(0) Não  "))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False
        else:
            print("Filme removido \n")
            op = int(input(("\n----------------\n" +
                            "\n(1) Remover mais filmes\n" +
                            "(0) Sair \n" +
                            "\n----------------\n" +
                            "Digite sua escolha: ")))
            while op != 1 and op != 0:
                op = int(input("Opção Incorreta! - Digite novamente: "))
            if op == 0:
                run = False

def mostrar_menu():
    run = True
    menu_filme = ("\n----------------\n" +
            "(1) Adicionar Filme \n" +
            "(2) Listar Filme \n" +
            "(3) Buscar Filme por gênero\n" +
            "(4) Buscar Filme por código\n" +
            "(5) Remover Filme por código \n" +
            "(0) Voltar\n" +
            "----------------")

    while (run):
        print(menu_filme)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif (op == 2):
            menu_listar()
        elif (op == 3):
            menu_buscar()
        elif (op == 4):
            menu_buscar_c()
        elif (op == 5):
            menu_remover()
        elif (op == 0):
            run = False

#Chamar menu;
if __name__ == "__main__":
    principal()


