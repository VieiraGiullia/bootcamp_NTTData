# Sistema Bancário em Python

## Descrição

Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

## Funcionalidades

O sistema bancário deve suportar as seguintes operações:

1. **Depósito**: Permitir que o usuário deposite um valor na conta.
2. **Saque**: Permitir que o usuário realize um saque, desde que haja saldo suficiente. Deve haver um limite de 3 saques diários com limite de 500 por saque.
3. **Extrato**: Permitir que o usuário visualize um extrato de todas as transações realizadas, incluindo depósitos e saques.

## Requisitos

- **Python 3.x**: O projeto deve ser desenvolvido usando Python 3.x.
- **Sem bibliotecas externas**: O projeto deve ser implementado sem o uso de bibliotecas externas, utilizando apenas a biblioteca padrão do Python.

## Instalação

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>

## Passo a passo 
- [x]  Definir as variáveis
- [x]  Definir as funções
    - [x]  deposito()
    - [x]  saque()
    - [x]  extrato()
- [x]  Menu de opções
- [x]  Loop do menu
- [x]  ajustes de erro

## Correções que foram necessárias
- [x]  1 teste - deu erro pois não conseguiu acessar a variável saldo, pois ela está fora do escopo da função, esqueci de adicionar a palavra reservada global para acessar a variável saldo fora do escopo da função
- [x]  2 teste - limite de saldo diário ok. limite de saldo ok.
- [x]  ajustar o extrato para que haja uma lista de operações realizadas