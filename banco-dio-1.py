import uuid
from datetime import datetime


def receive_input_value(operation:str)->float:
    print(f"Digite o valor a de {operation}")
    value = input()
    value = float(value.strip().replace(",", '.'))
    if (value > 0):
        return value
    else:
        print(f"Digite um valor válido de {operation}")
        return 0

def cadastrar_usuario(conta_id:int,nome:str):
    id_usuario = uuid.uuid4()
    nome_usuario = nome
    usuario = {nome_usuario:[conta_id]}
    print(f"O usuario {nome_usuario} posssui a(s) conta(s) {usuario[nome_usuario]}")

def cadastar_conta(conta_id:int,usuario:dict):
    usuario

def is_possible_to_saque(value:float,saldo:float,limite:float,num_saques:int)->bool:
    if (value > saldo or value > limite or num_saques > 3 or value > 500):
        print("Não é possível fazer essa operação")
        return False
    return True

def saque(value: float, saldo:float,limite:float,num_saques):
    cache_saldo = saldo
    cache_limite = limite
    cache_num_saques = num_saques

    if is_possible_to_saque(value,saldo,limite,num_saques):
        saldo -= value
        limite -= value
        num_saques += 1
        return saldo, limite, num_saques
    else:
        return cache_saldo, cache_limite, cache_num_saques


def deposita(value:float, saldo:float):
    saldo+= value
    return saldo

def generate_extrato(saldo:float, limite:float):
    print('--------------------')
    print(f"Data e hora:  {datetime.now()}")
    print(f"Valor em conta:  R${saldo}")
    print(f"Valor possível de ser sacado no dia atual: R${limite}")


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
        valor_sacado = receive_input_value("Saque")
        saldo, limite, numero_saques = saque(valor_sacado,saldo,limite,numero_saques)

    if option == 2:
        valor_depositado = receive_input_value("Deposito")
        saldo = deposita(valor_depositado, saldo)


    if option == 3:
        generate_extrato(saldo,limite)


    if option ==4:
        print("**** Saindo ******")
        menu_ativo = False


