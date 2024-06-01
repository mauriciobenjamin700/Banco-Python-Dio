# Repositório Destiado a Realizar o Desáfio "Criando um Sistema Bancário com Python" do Curso de Estruturas de Dados em Python

A ideia do projeto é simuar um sistema bancário simples usando linguagem python, entretanto devido a oportunidade de aprofundar os conhecimentos da linguagem, o projeto acabou escalando e permitindo a criação de um projeto maior, envolvendo conteúdos a mais como banco de dados, interface gráfica e novas dependencias.

## Funcionalidades Obrigatórias para o Desafio

- depositar
- sacar
- extrato

## Funcionalidades Adicionais

- Cadastro de Usuário
- Login do Usuário
- Transferencia Entre Contas
- Sistema de Agencias para Organizar as Contas

## Regras de Negócio

    - Um único usuário acessa por vez
    - Não se pode depositar valores negativos
    - Máximo de 3 saques diários
    - Se não tiver saldo, não pode sacar
    - Valor máximo de R$ 500.00 por saque
    - Todos os valores de extrato devem estar no seguinte formato: R$ xxx.xx

## Dependências de Execução

- Tenha a Linguagem Python instalada em sua maquina.
- Use o pip ou poetry para gerir as dependencias
- Todos os comandos devem ser executados em um terminal
  - Se optar pelo pip, crie uma virtualenv para as depdencias: `python -m venv venv`
    - Ative sua venv usando `venv/Scripts/Activate` no windows ou `source venv/bin/activate` no linux
    - execue `pip install -r requirements.txt`
  - Se optar pelo poetry, instale o primeiro seguindo a [documentação](https://python-poetry.org/docs/)
    - Ative usando `poetry install`
- Execute o arquivo [main.py](main.py) e aproveite do sistema.
