from abc import ABC, abstractmethod #Importação para a criação de classes abstratas



class Conta(ABC): #Classe abstrata parcial (métodos com lógica implementada)

    def __init__(self,numero: int, titular:str, _saldo:int) -> None:
        self.numero = numero
        self.titular = titular
        self._saldo = _saldo


    @abstractmethod
    def __str__(self) -> str: #Permite printar o objeto
        pass
    __repr__ = __str__ #Exibi informações do objeto caso o objeto seja printado estando dentro de um container(List(), Dict()..)

    @abstractmethod
    def depositar(self, valordeposito) ->None: #Esse método é igual para todas as subclasses/tipos de contas
        try:
            if valordeposito > 0: #Se o valor do depósito for maior que zero, a transação será permitida
                self._saldo += valordeposito # Soma e guarda o resultado na variavél _saldo
                print("Depósito Efetuado com sucesso")
            else:
                print("O valor do depósito não pode ser igual ou menor zero")
        except TypeError:
            print("O tipo do dado é incompatível com a operação.")
            
    @abstractmethod
    def sacar(self) -> None: # precisa verificar se o valor é maior que 0 e se o valor de saque é compativel com o saldo
        pass
    
    @property
    def _info_saldo(self) -> int: # Método Getter para retornar o atributo privado(_saldo)
        return self._saldo
    
    @abstractmethod
    def extrato(self) -> None: #Deve exibe número da conta, titular e saldo.
        pass
     
    @abstractmethod
    def type_count(self) -> None: # Informa o tipo de conta
        pass


class ContaRentavel(Conta):
    
    @abstractmethod
    def rentabilizar(self) -> None:
        pass