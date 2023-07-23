menu = """
======= MENU ======= 
| [d] - Depositar  |
| [s] - Sacar      |
| [e] - Extrato    |
| [q] - Sair       |
====================
 ==> """

saldo = 0
saque = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if (opcao == "d") or (opcao == "D"):
        print()

        print("============= Depósito =============")
        valor = float(input("Insira o valor de depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${saldo:.2f}\n"
            print("Deposito realizado com sucesso!!!")
            print("====================================")
        else:
            print("Valor inválido. Escolha novamente a operação!!!")
    
    elif (opcao == "s") or (opcao == "S"):
        
        print("============= Saque =============")
        print()
        valor = float(input("Insira o valor de saque: R$ "))
        
        if (valor <= limite) and (numero_saques < LIMITE_SAQUES):
            print("Saque realizado com sucesso")
            saldo -= valor  
            extrato += f"Saque: R${saldo:.2f}\n"  
            numero_saques += 1            

        elif numero_saques > LIMITE_SAQUES:
            print(f"Você fez {numero_saques}. Limite atingido para hoje.")
            print("====================================")

        elif valor > LIMITE_SAQUES:
            print(f"Total de saques é maior que o limite diário permitido.")

        else:
            print(f"Saldo insuficiente, R${saldo:.2f}!!!")
            print("====================================")
    
    elif (opcao == "e")  or (opcao == "E"):
        print()
        print("============= Extrato =============")
        print("Não foram realizadas movimentaçõe." if not extrato else extrato)
        print(f"Saldo em conta: R${saldo:.2f}")

        print("====================================")

    elif (opcao == "q") or (opcao == "Q"):
        print()
        print("Operação cancelada pelo usuário. Obrigado.")
        print()
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")