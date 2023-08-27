import time

menu = '''
Escolha uma opcao:

[1] = Deposito
[2] = Saque
[3] = Extrato
[4] = Nova Conta
[5] = Listar Contas
[6] = Novo Cliente
[7] = Sair do Programa

===> 
'''

saldo = 0
limite = 500
num_saques = 0
LIMITE_SAQUES = 3
extrato = ""
clientes = []
contas = []
AGENCIA = "0001"
num_conta = 0


def buscar_cliente(cpf,clientes):
    existe = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            existe = True
    
    return existe

def cad_cliente(nome,dt_nasc,cpf,endereco):
    clientes.append({'nome': nome,'data de nascimento': dt_nasc,'cpf': cpf,'endereco':endereco})
    print("cliente cadastrado com sucesso")

def cad_conta_corrente(num_conta,cpf):
    num_conta += 1
    contas.append({
            "Agencia":AGENCIA,
            "conta":num_conta,
            "usuario":cpf
            })
    print("conta de número {nun_conta} criada com sucesso")
    
    return num_conta

def listar_contas(cpf, contas):
    temp_contas = []
    for conta in contas:
        if conta['usuario'] == cpf:
            temp_contas.append(conta['conta'])
    if len(temp_contas) == 0:
        print('Usuário não possui conta cadastrada')
    else:
        print(temp_contas)

def depositar(valor, saldo, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'\nDepósito no valor de R${valor:.2f}'
        print(f'Depósito no valor de R${valor:.2f} realizado com sucesso')
        time.sleep(3)
    else:
        print("\nValor inválido!\n")
        time.sleep(3)

    return saldo, extrato

def sacar(*,num_saques, valor, saldo, extrato):
    
    if valor <= 0:
        print('\n Operação inválida!\n Valor inválido!')
        time.sleep(3)
    elif valor > saldo:
        print("Operação não realizada por falta de saldo")
        time.sleep(3)
    elif valor > 500:
        print("Falha na operação! \nValor máximo de R$500,00 por saque")
        time.sleep(3)
    else:
        num_saques += 1
        saldo -= valor
        extrato += f"\nSaque no valor de R${valor:.2f}"
        print(f"\nSaque no valor de R${valor:.2f} realizado com sucesso")
        time.sleep(3)

    return num_saques,saldo,extrato

def exibir_extrato(extrato,/,*,saldo):
    print(f'Extrato:\n {extrato}\n')
    print(f'Saldo: R${saldo:.2f}')



while True:
    opcao = int(input(menu))
    # print(opcao)
    if opcao == 1: #depositar
        valor = float(input("Digite o valor do depósito: "))
        saldo,extrato = depositar(valor, saldo, extrato)
        
    elif opcao == 2: #sacar
        if num_saques >= LIMITE_SAQUES:
            print("Limite de Saques diário atingido.")
            time.sleep(3)
        else:
            valor = float(input("Informe o valor a ser sacado:"))
            num_saques, saldo, extrato = sacar(num_saques=num_saques, valor=valor, saldo=saldo, extrato=extrato)
        
    elif opcao == 3: #extrato
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            exibir_extrato(extrato,saldo=saldo)
        time.sleep(5)

    elif opcao == 4: # nova conta
        cpf = input("informe o CPF do usuário: (somente números)")
        if buscar_cliente(cpf,clientes):
            nun_conta = cad_conta_corrente(num_conta,cpf)
        else:
            print("Não foi possivel realizar a operação solicitada, cliente não cadastrado")
        time.sleep(3)
    
    elif opcao == 5: #listar contas
        cpf = input("informe o CPF do usuário: (somente números)")
        cliente = buscar_cliente(cpf,clientes)
        # print(cliente)
        if cliente == True:
            listar_contas(cpf, contas)
        else:
            print("Cliente não encontrado")
        time.sleep(3)
    
    elif opcao == 6: #novo cliente
        print("=============Cadastro de usuário============")
        cpf =  (input("CPF(somente números): "))
        if buscar_cliente(cpf,clientes):
            print("Cliente já existente!")
            time.sleep(3)
        else:
            nome = input("Nome completo: ")
            dt_nasc = input("Data de Nascimento: ")
            endereco = input("logradouro: ")
            endereco += ", "
            endereco += input("Número: ")
            endereco += " - "
            endereco += input("Bairro: ")
            endereco += " - "
            endereco += input("Cidade: ")
            endereco += "/"
            endereco += input("Estado (sigla): ")
            #print(endereco)
            cad_cliente(nome,dt_nasc, cpf,endereco)
            time.sleep(3)
    
    elif opcao == 7:
        break
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(3)