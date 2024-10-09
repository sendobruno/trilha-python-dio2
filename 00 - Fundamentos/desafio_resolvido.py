menu = """
SISTEMA DE AUTOATENDIMENTO

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

*  Limite de R$ 500,00 por saque
** Limite de saques diário: 3

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"

        else:
            print(f"Operação falhou! O valor informado é inválido. [{valor}]")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

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

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n" + " EXTRATO ".center(30, "#"))
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\n-> Saldo: R$ {saldo:.2f}")
        print("\n" + " FIM DO EXTRATO ".center(30, "#"))

    elif opcao == "4":
        break

    else:
        print(f"Operação inválida, por favor selecione novamente a operação desejada. [{opcao}]")
