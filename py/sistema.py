menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

   opcao = input(menu)
   
   if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
             print("Depósito realizado com sucesso! ")
             saldo += valor
             extrato += f"Depósito: R$ {valor:.2f}\n"           

        else:
            print("Operação falhou! O valor informado é inválido.")



   elif opcao == "s":
       valor = float(input("Informe o valor desejado para saque:  "))

       excedeu_limite = valor > limite

       excedeu_saques = numero_saque >= LIMITE_SAQUES

       if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

       elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

       elif valor > 0:
            print("Saque realizado com sucesso! ")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

       else:
            print("Operação falhou! O valor informado é inválido.")

       if saldo < valor: 
         print("Saldo insuficiente")
           

   elif opcao == "e":
       print("\n=================Extrato==================\n")
       if not extrato:
           print("Não foram realizadas movimentações! ")
       else:
           print(extrato)
           print(f"\nSaldo: R$ {saldo:.2f}")
           print("==========================================")



   elif opcao == "q":
       break
   
   else:
       print("Operação inválida, por favor selecione novamente a operação desejada")
