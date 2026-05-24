from conta import Conta, ContaRentavel


class Cliente():
    
    
    def __init__(self, nome:str, cpf:str) -> None: 
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    
    def __str__(self) -> None:
        return f"Nome do titular: {self.nome}\nCPF: {self.cpf}" 

    __repr__ = __str__
        
    def adicionar_conta(self, conta:Conta):  #ContaPoupanca & ContaCorrente > Abastação('Conta') < Cliente
        self.contas.append(conta)
       
    def listar_contas(self)-> None:
        if len(self.contas) != 0:
            indice = 1
            for conta in self.contas:
                if isinstance(conta, ContaRentavel):
                    tipo_conta = "Conta Poupança"
                else:
                    tipo_conta = "Conta Corrente"
                print(f"Id conta: {indice} | número da conta: {conta.numero} | Titular da conta: {conta.titular} | Saldo em conta: R$ {conta._info_saldo} | Tipo de Conta: {tipo_conta}" )
                indice += 1
        


# # for conta in Vanessa.conta:
# #     if isinstance(conta, ContaRentavel):
# #         conta.render()