from random import randint


class SistemaDados:

    def d6():
        return randint(0, 6)

    def d20():
        return randint(0, 20)


var = SistemaDados.d20()
while True:
    num = int(input('Digite um numero entre 0 á 20: '))
    if var > num:
        print("Entre com um numero Maior: ")
    elif var < num:
        print("Entre com um numero Menor: ")
    else:
        print('Você Acertou Mizeravi!!!')
        saida = str(input('Você deseja continuar? s/n'))
        if saida in 'SsnN':
            var = SistemaDados.d20()
            if saida in 'Nn':
                break
        else:
            print('Erro! Valor invalido, tente novamente: ')
