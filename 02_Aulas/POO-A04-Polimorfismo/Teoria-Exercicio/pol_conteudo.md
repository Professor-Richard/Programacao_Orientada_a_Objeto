# Tema 04 – Relacionamentos e Pilares da POO

## Aula – Polimorfismo (Flexibilidade e Extensão de Comportamento)

---

## 1. Contextualização

Dentro dos pilares da Programação Orientada a Objetos (POO), **polimorfismo** é o mecanismo que permite que **objetos diferentes respondam à mesma operação (mensagem) de maneiras diferentes**.

Sem polimorfismo, sistemas tendem a crescer cheios de:

- `if`
- `elif`
- `switch`
- verificações de tipo (`isinstance()`)

Com polimorfismo, o sistema cresce de forma:

- **Aberta para extensão**
- **Fechada para modificação**

Isso se conecta diretamente com o Princípio **Open/Closed (OCP)** do SOLID.

---

## 2. O problema sem polimorfismo

Um exemplo comum é decidir comportamento por texto/tipo:

```python
def emitir_som(tipo: str) -> None:
    if tipo == "cachorro":
        print("Latido")
    elif tipo == "gato":
        print("Miau")
    else:
        print("Som desconhecido")
```

### Por que isso é ruim?

- **Alto acoplamento**: a função “conhece” todos os tipos.
- **Baixa escalabilidade**: cada novo tipo exige editar a função.
- **Manutenção difícil**: cresce com muitos ramos condicionais.
- **Viola OCP**: para adicionar um novo comportamento, você precisa _modificar_ o código existente.

---

## 3. Conceito de polimorfismo

**Polimorfismo** significa “muitas formas”.

Na prática, significa:

> **A mesma interface, comportamentos diferentes.**

Você chama o mesmo método (`emitir_som()`), mas cada objeto responde do seu jeito.

Três ideias-chave:

1. **Interface comum** (explícita ou implícita)
2. **Sobrescrita** (override) quando há herança
3. **Despacho dinâmico**: o Python decide em tempo de execução qual implementação chamar

---

## 4. Polimorfismo por sobrescrita (Override)

### 4.1 Classe base (contrato)

```python
class Animal:
    def emitir_som(self) -> str:
        raise NotImplementedError("Subclasse deve implementar emitir_som()")
```

### 4.2 Subclasses (implementações diferentes)

```python
class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "Latido"

class Gato(Animal):
    def emitir_som(self) -> str:
        return "Miau"
```

### 4.3 Uso polimórfico (sem `if`)

```python
def fazer_emitir(animal: Animal) -> None:
    print(animal.emitir_som())

animais = [Cachorro(), Gato()]

for a in animais:
    fazer_emitir(a)
```

### O que observar

- `fazer_emitir()` não precisa saber _qual_ animal é.
- A função só exige que exista o método `emitir_som()`.
- O comportamento varia conforme o objeto real passado.

Isso reduz acoplamento e melhora extensibilidade.

---

## 5. Duck Typing (polimorfismo implícito em Python)

Em Python, muitas vezes não é necessário herdar de uma classe base.

Se o objeto “tem o método esperado”, ele funciona.

```python
class Sirene:
    def emitir_som(self) -> str:
        return "Alarme!"

objetos = [Cachorro(), Gato(), Sirene()]

for obj in objetos:
    print(obj.emitir_som())
```

Isso é conhecido como **Duck Typing**:

> “Se anda como pato e faz quack, é pato.”

Observação didática: Duck typing é muito útil, mas exige **disciplina** (testes, nomes consistentes e contratos claros).

---

## 6. Exemplo de mundo real: sistema de pagamentos

### 6.1 Contrato

```python
class Pagamento:
    def processar(self, valor: float) -> str:
        raise NotImplementedError("Subclasse deve implementar processar()")
```

### 6.2 Formas de pagamento

```python
class Cartao(Pagamento):
    def processar(self, valor: float) -> str:
        return f"Pagamento de R$ {valor:.2f} no cartão"

class Pix(Pagamento):
    def processar(self, valor: float) -> str:
        return f"Pagamento de R$ {valor:.2f} via PIX"
```

### 6.3 Código principal (não muda)

```python
def finalizar_pagamento(pagamento: Pagamento, valor: float) -> None:
    print(pagamento.processar(valor))

finalizar_pagamento(Cartao(), 120.0)
finalizar_pagamento(Pix(), 120.0)
```

Para adicionar `Boleto`, você cria `class Boleto(Pagamento)` e pronto.  
Você **não altera** `finalizar_pagamento()`.

---

## 7. Relação com os outros pilares

| Pilar          | Relação com Polimorfismo                                           |
| -------------- | ------------------------------------------------------------------ |
| Encapsulamento | Esconde detalhes; você usa a interface, não a implementação        |
| Herança        | Facilita definir uma interface comum e sobrescrever comportamentos |
| Abstração      | Define o “contrato” que as classes concretas devem cumprir         |
| Composição     | Pode gerar polimorfismo sem herança (estratégias, plugins)         |

---

## 8. Quando NÃO usar polimorfismo

Evite quando:

- Não existe variação real de comportamento
- A hierarquia é forçada (“só para usar herança”)
- Você está tentando apenas reaproveitar código (prefira composição)
- O domínio é simples e uma função direta resolve melhor

Polimorfismo é ferramenta para **extensão e flexibilidade**, não enfeite.

---

## 9. Erros comuns

- Confundir polimorfismo com “ter muitas classes”
- Usar `if isinstance()` como padrão (quebra OCP)
- Criar hierarquias profundas e frágeis
- Não deixar claro o contrato do método base
- Não garantir substituição correta (ideia do **LSP**)

---
