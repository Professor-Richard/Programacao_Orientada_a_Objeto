## Atividade prática (guiada)

### Objetivo

Aplicar polimorfismo para calcular áreas **sem condicionais**.

### Parte 1 — Modelagem

Crie uma classe base `Forma` com método `calcular_area()`.

Crie subclasses:

- `Quadrado`
- `Retangulo`
- `Circulo`

Exemplo de assinatura:

```python
import math

class Forma:
    def calcular_area(self) -> float:
        raise NotImplementedError

class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

class Retangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)
```

### Parte 2 — Uso polimórfico

Crie uma lista de formas e percorra chamando `calcular_area()`:

```python
formas = [
    Quadrado(4),
    Retangulo(3, 5),
    Circulo(2)
]

for f in formas:
    print(type(f).__name__, "->", f.calcular_area())
```

Regra: **não usar `if` para descobrir qual forma é**.

---
