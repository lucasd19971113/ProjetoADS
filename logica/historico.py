historicos=[]

def adicionar_historico(cpf,cod_filme):
    historico=[cpf,cod_filme]
    historicos.append(historico)

def listar_historicos():
    return historicos

def buscar_historico(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(filmes) if cpf in row]
    if ind == []:
        return False
    else:
        pos = ind[0][0]

        print('\nCPF: ', clientes[pos][0])
        print('Nome: ', clientes[pos][1])
        print('E-mail: ', clientes[pos][2])
        print('Senha: ', clientes[pos][3],'\n')
        if clientes[0] == cpf:
            return clientes[0]

def remover_historico(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(clientes) if cpf in row]
    if ind == []:
        return False
    else:
        pos = ind[0][0]
        del clientes[pos]
        return True


def iniciar_hisotico():
    pass
