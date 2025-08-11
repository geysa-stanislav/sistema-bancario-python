# 🏦 Sistema Bancário Simples em Python

Este é um projeto simples de sistema bancário desenvolvido em Python. O objetivo principal foi colocar em prática conceitos fundamentais da linguagem, como variáveis, estruturas de controle de fluxo (`if`, `elif`, `else`) e loops (`while`).

O sistema simula operações bancárias básicas, permitindo ao usuário interagir com um menu para realizar depósitos, saques e visualizar um extrato.

## ✨ Funcionalidades

O programa oferece as seguintes operações:

-   **Depósito**: Permite adicionar fundos à conta. Apenas valores positivos são aceitos.
-   **Saque**: Permite retirar dinheiro da conta, com as seguintes regras de negócio:
    -   Limite máximo de R$ 500,00 por saque.
    -   Limite de 3 saques diários.
    -   Não permite sacar um valor maior que o saldo disponível.
-   **Extrato**: Exibe o histórico de todas as transações (depósitos e saques) realizadas, além do saldo atual da conta.

## ⚙️ Como Usar

Para executar este sistema, você precisa ter o Python 3 instalado em sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [insira aqui o link do seu repositório]
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd nome-da-sua-pasta
    ```

3.  **Execute o programa:**
    ```bash
    py sistema_bancario.py
    ```

Após a execução, um menu interativo será exibido no terminal, e você poderá selecionar a operação desejada.




Este projeto foi desenvolvido como parte de um desafio prático da plataforma DIO.
