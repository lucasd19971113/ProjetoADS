historicos=[]


def adicionar_historico(cpf,cod_filme):
    historico=[cpf,cod_filme]
    historicos.append(historico)

def listar_historicos():
    return historicos


def iniciar_historico():
    adicionar_historico(43356795805,1)
    adicionar_historico(43356721405,2)