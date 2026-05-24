from cliente import Cliente
from tipos_contas import *


class Banco:
    def __init__(self) -> None:
        self.bd_clientes = [] #Cada Instância da classe Banco deve ter o seu banco de dados(db_clientes) de forma individual
        
    def listar_cliente(self) -> None:
        numeracao = 1
        for cliente in self.bd_clientes:
            print(f" {numeracao} - Cliente: {cliente.nome} | CPF: {cliente.cpf}")
            numeracao += 1
            
    def cadastrar_cliente(self,cliente:Cliente) -> None:
        for objeto in self.bd_clientes:
            if cliente.cpf == objeto.cpf: #Se em algum momento do fluxo o atributo'cpf' for igual a um cpf contindo no objeto que está na lista, o break para o fluxo
                print("CPF já cadastrado")
                break
        else: #Se o o fluxo for concluido(nesse caso o "cpf" é novo, ele cadastra o cliente)
            self.bd_clientes.append(cliente)
            print("Usuário Cadastrado")

    def buscar_cliente(self, cpf)-> None:
        cpf = str(cpf)# Convertendo a entrada(cpf) em string, pois os cpfs dos clientes foram armazenas no bd como string
        for cliente in self.bd_clientes:
            if cpf == cliente.cpf:
                print(f"Cliente: {cliente.nome} | CPF: {cliente.cpf}")
                break
        else:
            print("Usuário não encontrado ")
    
    def transferir(self, conta_origem, conta_destino, valor:int) -> None:
        saldo_origem = conta_origem._info_saldo
        conta_origem.sacar(valor)
        if conta_origem._info_saldo != saldo_origem:#Caso o saque seja efetuado(Ou seja, ocorre uma alteração no saldo de origem), o método depositar irá inserir o valor do saque no saldo da conta destinatária
            conta_destino.depositar(valor)
            print(f"A transferência de R${valor} foi efetuada com sucesso ")
            
            
    def relatorio(self):
        indice = 0
        for cliente in self.bd_clientes:
            for conta in cliente.contas:
                indice += 1
                print(f"Nome do cliente: {cliente.nome} - Conta{indice}: {conta.titular} | R$ {conta._info_saldo},00")

            
        






