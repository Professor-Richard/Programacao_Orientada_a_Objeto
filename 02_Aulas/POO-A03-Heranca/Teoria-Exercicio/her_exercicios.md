# Exercícios

## Exercício 1: Criando uma Hierarquia de Veículos

Crie uma classe **Veiculo** com os atributos `marca` e `ano`. Em seguida, crie as subclasses **Carro** e **Moto**, que herdam de `Veiculo`. Ambas devem ter um método `info()` que exibe as informações do veículo.

## Exercício 2: Herança Multinível

Crie uma classe **Funcionario** com os atributos `nome` e `salario`. Depois, crie uma subclasse **Gerente**, que adiciona um atributo `departamento`. Por fim, crie uma subclasse **Diretor**, que tem um atributo `bonus`.

## Exercício 3: Reescrevendo Métodos

Crie uma classe **InstrumentoMusical** com um método `tocar()`. Depois, crie as subclasses **Guitarra** e **Bateria**, sobrescrevendo o método `tocar()` para exibir uma mensagem diferente para cada instrumento.

## Exercício 4: Reescrevendo Métodos

Você foi contratado para desenvolver um módulo de pagamentos de um e-commerce que deve integrar múltiplos gateways (PayPal, Stripe, Mercado Pago). Cada gateway tem regras distintas:

- O PayPal cobra uma taxa fixa de 2% por transação.
- O Stripe permite estorno total apenas em até 7 dias.
- O Mercado Pago exige um token de segurança e limita transações a R$ 10.000.

## Exercício 5: Desafio

1. Projete classes para cada gateway usando herança e polimorfismo, garantindo que novos gateways sejam adicionados sem modificar o código existente.
2. Implemente um método abstrato `processar_pagamento(valor)` que retorne o ID da transação, custo de processamento e status.
3. Adicione exceções personalizadas para:
   - Valores excedentes (transações acima de R$ 10.000 no Mercado Pago).
   - Tokens inválidos (Mercado Pago).
   - Estornos fora do prazo (Stripe).
