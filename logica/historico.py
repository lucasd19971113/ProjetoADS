from logica import usuario
from logica import filme
historicos=[]




def adicionar_historico(cpf,cod_filme):
    ind = [(index, row.index(cpf)) for index, row in enumerate(usuario.clientes) if cpf in row]
    if ind == []:
        return False
    ind_1 = [(index, row.index(cod_filme)) for index, row in enumerate(filme.filmes) if cod_filme in row]
    if ind_1 == []:
        return False
    if ind == cpf and ind_1 == cod_filme:

        historico=[cpf,cod_filme]
        historicos.append(historico)
        return True

def listar_historicos(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(historicos) if cpf in row]
    if ind == []:
        return False
    else:
        cont=0
        while cont<len(ind):
            linha=ind[cont][0]
            print("\n\nCPF do usuário:  ",historicos[linha][0],"\nCódigo do filme assistido:  ",historicos[linha][1],"\n\n")
            cont+=1
        return


def iniciar_historico():
    pass


