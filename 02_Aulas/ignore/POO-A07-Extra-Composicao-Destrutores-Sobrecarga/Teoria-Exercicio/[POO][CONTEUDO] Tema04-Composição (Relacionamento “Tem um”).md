# Tema 04 – Relacionamentos e Pilares da POO  
## Aula – Composição (Relacionamento “Tem um”)

---

## 1. Fundamentação Teórica

Composição é um mecanismo de reutilização baseado em **relacionamento entre objetos**.

Enquanto a herança modela:

> **“É um tipo de”**

A composição modela:

> **“Tem um”**

Exemplos:

- Um **Carro tem um Motor**
- Um **Pedido tem uma Lista de Itens**
- Um **Personagem tem uma Arma**
- Um **Computador tem um Processador**

Na composição, uma classe utiliza outra como parte de sua estrutura interna.

---

## 2. Por que Composição é Importante?

A herança cria dependência estrutural forte.

A composição cria dependência comportamental mais flexível.

Um princípio amplamente adotado em Engenharia de Software é:

> **Prefira composição à herança.**

### Motivos:

- Menor acoplamento
- Maior flexibilidade
- Evita hierarquias rígidas
- Facilita manutenção
- Permite trocar comportamentos em tempo de execução

---

## 3. Estrutura da Composição

A composição ocorre quando um objeto recebe outro objeto como atributo.

### Exemplo 1 – Estrutura Básica

```python
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self):
        self.motor = Motor()  # Carro TEM um Motor

    def ligar(self):
        return self.motor.ligar()
```

Uso:

```python
carro = Carro()
print(carro.ligar())
```

Observe:

- `Carro` não herda de `Motor`
- `Carro` utiliza `Motor`
- O comportamento é delegado

---

## 4. Delegação de Responsabilidade

Composição normalmente envolve **delegação**.

A classe principal delega parte do comportamento para outro objeto.

```python
class Arma:
    def atacar(self):
        return "Ataque básico"

class Personagem:
    def __init__(self, arma):
        self.arma = arma

    def atacar(self):
        return self.arma.atacar()
```

Agora podemos trocar a arma sem alterar a classe `Personagem`.

```python
class Espada:
    def atacar(self):
        return "Corte com espada"

class Arco:
    def atacar(self):
        return "Disparo de flecha"

p1 = Personagem(Espada())
p2 = Personagem(Arco())

print(p1.atacar())
print(p2.atacar())
```

Aqui vemos flexibilidade estrutural.

---

## 5. Comparação: Herança vs Composição

| Herança | Composição |
|----------|------------|
| Relação “é um” | Relação “tem um” |
| Cria hierarquia | Cria estrutura modular |
| Acoplamento mais forte | Acoplamento mais fraco |
| Reutilização estrutural | Reutilização comportamental |
| Difícil alterar em runtime | Fácil alterar em runtime |

---

## 6. Quando Usar Composição?

Use composição quando:

- Não houver relação clara de especialização
- Você quiser flexibilidade
- Desejar trocar comportamentos dinamicamente
- Evitar hierarquias profundas
- Modelar partes de um sistema

Evite herança apenas para reaproveitar código.

---

## 7. Composição Forte vs Agregação

### Composição Forte

O objeto interno depende totalmente do objeto principal.

Exemplo:

```python
class Casa:
    def __init__(self):
        self.porta = Porta()
```

Se a casa deixa de existir, a porta também.

---

### Agregação

O objeto pode existir independentemente.

```python
class Professor:
    def __init__(self, nome):
        self.nome = nome

class Escola:
    def __init__(self, professor):
        self.professor = professor
```

Aqui o professor pode existir fora da escola.

---

## 8. Impacto Arquitetural

Composição permite:

- Sistemas extensíveis
- Baixo acoplamento
- Aplicação do princípio Open/Closed
- Melhor testabilidade
- Melhor separação de responsabilidades

É base de arquiteturas modernas como:

- Clean Architecture
- Domain-Driven Design
- Arquitetura orientada a serviços

---

## 9. Exercícios

### Exercício 1 – Sistema de Veículo

Crie:

- Classe `Motor`
- Classe `Carro` que possui um motor
- Permita trocar o motor após a criação

---

### Exercício 2 – Sistema de Jogo

Crie:

- Classe `Habilidade`
- Classe `Personagem` que recebe uma habilidade
- Permita que o personagem troque de habilidade

---

### Exercício 3 – Reflexão

Responda:

1. Por que composição gera menos acoplamento que herança?
2. Em que situação herança seria mais adequada?
3. Qual a diferença entre composição forte e agregação?

---

## 10. Síntese Conceitual

Composição é um dos mecanismos mais importantes da POO moderna.

Ela promove:

- Flexibilidade
- Manutenção simplificada
- Código modular
- Reutilização inteligente

Em projetos reais, composição tende a ser mais utilizada que herança.

---
