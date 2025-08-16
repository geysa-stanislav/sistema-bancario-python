# 🏦 Sistema Bancário V2: Programação Orientada a Objetos com Python

Este projeto representa a segunda grande refatoração de um sistema bancário, evoluindo de uma abordagem funcional para um modelo totalmente orientado a objetos (OOP). O objetivo principal foi aplicar os pilares da OOP para criar um sistema mais robusto, escalável e que modela de forma mais fiel as entidades do mundo real, como clientes e contas bancárias.

A implementação anterior, baseada em dicionários e funções, foi completamente reestruturada para utilizar classes, encapsulando dados e comportamentos de forma coesa e organizada.

## 🏛️ Arquitetura e Modelo de Classes (UML)

O design do sistema foi guiado por um modelo de classes UML para garantir que as responsabilidades de cada entidade estivessem bem definidas. A seguir, uma representação textual da arquitetura:

```plaintext
+------------------+           +------------------+
|     Cliente      |           |      Conta       |
+------------------+           +------------------+
| - endereco: str  |           | - saldo: float   |
| - contas: list   |1        * | - numero: int    |
+------------------+<>----------+ - agencia: str   |
| + realizar_transacao() |     | - cliente: Cliente |
| + adicionar_conta()    |     | - historico: Historico |
+------------------+           +------------------+
          ^                      | + saldo() : float|
          |                      | + sacar()        |
          |                      | + depositar()    |
+------------------+           +------------------+
|  PessoaFisica   |
+------------------+
| - cpf: str       |
| - nome: str      |
| - data_nasc: str |
+------------------+
+