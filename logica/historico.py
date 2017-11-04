historicos=[]


def adicionar_historico(cpf,cod_filme):
    historico=[cpf,cod_filme]
    historicos.append(historico)

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
    adicionar_historico(43356725805,1)
    adicionar_historico(43356721405,2)

    adicionar_historico(43356725805,5)
    adicionar_historico(43356725805, 3)

