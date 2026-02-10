# Plano de Aula: Introdução à Orientação a Objetos

1. ## Introdução Teórica

    O que é Programação Orientada a Objetos (POO)?
    É um Paradigma de programação baseado em "objetos".
    Objetos são instâncias de classes que encapsulam dados (atributos) e comportamentos (métodos).

### Conceitos básicos:

    Classe: Modelo ou blueprint para criar objetos.
    Objeto: Instância de uma classe.
    Encapsulamento: Proteção dos dados internos de um objeto.

### Comparação entre programação procedural e orientada a objetos.

    Programação Procedural:
    Foco em funções e sequência de passos.
    Dados e funções são separados.
    Ideal para tarefas simples e scripts pequenos.
    Exemplo: C, Pascal.

### Programação Orientada a Objetos (POO):

    Foco em objetos (combinação de dados e comportamentos).
    Organiza o código em classes e objetos.
    Ideal para projetos grandes e complexos.
    Exemplo: Java, Python, C++.

### Diferença Chave:

    Procedural: "O que fazer" (funções).
    POO: "Quem faz o quê" (objetos).

---

2. ## Diferença entre Classe e Objeto

    Classe como um molde (exemplo: "Receita de bolo").
    Objeto como uma instância específica (exemplo: "Bolo de chocolate").
    Exemplo em Python:

### Definição de uma classe

```python
class Carro:
pass
```

### Instanciação de objetos

```python
fusca = Carro()
civic = Carro()
```

## Discussão: O que FUSCA e CIVIC têm em comum? O que os diferencia?

---

3. ## Atributos e Métodos

## Atributos: São Variáveis que pertencem a uma classe ou objeto.

    Exemplo: cor, modelo, ano para a classe Carro.

## Métodos: São Funções que pertencem a uma classe ou objeto.

    Exemplo: ligar(), acelerar(), frear() para a classe Carro.
    Exemplo em Python:

```python
class Carro: # Atributos
def **init**(self, cor, modelo, ano):
self.cor = cor
self.modelo = modelo
self.ano = ano
```

## Métodos

```python
def ligar(self):
    return f"{self.modelo} está ligado!"

def acelerar(self):
    return f"{self.modelo} está acelerando."
```

## Instanciação e uso:

```python
fusca = Carro("Azul", "Fusca", 1970)
print(fusca.ligar()) # Saída: Fusca está ligado!
print(fusca.acelerar()) # Saída: Fusca está acelerando.
```

---

4. # Criação de Classes e Instanciação de Objetos

## Prática:

    Crie uma classe Pessoa com atributos: nome, idade, cpf.
    Adicione métodos: falar(), andar().
    Instancie objetos e teste os métodos.

## Exemplo:

```python
class Pessoa:
def **init**(self, nome, idade, cpf):
self.nome = nome
self.idade = idade
self.cpf = cpf

def falar(self, mensagem):
    return f"{self.nome} diz: {mensagem}"

def andar(self):
    return f"{self.nome} está andando."
```

## Teste:

```python
joao = Pessoa("João", 25, "123.456.789-00")
print(joao.falar("Olá, mundo!"))
print(joao.andar())
```

## Saida

> João diz: Olá, mundo!
>
> Saída: João está andando.

---

5. # Exemplos Práticos: Modelagem de Problemas do Mundo Real
   Conteúdo:
   Modelagem de problemas simples usando POO.
   Exemplos:
   Classe ContaBancaria:
   Atributos: numero_conta, saldo, titular.
   Métodos: depositar(), sacar(), consultar_saldo().
   Classe Animal:
   Atributos: nome, especie, idade.
   Métodos: comer(), dormir(), emitir_som().
   Atividade em grupo:
   Divida a turma em grupos e peça para cada grupo criar uma classe para um problema específico (ex: Produto, Livro, Aluno).
   Apresentação rápida dos modelos criados.

---

Exercícios Práticos:
Crie uma classe Círculo com atributos raio e métodos para calcular área e perímetro.
Modele uma classe Retângulo com atributos largura e altura e métodos para calcular área e perímetro.

Desafio: Crie uma classe Contato para uma agenda telefônica, com atributos nome, telefone e email, e métodos para exibir informações.
