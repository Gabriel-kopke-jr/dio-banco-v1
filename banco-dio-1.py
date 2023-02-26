from datetime import datetime

def receive_input_value(operation:str)->float:
    print(f"Digite o valor a ser {operation}")
    value = input()
    value = float(value.strip().replace(",", '.'))
    return value


limite = 1500
saldo = 2000
menu_ativo = True
numero_saques = 0

print("Olá bem vindo a sistema do banco")

while menu_ativo:
    print("Escolha um dos nossos serviços:")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver Extrato")
    print("4 - Sair")
    option  = int(input())

    if option == 1:
        valor_sacado = receive_input_value("Sacado")
        if(valor_sacado > 0):

            if (valor_sacado > saldo or valor_sacado > limite or numero_saques> 3 or valor_sacado > 500):
                print("Não é possível fazer essa operação")

            else:
                saldo -= valor_sacado
                limite -= valor_sacado
                numero_saques+=1
        else:
            print("Digite um valor válido de saque")

    if option == 2:
        valor_depositado = receive_input_value("Depositado")
        saldo += valor_depositado


    if option == 3:
        print('--------------------')
        print(f"Data e hora:  {datetime.now()}")
        print(f"Valor em conta:  R${saldo}")
        print(f"Valor possível de ser sacado no dia atual: R${limite}")


    if option ==4:
        print("**** Saindo ******")
        menu_ativo = False


