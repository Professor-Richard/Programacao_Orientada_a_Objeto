## Aula 3 – Abstração (Modelagem Essencial do Problema)

# 1. Fundamentação Teórica

    Abstração é o processo de identificar características essenciais de um objeto, ignorando detalhes irrelevantes.

    Ela responde:

    O que o objeto deve fazer?

    Não responde:

    Como ele faz internamente?

# 2. Abstração na Modelagem

    Exemplo: Sistema bancário

    ContaBancaria deve:

    Depositar

    Sacar

    Consultar saldo

    Não importa para o usuário:

    Como os dados são armazenados

    Se usa banco SQL ou memória

# 3. Classes Abstratas

São modelos que não podem ser instanciados diretamente.

```python
from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass
```

Isso cria um contrato:

Toda subclasse deve implementar calcular_area.

# 4. Papel na Arquitetura

    Abstração:

    Define contratos

    Permite extensibilidade

    Base para sistemas grandes

    É essencial para aplicar princípios SOLID posteriormente.

# 5. Discussão Avançada

    Diferença entre:

    Classe abstrata

    Interface (conceito geral)

    Implementação concreta

# 6. Exercício

    Por que não devemos colocar lógica de implementação dentro de classes abstratas quando o objetivo é definir contrato?
