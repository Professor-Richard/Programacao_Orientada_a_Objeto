# Getter e Setter em Python

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
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string")
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
