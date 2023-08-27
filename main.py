import time
menu = '''
Escolha uma opcao:

[d] = Deposito
[s] = Saque
[e] = Extrato
[q] = Sair

===> 
'''

saldo = 0
limite = 500
num_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(menu)
    # print(opcao)
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'\nDepósito no valor de R${valor:.2f}'
            print(f'Depósito no valor de R${valor:.2f} realizado com sucesso')
            time.sleep(3)
        else:
            print("\nValor inválido!\n")
            time.sleep(3)
    elif opcao == "s":
        if num_saques >= LIMITE_SAQUES:
            print("Limite de Saques diário atingido.")
            time.sleep(3)
        else:
            valor = float(input("Informe o valor a ser sacado:"))
            if valor <= 0:
                print('\nValor inválido!')
                time.sleep(3)
            elif valor > saldo:
                print("Operação não realizada por falta de saldo")
                time.sleep(3)
            elif valor > 500:
                print("Valor máximo de R$500,00 por saque")
                time.sleep(3)
            else:
                num_saques += 1
                saldo -= valor
                extrato += f"\nSaque no valor de R${valor:.2f}"
                print(f"\nSaque no valor de R${valor:.2f} realizado com sucesso")
                time.sleep(3)
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(f'Extrato:\n {extrato}\n')
            print(f'Saldo: R${saldo:.2f}')
        time.sleep(5)
    elif opcao == "q":
        break
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(3)