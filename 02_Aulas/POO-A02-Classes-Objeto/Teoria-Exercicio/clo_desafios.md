# Desafio:

## 1 Gerenciador de Tarefas

Crie um sistema de Gerenciador de Tarefas utilizando somente classes e objetos. O sistema deve permitir:

    Criar tarefas com descrição e status (pendente ou concluída).
    Alterar o status da tarefa (de pendente para concluída).
    Listar todas as tarefas e indicar quais já foram concluídas.
    Regras:

O código deve usar apenas classes e objetos
O usuário deve criar pelo menos três tarefas.
As tarefas devem ser exibidas de maneira organizada.

## 2 : Sistema de Gestão de Contas Bancárias

Você foi contratado para desenvolver um sistema de gestão de contas bancárias, permitindo que clientes criem contas, realizem depósitos, saques e consultem seus saldos.

Requisitos:

    Crie uma classe ContaBancaria com os seguintes atributos:
    **Nome do titular
    **Número da conta
    Saldo inicial (começa em 0)

    Implemente os seguintes métodos na classe:
    depositar(valor): Adiciona o valor ao saldo da conta.
    sacar(valor): Reduz o saldo da conta, mas só se houver saldo suficiente.
    consultar_saldo(): Exibe o saldo da conta.

No programa principal:
Crie pelo menos duas contas bancárias.
Realize depósitos, saques e consulte os saldos das contas.

## 3 : Sistema de Gestão de Personagens em um RPG

Você foi contratado por uma desenvolvedora indie para criar um sistema básico de gestão de personagens para um jogo de RPG. Seu desafio é desenvolver um programa em Python que utilize classes e métodos para representar personagens com atributos e ações específicas.

Requisitos:

    Crie uma classe chamada Personagem com os seguintes atributos:
    Nome
    Classe (ex: Guerreiro, Mago, Arqueiro)
    Vida (valor inicial: 100)
    Ataque
    Defesa

    Implemente os seguintes métodos na classe:

    atacar(outro_personagem): Reduz a vida do outro personagem com base no ataque do atacante e na defesa do alvo.
    defender(): Aumenta temporariamente a defesa do personagem.
    exibir_status(): Mostra as informações do personagem na tela.

Crie pelo menos dois personagens e simule um combate entre eles, utilizando os métodos implementados.

## 4 : Sistema de Biblioteca Digital

Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca digital usando POO (Programação Orientada a Objetos) em Python. O sistema deve permitir cadastrar livros, emprestar e devolver exemplares.

Requisitos:

    Crie uma classe Livro com os seguintes atributos:

    Título
    Autor
    Ano de publicação
    Disponível (True/False)

    Implemente os seguintes métodos na classe
    Livro:
    emprestar(): Define o livro como indisponível se ele estiver disponível.
    devolver(): Define o livro como disponível novamente.
    exibir_detalhes(): Exibe as informações do livro.

    Crie uma classe Biblioteca com os seguintes atributos e métodos:
    Atributo: Lista de livros cadastrados.

    Métodos:
    adicionar_livro(livro): Adiciona um livro à biblioteca.
    listar_livros_disponiveis(): Exibe todos os livros disponíveis para empréstimo.

No programa principal, crie pelo menos três livros, adicione-os à biblioteca e simule o empréstimo e a devolução de um deles.
