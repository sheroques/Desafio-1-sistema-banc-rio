menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R${valor:.2f}\n"

        else: 
            print ("erro")

    elif opcao == "s":
        valor = float(input("informe o valor do saque"))

        excedeu_saldo= valor > saldo
        
        excedeu_limite= valor > limite

        excedeu_saques = numero = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("saldo insuficiente")
        
        elif excedeu_limite:
            print("sem limite")

        elif excedeu_saques:
            print (" saques excedidos")

        elif valor > 0:
             saldo -= valor
             extrato += f"saque: R${valor:.2f}\n"
             numero_saques += 1
            
        else:
            print("invalido")


    elif opcao == "e":
        print("\n =================EXTRATO===================")
        print("nao foram realizados movimentacoes" if not extrato else extrato)
        print (f"\n saldo: R${ saldo:.2f} ")
        print ("========================================================")
            
    elif opcao == "q":
        break 

    else:
        print("Operacao invalida, por favor selecione novamente a operacao dessa janela")