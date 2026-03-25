# obj Usuario - classe Usuario
# Atributos -> matricula(str), nome(str), lista_livros_emprestados(list),
# Metodos ->
# >pegar_emprestado() - adiciona o livro a lista de emprestimo
# >devolver_livro() - remove o livro da lista
# >>Aluno = >>Professor (herança)
# --Aluno: Limite 3 livros simultaneos
# --Professor: Limite 5 livros simultaneos

class Usuario:
    def __init__(self, matricula: str, nome: str, lista_livros_emprestados: list):
        self.matricula = matricula
        self.nome = nome
        self.lista_livros_emprestados = lista_livros_emprestados

    def pegar_emprestado():
        pass

    def devolver_livro():
        pass
