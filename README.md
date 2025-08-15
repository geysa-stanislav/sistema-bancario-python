# 🏦 Sistema Bancário Otimizado com Funções em Python

Este projeto é a evolução de um sistema bancário simples, refatorado para utilizar **funções** e estruturas de dados mais robustas em Python. O objetivo foi aplicar conceitos de modularização, separação de responsabilidades e aprimorar a organização do código, tornando-o mais limpo, legível e escalável.

O sistema agora distingue **usuários (clientes)** e **contas bancárias**, permitindo que cada usuário possa ter múltiplas contas no futuro.

## ✨ Funcionalidades

O programa foi aprimorado e agora oferece as seguintes operações:

### Operações Bancárias
-   **Depósito**: Permite adicionar fundos à conta. Apenas valores positivos são aceitos.
-   **Saque**: Permite retirar dinheiro da conta, com as seguintes regras de negócio:
    -   Limite máximo de R$ 500,00 por saque.
    -   Limite de 3 saques diários.
    -   Não permite sacar um valor maior que o saldo disponível.
-   **Extrato**: Exibe o histórico de todas as transações (depósitos e saques), além do saldo atual da conta.

### Gerenciamento de Usuários e Contas
-   **Novo Usuário**: Cadastra um novo cliente no sistema com nome, data de nascimento, CPF e endereço. O sistema impede a criação de usuários com CPFs duplicados.
-   **Nova Conta**: Cria uma nova conta corrente vinculada a um usuário já existente. Cada conta possui uma agência e um número único.
-   **Listar Contas**: Exibe uma lista com todas as contas cadastradas no sistema.

## 🚀 Tecnologias e Conceitos Aplicados

Este projeto foi desenvolvido utilizando **Python 3** e foca nos seguintes conceitos:

-   **Modularização com Funções**: Todo o sistema foi dividido em funções específicas para cada operação (`depositar`, `sacar`, `criar_usuario`, etc.), melhorando a organização e o reuso de código.
-   **Estruturas de Dados**: Uso de **listas** e **dicionários** para armazenar e gerenciar os dados de usuários e contas.
-   **Argumentos de Função**: Aplicação de `positional-only` e `keyword-only arguments` para definir assinaturas de função mais claras e seguras.
-   **Separação de Responsabilidades**: A lógica de cada operação está encapsulada em sua própria função, facilitando a manutenção e futuros upgrades.
-   **Manipulação de Strings**: Uso de `f-strings` e da biblioteca `textwrap` para formatar saídas no terminal.

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
    python sistema_bancario.py
    ```

Após a execução, um menu interativo será exibido no terminal, e você poderá selecionar a operação desejada.

---

Este projeto foi desenvolvido como parte de um desafio prático da plataforma DIO, focando na evolução e refatoração de um sistema pré-existente.