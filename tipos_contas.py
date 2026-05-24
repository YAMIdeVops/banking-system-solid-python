from conta import Conta, ContaRentavel

class ContaCorrente(Conta): #Aplicando o conceito de herança
    def __init__(self, numero:int, titular:str, _saldo:int) ->None:
        super().__init__(numero, titular, _saldo)
        self._limite_cheque = 500

    def __str__(self):
        return f"Number:{self.numero}\nUser:{self.titular}\nValue:{self._info_saldo}\nCheque Especial: R${self._limite_cheque}"
    __repr__ = __str__

    def depositar(self, valordeposito) -> None:
        super().depositar(valordeposito)
    
    def chequeespecial(self, valorsaque):
        if self._saldo + self._limite_cheque >= valorsaque: # Verifica se o limite especial e o saldo conseguem cobrir o valor do saque
            diferenca_do_valor = self._saldo - valorsaque # Recebe a diferença de valor entre o saque e o saldo em conta
            self._saldo -= valorsaque

            self._limite_cheque += self._saldo # É descontado a diferença entre saldo em conta e saque, do saldo do chque especial
            self._saldo -= diferenca_do_valor # O saldo recebe a diferença de volta(fica zerado)
            print(f"Você não tem saldo suficiente\nRecorrendo ao cheque especial...\nSaque de R$ {valorsaque} efetuando com sucesso")
        else:
            print("O valor solicitado é maior que o saldo disponível e também ultrapassa o limite do cheque especial.")

        
    def sacar(self,valorsaque):
        try:
            if valorsaque > 0:
                if self._saldo >= valorsaque:
                    self._saldo -= valorsaque
                    print("Saque efetuado com sucesso")
                else:
                    self.chequeespecial(valorsaque)
            else:
                print("O valor do saque não pode ser menor ou igual a R$00,00")
        except TypeError:
            print("O tipo do dado é incompatível com a operação.")

    
    def extrato(self):
        print("=" * 40)
        print("📄 EXTRATO DA CONTA".center(40))
        print("=" * 40)
        print(f"🏦 Conta: {self.numero}")
        print(f"👤 Titular: {self.titular}")
        print(f"💰 Saldo: R$ {self._info_saldo:.2f}")
        print(f"🛡️ Cheque Especial: R$ {self._limite_cheque:.2f}")
        print("=" * 40)
    
    def type_count(self):
        print("Tipo de conta: Conta Corrente")



class ContaPoupanca(ContaRentavel): #A classe Conta Rentavel é uma abstração que estende o contrato da classe conta (ContaRentavel(Conta))
    def __init__(self, numero, titular, _saldo)->None:
        super().__init__(numero, titular, _saldo)
        self._rentabilidade = 0.01
        
    def __str__(self):
        return f"Number:{self.numero}\nUser:{self.titular}\nValue:{self._info_saldo}\nRendimento: R${self._rentabilidade}"
    __repr__ = __str__

    def depositar(self, valordeposito) -> None:
        return super().depositar(valordeposito)

    def rentabilizar(self): # Implementando o método da abstração Conta Rentavel
        self._saldo += (self._saldo * self._rentabilidade)
        print("O rendimento foi aplicado a sua conta")
    
    def sacar(self,valorsaque):
        try:
            if valorsaque > 0:
                if self._saldo >= valorsaque:
                    self._saldo -= valorsaque
                    print("Saque efetuado com sucesso")
                else:
                    print("Você não tem saldo suficiente")
            else:print("O valor do saldo deve ser maior que R$ 0,00")
        except TypeError:
            print("O tipo do dado é incompatível com a operação.")
    def extrato(self):
        print("=" * 40)
        print("📄 EXTRATO DA CONTA".center(40))
        print("=" * 40)
        print(f"🏦 Conta: {self.numero}")
        print(f"👤 Titular: {self.titular}")
        print(f"💰 Saldo: R$ {self._info_saldo:.2f}")
        print(f"🛡️ Rentabilidade: R$ {self._rentabilidade:.2f}")
        print("=" * 40)
    
    
    def type_count(self):
        print("Tipo de conta: Conta Poupança")
    
