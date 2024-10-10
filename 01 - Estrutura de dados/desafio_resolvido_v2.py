def buscar_usuario(cpf, usuarios):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuario_encontrado


def criar_conta(usuarios, contas, AGENCIA):
    cpf = input("Digite o CPF do cliente: ")
    usuario_encontrado = buscar_usuario(cpf, usuarios)   
    
    if usuario_encontrado != []:
        conta = len(contas) + 1
        contas.append({"agencia": AGENCIA, "conta": conta, "cpf": cpf})
        print("\nConta criada com sucesso.")

    else:
        print("\nCPF não pertence a um cliente válido. Não é possível criar uma conta.")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF do cliente: ")
    usuario_encontrado = buscar_usuario(cpf, usuarios)   
    
    if usuario_encontrado == []:
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\nUsuário cadastrado com sucesso.")

    else:
        print("\nUsuário já é um cliente.")


def depositar(saldo, valor, extrato, /):
   
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
        print("Deposito realizado com sucesso.")

    else:
        print(f"Operação falhou! O valor informado é inválido. [{valor}]")

    return saldo, extrato


# def criar_usuario(*, nome, data_nascimento, cpf, endereco, lista):


def exibir_extrato(saldo, /, *, extrato):
    print("\n" + " EXTRATO ".center(30, "#"))
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\n-> Saldo: R$ {saldo:.2f}")
    print("\n" + " FIM DO EXTRATO ".center(30, "#"))


def sacar(*, saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo é de R$ {saldo}.")

    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite}.")

    elif excedeu_saques:
        print(f"Operação falhou! Número máximo de saques excedido. [{LIMITE_SAQUES}]")

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def menu():
    menu = """
    SISTEMA DE AUTOATENDIMENTO

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar cliente
    [5] Cadastrar conta
    [6] Sair

    *  Limite de R$ 500,00 por saque
    ** Limite de saques diário: 3

    => """

    return input(menu)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 100
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1": # Depósitar
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2": # Sacar
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "3": # Extrato
            exibir_extrato(saldo, extrato=extrato)    

        elif opcao == "4": # Cadastrar cliente
            criar_usuario(usuarios)
        
        elif opcao == "5": # Cadastrar conta    
            criar_conta(usuarios, contas, AGENCIA)

        elif opcao == "6": # Sair
            break

        else:
            print(f"Operação inválida, por favor selecione novamente a operação desejada. [{opcao}]")


main()


