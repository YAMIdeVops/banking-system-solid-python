
from tipos_contas import ContaCorrente, ContaPoupanca
from cliente import Cliente
from banco import Banco


contacorrente = ContaCorrente(1,"usuário1",50)
contapoupanca2 = ContaPoupanca(2,"usuário2",100)
contacorrente3 = ContaCorrente(3,"usuário3",550)
contacorrente4 = ContaCorrente(4,"usuário4",600)
contacorrente5 = ContaCorrente(5,"usuário5",650)
contacorrente6 = ContaCorrente(6,"usuário6",700)
contacorrente7 = ContaCorrente(7,"usuário7",750)




# Testes copm a conta corrente
contacorrente.extrato()
print()
contacorrente.depositar(-3)
print()
contacorrente.depositar(0)
print()
contacorrente.depositar("m")
print()
contacorrente.depositar(50)
print()
contacorrente.extrato()
print()
contacorrente.sacar(-1)
print()
contacorrente.sacar(0)
print()
contacorrente.sacar("m")
print()
#contacorrente.sacar(50)
print()
contacorrente.sacar(601)
print()
contacorrente.sacar(600)
print()
contacorrente.extrato()
print(contacorrente)

#Testes com a Conta Poupança
contapoupanca2.extrato()
print()
contapoupanca2.depositar(0)
print()
contapoupanca2.depositar(75)
print()
contapoupanca2.depositar("")
print()
contapoupanca2.sacar(250)
print()
contapoupanca2.rentabilizar()
print()
contapoupanca2.extrato()
print(contapoupanca2)

#Testes com Conta
Bruno = Cliente("Bruno", "10133455335")
Bruno.listar_contas()
print()
Bruno.adicionar_conta(contacorrente)
Bruno.adicionar_conta(contacorrente3)
Bruno.adicionar_conta(contapoupanca2)
Bruno.listar_contas()
print()
print(Bruno)


Vanesa = Cliente("Vanessa S Leite", "09830048381")
Vanesa.adicionar_conta(contacorrente6)

# Testes com Banco
Inter = Banco()
Inter.cadastrar_cliente(Bruno)
Inter.cadastrar_cliente(Vanesa)
contacorrente6.extrato()
print()
contacorrente.extrato()
print()
Inter.listar_cliente()
print()
Inter.relatorio()
print()
Inter.buscar_cliente(10133455335)
print()
Inter.transferir(contacorrente6,contacorrente, 120)
print()
contacorrente6.extrato()
print()
contacorrente.extrato()
