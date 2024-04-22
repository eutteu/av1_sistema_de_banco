menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

===> """

saldo = 0
limite = 500
extrato = ""
limites_saques = 3
numeros_saques = 0

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("VALOR DO DEPOSITO?"))
        
        saldo += deposito

        extrato += f"Deposito {deposito:.2f}\n"

        print("Valor depositado!")
    elif opcao == 2:
        valor_saque = float(input("VALOR DO SAQUE?"))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saque_diario = numeros_saques > limites_saques

        if excedeu_saldo:
            print("Sem saldo suficiente!")

        elif excedeu_limite:
            print("Excedeu o limite!")

        elif excedeu_saque_diario:
            print("Excedeu o limite de saques diarios!")

        elif valor_saque > 0:
            saldo +- valor_saque
            extrato += f"Saque {valor_saque:.2f}\n"
            numeros_saques += 1

            print("Valor Sacado")
    elif opcao == 3:

        print("EXTRATO")
        print("Movimentações" if not extrato else extrato)
        print(f"Saldo da sua conta é R${saldo:.2f}")

    elif opcao == 4:
        print("Saindo....")
        break

    else:
        print("Opção inválida. Escolha novamente.")