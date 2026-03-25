# Pratica de dicionario

    dicionario.keys() → chaves
    dicionario.values() → valores
    dicionario.items() → chave + valor

## Criando Dicionario

```python
dicionario = {
'nome': 'Richard',
'idade': 35,
'cidade': 'Tres Lagoas'
}
```

## Acessando um valor

print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['cidade'])

## Alterando um valor

dicionario['idade'] = 36

## Adicionando um valor

dicionario['estado'] = 'MS'

## Removendo um item

del dicionario['cidade']

# Percorrendo o Discionario

## Só as chaves

for chaves in dicionario:
print(chaves)

## Chave e valor

for c, k in dicionario.items():
print(f'C: {c}, K: {k}')

print(dicionario)
