# Relacionamentos e Pilares da POO

## Aula – Herança (Relação “É um”)

---

## 1. Fundamentação Conceitual

Herança é o mecanismo que permite a criação de novas classes a partir de classes existentes, aproveitando e especializando comportamentos já definidos. A classe que herda é chamada de **subclasse**, e a classe base é chamada de **superclasse**.
**Vantagens da herança:**

- Reutilização de código.
- Facilidade de manutenção.
- Melhor organização do código.

**Riscos da Herança**

- Herança excessiva
- Hierarquias complexas
- Violação do princípio da substituição (LSP)

**Quando Usar Herança?**

- Use quando houver relação clara de especialização.
- Evite quando for apenas reutilização de código — nesse caso, prefira composição.

Ela modela a relação:

> “É um tipo de”

Exemplos:

- Cachorro é um tipo de Animal
- Gerente é um tipo de Funcionário
- Aluno é uma Pessoa

---

## 2. Objetivos da Herança

A herança existe para:

- Reutilização estrutural
- Especialização de comportamento
- Extensão controlada
- Organização hierárquica
- Modelagem do mundo real

---

## 2. Exemplo de Herança em Python

### Criando a Superclasse

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
```

### Criando a Subclasse

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # Chamada ao construtor da superclasse
        self.curso = curso

    def apresentar(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}."
```

### Usando as Classes

```python
pessoa = Pessoa("Carlos", 40)
print(pessoa.apresentar())  # Meu nome é Carlos e tenho 40 anos.

estudante = Estudante("Ana", 20, "Engenharia")
print(estudante.apresentar())  # Meu nome é Ana, tenho 20 anos e estudo Engenharia.
```

---

## 3. Tipos de Herança

### 3.1. Herança Simples

Uma classe herda diretamente de uma outra classe.

```python
class Animal:
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
```

### 3.2. Herança Múltipla

Uma classe pode herdar de múltiplas classes.
Python resolve conflitos usando MRO (Method Resolution Order).**Deve ser utilizada com cautela.**

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

### 3.3. Herança Multinível

Uma classe herda de outra, que já herdou de uma terceira classe.

```python
class Veiculo:
    pass

class Carro(Veiculo):
    pass

class Esportivo(Carro):
    pass
```

---

Utilizando super()
Quando a subclasse precisa reutilizar o construtor da superclasse:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
```

## Sem o uso de super(), os atributos herdados não seriam inicializados corretamente.

4. Sobrescrita de Métodos (Override)

Sobrescrita permite redefinir um comportamento herdado.

```python
class Funcionario:
    def calcular_bonus(self):
        return 500

class Gerente(Funcionario):
    def calcular_bonus(self):
        return 2000
```

8. Quando Não Usar Herança

Evite herança quando:

Não houver relação clara de especialização

A intenção for apenas reaproveitar código

A hierarquia começar a ficar complexa demais

## Nesses casos, prefira composição.

9. Comparação: Herança vs Composição

| Critério             | Herança  | Composição |
| -------------------- | -------- | ---------- |
| Relação              | É um     | Tem um     |
| Acoplamento          | Alto     | Baixo      |
| Flexibilidade        | Média    | Alta       |
| Recomendação moderna | Moderada | Preferida  |

---
