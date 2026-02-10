# Nivelamento LISTA

## Listas

    Listas são estruturas de dados capazes de armazenar múltiplos elementos.

## Declaração

    Para a criação de uma lista, basta colocar os elementos separados por vírgulas dentro de colchetes [], como no exemplo abaixo:

```python
nomes_frutas = ["maçã", "banana", "abacaxi"]
print(nomes_frutas) #['maçã', 'banana', 'abacaxi']

numeros = [2, 13, 17, 47]
print(numeros) #[2, 13, 17, 47]
```

A lista pode conter elementos de tipos diferentes:

    vazia = []
    ['texto', 150, 1.3, [-1, -2]]

## Índices

Assim como nas strings, é possível acessar separadamente cada item de uma lista a partir de seu índice:

```python
# Definindo a lista com cinco elementos
lista = [100, 200, 300, 400, 500]
# Acessando o primeiro elemento, que está no índice 0
print(lista[0])  # 100
# Acessando o último elemento, que está no índice 4
print(lista[4])  # 500
# Acessando o último elemento usando índice negativo
print(lista[-1])  # 500
```

Conforme visto anteriormente, ao utilizar um índice negativo os elementos são acessados de trás pra frente, a partir do final da lista.

Ou pode-se acessar através de slices (fatias), como nas strings:

```python
  # Lista de números
lista = [100, 200, 300, 400, 500]
# Fatiamento da lista da posição 2 até a 4 (não inclusa)
print(lista[2:4])  # [300, 400]
# Fatiamento da lista até a posição 3 (não inclusa)
print(lista[:3])  # [100, 200, 300]
# Fatiamento da lista da posição 2 até o final
print(lista[2:])  # [300, 400, 500]
# Fatiamento da lista do começo até o final
print(lista[:])  # [100, 200, 300, 400, 500]
```

### Podemos avaliar se os elementos estão na lista com a palavra in:

```python
# Definindo a lista com diversos elementos
lista_estranha = ['duas palavras', 42, True, ['batman', 'robin'], -0.84, 'hipófise']
# Verificando se o número 42 está na lista
print(42 in lista_estranha)  # True
# Verificando se a string 'duas palavras' está na lista
print('duas palavras' in lista_estranha)  # True
# Verificando se a string 'dominó' está na lista
print('dominó' in lista_estranha)  # False
# Verificando se o elemento 'batman' está na lista interna (índice 3)
print('batman' in lista_estranha[3])  # True
```

É possível obter o tamanho da lista utilizando o método len():

```python
# Lista de números
lista = [100, 200, 300, 400, 500]
# Obtendo o tamanho da lista
print(len(lista))  # 5
# Lista com elementos variados
lista_estranha = ['duas palavras', 42, True, ['batman', 'robin'], -0.84, 'hipófise']
# Obtendo o tamanho da lista estranha
print(len(lista_estranha))  # 6
# Obtendo o tamanho do subelemento na posição 3 da lista estranha (que é uma lista)
print(len(lista_estranha[3]))  # 2
```

## Removendo itens da lista

Devido à lista ser uma estrutura mutável, é possível remover seus elementos utilizando o comando del:

```python
# Lista inicial
lista_estranha = ['duas palavras', 42, True, ['batman', 'robin'], -0.84, 'hipófise']
# Removendo o elemento na posição 2 (índice 2)
del lista_estranha[2]
# Imprimindo a lista após remoção
print(lista_estranha)  # ['duas palavras', 42, ['batman', 'robin'], -0.84, 'hipófise']
# Removendo o último elemento da lista
del lista_estranha[-1]
# Imprimindo a lista após remoção do último elemento
print(lista_estranha)  # ['duas palavras', 42, ['batman', 'robin'], -0.84]
```

## Trabalhando com listas

O operador + concatena listas:

```python
# Definindo duas listas
a = [1, 2, 3]
b = [4, 5, 6]
# Concatenando as listas
c = a + b
# Imprimindo o resultado da concatenação
print(c)  # [1, 2, 3, 4, 5, 6]
```

O operador \* repete a lista dado um número de vezes:

```python
# Multiplicando a lista [0] por 3
print([0] * 3)  # [0, 0, 0]
# Multiplicando a lista [1, 2, 3] por 2
print([1, 2, 3] * 2)  # [1, 2, 3, 1, 2, 3]

```

O método append() adiciona um elemento ao final da lista:

```python
# Definindo a lista inicial
lista = ['a', 'b', 'c']
# Imprimindo a lista original
print(lista)  # ['a', 'b', 'c']
# Adicionando o elemento 'e' ao final da lista
lista.append('e')
# Imprimindo a lista após o append
print(lista)  # ['a', 'b', 'c', 'e']
```

Temos também o insert(), que insere um elemento na posição especificada e move os demais elementos para direita:

```python
# Lista inicial
lista = ['a', 'b', 'c', 'e']
# Usando insert() para adicionar o elemento 'd' na posição 3
lista.insert(3, 'd')
# Imprimindo a lista após o insert
print(lista)  # ['a', 'b', 'c', 'd', 'e']
```

Aviso

Cuidado com lista.insert(-1, algo)! Nesse caso, inserimos algo na posição -1 e o elemento que estava previamente na posição -1 é movido para a direita:

```python
# Lista inicial
lista = ['a', 'b', 'c', 'd', 'e']
# Usando insert() para adicionar o elemento 'ç' antes do último elemento
lista.insert(-1, 'ç')
# Imprimindo a lista após o insert
print(lista)  # ['a', 'b', 'c', 'd', 'ç', 'e']
```

Use append() caso queira algo adicionado ao final da lista.

extend() recebe uma lista como argumento e adiciona todos seus elementos a outra:

```python
# Definindo as duas listas
lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e']
# Imprimindo as listas antes do extend
print(lista1)  # ['a', 'b', 'c']
print(lista2)  # ['d', 'e']
# Usando extend() para adicionar os elementos de lista2 em lista1
lista1.extend(lista2)
# Imprimindo a lista1 após o extend
print(lista1)  # ['a', 'b', 'c', 'd', 'e']
```

lista2 não é modificado:

```python
print(lista2)  # ['d', 'e']
```

O método sort() ordena os elementos da lista em ordem ascendente:

```python
# Lista desordenada
lista_desordenada = ['b', 'z', 'k', 'a', 'h']
# Ordenando a lista em ordem crescente
lista_desordenada.sort()
# Imprimindo a lista após a ordenação
print(lista_desordenada)  # ['a', 'b', 'h', 'k', 'z']
```

Para fazer uma cópia de uma lista, devemos usar o método copy():

```python
# Lista original
lista1 = ['a', 'b', 'c']
# Criando uma cópia da lista1
lista2 = lista1.copy()
# Imprimindo as listas antes de qualquer modificação
print(lista1)  # ['a', 'b', 'c']
print(lista2)  # ['a', 'b', 'c']
# Adicionando o elemento 'd' na lista2
lista2.append('d')
# Imprimindo as listas após a modificação na lista2
print(lista1)  # ['a', 'b', 'c']  # lista1 permanece inalterada
print(lista2)  # ['a', 'b', 'c', 'd']  # lista2 foi modificada
```

Se não usarmos o copy(), acontece algo bem estranho:

```python
# Lista original
lista1 = ['a', 'b', 'c']
# Criando uma referência para lista1, ou seja, lista2 aponta para a mesma lista
lista2 = lista1
# Imprimindo as listas antes de qualquer modificação
print(lista1)  # ['a', 'b', 'c']
print(lista2)  # ['a', 'b', 'c']
# Adicionando o elemento 'd' na lista2
lista2.append('d')
# Imprimindo as listas após a modificação na lista2
print(lista1)  # ['a', 'b', 'c', 'd']  # lista1 é modificada, pois lista2 é apenas uma referência
print(lista2)  # ['a', 'b', 'c', 'd']  # lista2 também reflete a modificação
```

Tudo o que for feito com lista2 nesse exemplo também altera lista1 e vice-versa.
