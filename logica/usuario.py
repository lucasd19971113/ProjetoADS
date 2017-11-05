global clientes
clientes=[]


def adicionar_usuario(cpf, nome,email,senha):
    cliente=[cpf,nome,email,senha]
    clientes.append(cliente)

def listar_clientes():
    return clientes

def buscar_usuario(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(clientes) if cpf in row]
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

def remover_usuario(cpf):
    ind = [(index, row.index(cpf)) for index, row in enumerate(clientes) if cpf in row]
    if ind == []:
        return False
    else:
        pos = ind[0][0]
        del clientes[pos]
        return True

def login_cliente(email,senha):
    email_1 = [(index, row.index(email)) for index, row in enumerate(clientes) if email in row]
    if email_1 == []:
        return False
    linha=email_1[0][0]
    col = email_1[0][1]
    if linha==0 or linha == 1 and col == 2:
        return False
    else:
        cliente=clientes[linha][3]
        if senha != cliente:
            return False
        else:
            return True


def login_admin(email,senha):
    email_1 = [(index, row.index(email)) for index, row in enumerate(clientes) if email in row]
    if email_1 == []:
        return False
    linha=email_1[0][0]
    col = email_1[0][1]
    if linha > 1 and col == 2:
        return False
    else:
        admin=clientes[linha][3]
        if senha != admin:
            return False
        else:
            return True




def iniciar_clientes():
    adicionar_usuario(43356795805,"André","andre.oliveria@gmail.com","12341234")
    adicionar_usuario(43356725805, "Lucas", "lucas.dias@hotmail.com", "34123412")
