# Aula 5 – Encapsulamento (Proteção e Controle de Estado)

# 1. Introdução ao Controle de Acesso em Python

Encapsulamento é o princípio que determina que os dados internos de um objeto devem ser protegidos contra acesso direto indevido.

Ele garante:

- Integridade dos dados
- Segurança
- Controle de regras de negócio

Sem encapsulamento, qualquer parte do sistema poderia alterar dados de forma inconsistente.

Diferente de linguagens como Java e C++, Python **não possui modificadores de acesso formais** (`public`, `private`, `protected`).

Em vez disso, utiliza **convenções de nomenclatura** para indicar o nível de acesso:

- Público → acesso livre
- Protegido → \_ uso interno (convenção)
- Privado → \_\_ restrição com _name mangling_

## 1.2. Problema Sem Encapsulamento

### UML de exemplo da classe Conta

```text
Conta
--------------------
nome
saldo
--------------------
conta(nome,saldo)
mostrar_saldo()
alterar_saldo(valor)
```

### Classe

```python
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
```

### Nada impede:

```python
conta.saldo = + 1.000.000
```

Isso quebra a regra do domínio.

## 1.3. Encapsulamento em Python

### Python utiliza convenção:

- Público → atributo
- Protegido → \_atributo
- Privado → \_\_atributo

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo
```

## 1.4. Conceito de Interface Pública

A interface pública define como o objeto pode ser utilizado.

O usuário da classe não precisa saber como o saldo é armazenado, apenas como interagir com ele.

## 1.5. Benefícios na Engenharia de Software

- Reduz acoplamento
- Facilita manutenção
- Permite evolução interna sem quebrar código externo

# 2. Getter e Setter em Python

Em Python, getters e setters são métodos utilizados para acessar e modificar atributos privados de uma classe. O uso desses métodos ajuda a proteger os dados e garantir que regras de validação sejam aplicadas antes de modificar um valor.

## Criando Getters e Setters

### Usando Métodos Convencionais

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

```

### Usando `property`

O decorador `property` pode ser usado para criar propriedades de maneira mais elegante.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string")
```

## Vantagens do Uso de Getters e Setters

- Encapsulamento de dados
- Controle de acesso
- Validação antes da atribuição de valores
- Flexibilidade para modificar a implementação sem afetar o código que usa a classe

## 6. Exercício
