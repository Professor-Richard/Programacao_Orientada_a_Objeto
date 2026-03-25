# obj Livro - Classe Livro
# >Atributos -> ISBN(str), titulo(str),autor(str),disponivel(bool);
# >Metodos ->
# >emprestar() - marca livro como indidponivel
# >devolver() - marca livro como disponivel
# >>cadastro
# >>emprestimos
class Livros:
    def __init__(self, isbn: str, titulo: str, autor: str, disponivel: bool):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar():
        pass

    def devolver():
        pass

    def cadastrar():
        livros = []
        print('-'*40)
        print(f'{"MENU DE CADASTRO - LIVROS":-^40}')
        print('-'*40)
        print('0 - Sair \n 1 - Cadastrar livro')
        while True:
            if int(input('Qual sua opção? ')) != 1:
                break
            else:
                isbn = input('ISBN: ')
                titulo = input('Titulo: ')
                autor = input('Autor: ')
                disponivel = bool(input('Disponivel: 0-sim,1-não')) == '1'
                livros.append((isbn, titulo, autor, disponivel))
        print('---teste---')
        for livro in livros:
            print(livro)

    def emprestimos():
        pass
