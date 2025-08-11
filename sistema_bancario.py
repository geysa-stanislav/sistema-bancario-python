# Definindo as variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# O menu de opções que será exibido para o usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Loop principal do programa
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários atingido.")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        print("Sair")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")