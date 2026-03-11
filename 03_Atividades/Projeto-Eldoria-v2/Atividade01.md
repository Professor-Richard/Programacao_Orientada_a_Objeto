# Exercício – Modelagem de Entidades em um RPG (POO em Python)

## Parte 1 – Classe Base

Crie um arquivo chamado `entidade.py` contendo uma classe `Entidade`.

### Atributos:

- nome (str)
- poder (int)
- defesa (int)
- vida_maxima (int)
- vida_atual (int) → deve iniciar com o valor de vida_maxima
- esquiva (int)

### Métodos:

- `esta_vivo()` → retorna True se vida_atual > 0
- `receber_dano(dano)` → reduz a vida sem permitir valores negativos
- `curar(valor)` → aumenta a vida sem ultrapassar vida_maxima

No final do arquivo, crie um objeto para testar os métodos.

---

## Parte 2 – Herança

Crie um arquivo `jogador.py`.

Implemente uma classe `Jogador` que herde de `Entidade`.

### Atributos adicionais:

- nivel (inicia em 1)
- experiencia (inicia em 0)
- inventario (lista vazia)
- raca (str)
- vocacao (str)

Utilize `super()` para inicializar os atributos herdados.

---

## Objetivo

Demonstrar:

- Criação de classes
- Uso de construtor
- Manipulação de atributos
- Herança
- Uso de `super()`
- Organização em múltiplos arquivos
