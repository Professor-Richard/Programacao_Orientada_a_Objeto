from classes.biblioteca import Biblioteca
from classes.livros import Livros


class Menu:

    def show():
        while True:
            print('-'*40)
            print(f'{"MENU DE CADASTRO":-^40}')
            print('-'*40)
            print('0 - Sair \n1 - Cadastrar usuario \n2- Cadastrar livro')
            opcao = int(input('Qual sua opção: '))
            if opcao == 1:
                return Biblioteca.cadastrar_usuario()
            elif opcao == 2:
                return Livros.cadastrar()
            else:
                print('Saindo do Menu... ')
                break
