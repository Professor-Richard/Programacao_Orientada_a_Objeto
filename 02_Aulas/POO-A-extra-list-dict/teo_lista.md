# Teoria de lista

    lista[0] → acessa pelo índice
    lista.append() → adiciona no final
    lista.insert() → adiciona em posição específica
    lista.remove() → remove pelo valor
    lista.pop() → remove pelo índice
    lista.sort() → ordena a lista
    len(lista) → retorna o tamanho

## Criando Lista

```python
lista = ['Richard', 'Ana', 'Carlos', 'Beatriz']
```

## Acessando um valor pelo índice

    int(lista[0]) # primeiro elemento
    print(lista[-1]) # último elemento

## Alterando um valor

lista[0] = 'Roberto'

## Adicionando um valor no final

lista.append('Fernando')

## Adicionando em posição específica

lista.insert(1, 'Mariana') # insere na posição 1

## Removendo pelo valor

lista.remove('Carlos')

## Removendo pelo índice

lista.pop(0) # remove o primeiro elemento

## Tamanho da lista

print(len(lista))

# Percorrendo a lista

## Só os valores

    for nome in lista:
    print(nome)

# Valor e índice

    for i, nome in enumerate(lista):
    print(f'Índice: {i}, Valor: {nome}')

# Verificando se um valor existe na lista

    if 'Ana' in lista:
    print('Ana está na lista')

# Ordenando a lista

    lista.sort()
    print(lista)

# Fatiamento (slice)

    print(lista[0:2]) # do índice 0 até 1
    print(lista[1:]) # do índice 1 até o final
    print(lista[:3]) # do início até o índice 2

    print(lista)
