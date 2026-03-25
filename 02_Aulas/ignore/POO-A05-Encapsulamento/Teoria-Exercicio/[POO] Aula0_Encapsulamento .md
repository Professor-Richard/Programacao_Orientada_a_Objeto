# Aula 2 – Encapsulamento (Proteção e Controle de Estado)

## 1. Fundamentação Teórica

    Encapsulamento é o princípio que determina que os dados internos de um objeto devem ser protegidos contra acesso direto indevido.

    Ele garante:

    Integridade dos dados

    Segurança

    Controle de regras de negócio

    Sem encapsulamento, qualquer parte do sistema poderia alterar dados de forma inconsistente.

## 2. Problema Sem Encapsulamento

```python
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
```

Nada impede:

```python
conta.saldo = -999999
```

Isso quebra a regra do domínio.

## 3. Encapsulamento em Python

Python utiliza convenção:

Público → atributo

Protegido → \_atributo

Privado → \_\_atributo

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

## 4. Conceito de Interface Pública

    A interface pública define como o objeto pode ser utilizado.

    O usuário da classe não precisa saber como o saldo é armazenado, apenas como interagir com ele.

## 5. Benefícios na Engenharia de Software

    Reduz acoplamento

    Facilita manutenção

    Permite evolução interna sem quebrar código externo

## 6. Exercício

    Qual o risco de deixar atributos críticos públicos?

    Encapsulamento é apenas esconder dados?
