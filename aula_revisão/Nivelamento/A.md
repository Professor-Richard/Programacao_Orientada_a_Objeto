Lista
Uma lista é uma sequencia ordenada pelo índice, de zero ou mais referências a objetos.

Características: _ É uma estrutura de dado recursiva _ Representada por uma sequência, fechada por colchetes ( [** e **]) _ O primeiro elemento esta na posição zero _ Lista são mutáveis, podem receber novos elementos, substituir ou remover antigos elementos

Exemplo:

#Declarando uma lista:
salada = []

#Incluindo valores:
salada = ["manda", "pera", "uva"]

Operações básicas para manipulação de listas:

Operações de inclusão de novos elementos:
apend( novoElemento ): anexa um novoElemento no final da lista
insert( pos,novoElemento ): insere o novoElemento) na posição pos\* da lista, caso essa posição não exista, será criada

Exemplo:

#Incluindo valores:
salada = ["manda", "pera", "uva"]
print(salada)

salada.append("banana")
print(salada)

salada.insert(2,"goiaba")
print(salada)

## ['manda', 'pera', 'uva']

## ['manda', 'pera', 'uva', 'banana']

## ['manda', 'pera', 'goiaba', 'uva', 'banana']

Criando uma lista de numeros aleatórios em um intervalo pre estabelecido pelo usuário:
#Exemplo 1

#subprogramas
def preencher(listaElems, qtd, min, max):
from random import randint #Requer pacote com funcao externa
for item in range(qtd):
listaElems.append(randint(min, max))
return None

#programa principal
qtdNumeros = int(input("A Lista deve ter quantos valores?"))
minimo = int(input("Menor valor da faixa:"))
maximo = int(input("Maior valor da faixa:"))
numeros = []
preencher(numeros, qtdNumeros, minimo, maximo)
print(numeros)

Operações de exclusão: de novos elementos:
pop( ): retorna e remove o último elemento da lista.
pop( pos ): retorna e remove o elemento na posição pos da lista.
remove( x ): remove a primeira ocorrência do item x.
Outras operações úteis com listas:
les( ): retorna o comprimento da lista.
lista.count( elemento ): retorna quantas vezes o elemento aparece na lista
lista.sort( lista ): ordena o conteúdo da lista

Fatiamento de Listas
Fatiamento de Listas:
listaAntiga[posInicio : posFim *]\*: retorna uma nova lista composta de referências para elementos existentes na listAntiga
Exemplo:

saladaComposta = ["banana", "caju", "uva", "pera", "manga", "kiwi"]
print(saladaComposta)
saladaSimples = saladaComposta[1:4]
print(saladaSimples)

## ['banana', 'caju', 'uva', 'pera', 'manga', 'kiwi']

## ['caju', 'uva', 'pera']
