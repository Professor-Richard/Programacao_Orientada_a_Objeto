# Road Map das aulas

### Aula 1. Classe

Uma classe é um modelo para criar objetos. Define os atributos e métodos que os objetos daquela classe terão.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

### Aula 2. Objeto

Um objeto é uma instância de uma classe.

```python
pessoa1 = Pessoa("Alice", 25)
pessoa1.apresentar()
```

### Aula 3. Encapsulamento

O encapsulamento protege os dados dentro de uma classe, permitindo acesso controlado a eles.

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def get_saldo(self):
        return self.__saldo
```

### Aula 4. Herança

Herança permite que uma classe herde atributos e métodos de outra classe.

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
```

### Aula 5. Polimorfismo

Polimorfismo permite que métodos com o mesmo nome tenham comportamentos diferentes dependendo da classe que os implementa.

```python
class Cachorro:
    def falar(self):
        return "Au Au!"

class Gato:
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.falar())
```
