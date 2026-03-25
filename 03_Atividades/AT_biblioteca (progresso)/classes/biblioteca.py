# BLIBLIOTECA
# obj biblioteca:
# >Atributos -> acervo(lista_livros), usuarios_cadastrados(lista_usuarios)
# >Metodos:
# >cadastrar_usuario()-adiciona um usuário a lista
# >registra_emprestimo() - matricula: valida disponibilidade e limites antes de emprestrar
from classes.usuario import Usuario


class Biblioteca:
    def __init__(self, acervo: list, usuarios_cadastrados: list):
        self.acervo = acervo
        self.usuarios_cadastrados = usuarios_cadastrados

    def cadastrar_usuario():
        usuarios = []
        while True:
            print('-'*40)
            print(f'{"CADASTRO - USUARIO":-^40}')
            print('-'*40)
            print('0 - Sair \n 1 - Cadastrar usuario')
            if int(input('Qual sua opção? ')) != 1:
                break
            else:
                usuario = Usuario()

        print('---teste---')
        for livro in livros:
            print(livro)

    def registar_emprestimo():
        pass
