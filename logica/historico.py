from logica import usuario
from logica import filme
historicos=[]




def registrar_filme_assistido(cpf,cod_filme):
    ind = [(index, row.index(cpf)) for index, row in enumerate(usuario.clientes) if cpf in row]
    if ind == []:
        return False
    ind_1 = [(index, row.index(cod_filme)) for index, row in enumerate(filme.filmes) if cod_filme in row]
    if ind_1 == []:
        return False
    else:
        linha_cli=ind[0][0]
        linha_f=ind_1[0][0]
        nome_cli=usuario.clientes[linha_cli][1]
        titulo_filme=filme.filmes[linha_f][1]
        historicos.append([nome_cli,cpf,titulo_filme,cod_filme])

def listar_filmes_assistidos(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(historicos) if cpf in row]
    if ind == []:
        return False
    else:
        cont=0
        while cont<len(ind):
            linha=ind[cont][0]
            print("\n\nNome: ",historicos[linha][0],"\nCPF:  ",historicos[linha][1],"\nTitulo do filme: ",historicos[linha][2],"\nCódigo do filme assistido:  ",historicos[linha][3],"\n\n")
            cont+=1
        return


def iniciar_historico():
    pass


