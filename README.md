Sistema Bancário
Descrição do projeto:
Simular um protótipo das regras de um sistema bancário aplicando conceitos de POO

- Estrutura de contas:
System_bank/
│
├── banco.py
├── conta.py
├── cliente.py
├── tipos_contas.py
└── main.py

**Cada Responsabilidade foi divida em módulos seguindo o Single Responsibility Principle (SRP)**
Módulos:
**Conta(Abstação)**
É uma Superclasse/Classe Pai que serve como molde para o módulo de tipos de contas(Abstração). A abstração *Conta* como contrato orientar que todas as classes filhas devem possui os seguintes métodos:
__str__ -> Ao printar o objeto diretamente será exibidos informações chaves.
depositar() -> A abstração já implementa a função pois idependente do tipo de conta, todas tem o método sacar()
sacar() -> O método deve validar se o valor é maior que zero e se possui saldo maior que valor dos saque
_info_saldo -> A abstração implementa o decorator para a manipulação do atributo *_saldo*, para que o mesmo não seja manipulado diretamente.
extrato() -> O método deve exibir as principais informações de suas respectivas contas.
type_count() -> O método informa o tipo(Corrente, Poupança) de sua respectiva conta.

**ContaRentavel (Abstração)**
A classe abstrata ContaRentavel herda o contrato da classe Conta, ou seja, ela continua seguindo as regras básicas de uma conta, mas adiciona uma nova responsabilidade: o método rentabilizar().
Essa abstração deve ser usada apenas por tipos de conta que realmente possuem algum tipo de rendimento, como uma conta poupança ou conta investimento.
Com isso, evitamos adicionar o método rentabilizar() diretamente na classe Conta, pois nem toda conta precisa dessa funcionalidade. Se esse método estivesse em Conta, todas as subclasses seriam obrigadas a implementá-lo, mesmo quando não fizesse sentido.
Dessa forma, o código fica mais coeso e respeita o Princípio da Segregação de Interfaces, já que cada classe só é obrigada a implementar comportamentos que realmente fazem parte da sua responsabilidade.
rentabilizar() -> O método deve aplicar o rendimento sobre o saldo da conta
_____________________________________________________________________________________________________________________________________________________________________
**Classes Concretas**
**Os tipos de contas podem ter seus comportamentos estendidos sem modificar a Abstração Conta, seguindo o Open/Closed Principle (OCP)**
Módulos
- ContaCorrente
A conta do tipo *ContaCorrente* seguiu o contrato proposto pela abstração Conta e através do *POLIMORFISMO* implementa os comportamentos adequados ao contexto nos quais a classe está inserido. A classe *Conta Corrente* possuiu uma particularidade na função sacar(), no qual usa-se o limite do cheque especial caso o usuário não tenha saldo suficiente
- Conta Poupança
A conta do tipo *ContaPoupança* seguiu o contrato proposto pela abstração Conta Rentavel(Extensão da abstração Conta) e através do *POLIMORFISMO* implementa os comportamentos adequados ao contexto nos quais a classe está inserido.
A Classe do tipo *Conta Poupança* possui uma particularidade diferente (motivo da criação da abstração Conta Rentavel) que nesse caso é a função rentabilizar()

***Os tipos de contas implementaram todas as responsabilidades sugerida pela abstração Conta e Conta Rentavel(Conta), seguindo o Liskov Substitution Principle (LSP)**, 

**Houve a separação da função rentabilizar() numa abstração própria(Conta Rentavel), então ContaCorrente não é obrigada a implementar um método de rentabilidade que não faz sentido pra ela, seguindo assim a Interface Segregation Principle (ISP)**
_____________________________________________________________________________________________________________________________________________________________________
- Cliente
O módulo Cliente possui como funções adicionar e listar contas que foram adicionadas.
**Recebe as instâncias das classes Conta Corrente e Conta Poupança por meio de injeção de dependencia e armazena em sua estrutura(Associação do tipo agregação), vale observar que o moódulo cliente depende da abstração Conta, e não de um classe em especifica de baixo nivel, respeitando assim o principio da Inversão de dependência**
DIP:
*ContaCorrente* & *ContaPoupanca* -> 'Conta' <- *Cliente*
*Módulos Baixos* -> 'Abstração' <- *Módulos Principais*
__________________________________________________________________________
- Banco
O módulo Banco possui como funções listar clientes, cadastra-los, buscar clientes, transferir de uma conta para a outra e exibir um relatorio mostrando os clientes cadastrados e suas respectivas contas.
**Recebe as instâncias das classes cliente por meio de injeção de dependencia e armazena em sua estrutura(Associação do tipo agregação)**


____________________________________________________________________________________________________________________________________________________________________

## Como executar

Versão Python: 3.12.1

1. Clone o repositório
2. Acesse a pasta do projeto
3. Execute: python main.py