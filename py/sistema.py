menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3

while True:

   opcao = input(menu)
   
   if opcao == "d":
      print("Depósito")


   elif opcao == "s":
       print("Saque")
       
           

   elif opcao == "e":
       print("Extrato")

   elif opcao == "q":
       break
   
   else:
       print("Operação inválida, por favor selecione novamente a operação desejada")
