historicos=[]

def adicionar_historico(cpf,cod_filme):
    historico=[cpf,cod_filme]
    historicos.append(historico)

def listar_historicos():
    return historicos


def iniciar_historico():
    adicionar_historico(43356795805,5)
    adicionar_historico(43356725805, 3)
