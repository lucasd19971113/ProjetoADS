global filmes
filmes=[]


codigo_geral_i = 0
def _gerar_codigo():
    global codigo_geral_i
    codigo_geral_i += 1
    return codigo_geral_i


def adicionar_filme(codigo,titulo,genero,ano):
    filme=[codigo,titulo,genero,ano]
    filmes.append(filme)


def listar_filmes():
    return filmes


def buscar_filme_g(genero):
    ind = [(index, row.index(genero)) for index, row in enumerate(filmes) if genero in row]
    if ind == []:
        return False

    else:

        pos = ind[0][0]
        print("\n----------------\n")
        print("Filme Por Gênero\n")
        print('\nCódigo: ', filmes[pos][0])
        print('Título: ', filmes[pos][1])
        print('genero: ', filmes[pos][2])
        print('ano: ', filmes[pos][3])
        print("\n----------------\n")
        if filmes[0] == genero:
            return filmes[0]


def buscar_filme(codigo):
    ind = [(index, row.index(codigo)) for index, row in enumerate(filmes) if codigo in row]
    if ind == []:
        return False

    else:

        pos = ind[0][0]
        print("\n----------------\n")
        print("\nFilme Por Código")
        print('Código: ', filmes[pos][0])
        print('Título: ', filmes[pos][1])
        print('genero: ', filmes[pos][2])
        print('ano: ', filmes[pos][3])
        print("\n----------------\n")
        if filmes[0] == codigo:
            return filmes[0]


def remover_filme(codigo):
    ind = [(index, row.index(codigo)) for index, row in enumerate(filmes) if codigo in row]
    if ind == []:
        return False
    else:
        pos = ind[0][0]
        del filmes[pos]
        return True


def iniciar_filmes():
   adicionar_filme(_gerar_codigo(),"André","Terror",2016)
   adicionar_filme(_gerar_codigo(), "Lucas", "Esportes", 2012)

