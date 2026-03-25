# BLIBLIOTECA
# obj biblioteca:
# >Atributos -> acervo(lista_livros), usuarios_cadastrados(lista_usuarios)
# >Metodos:
# >cadastrar_usuario()-adiciona um usuário a lista
# >registra_emprestimop() - matricula: valida disponibilidade e limites antes de emprestrar

# obj Livro - Classe Livro
# >Atributos -> ISBN(str), titulo(str),autor(str),disponivel(bool);
# >Metodos ->
# >emprestar() - marca livro como indidponivel
# >devolver() - marca livro como disponivel
# >>cadastro
# >>emprestimos

# obj Usuario - classe Usuario
# Atributos -> matricula(str), nome(str), lista_livros_emprestados(list),
# Metodos ->
# >pegar_emprestado() - adiciona o livro a lista de emprestimo
# >devolver_livro() - remove o livro da lista
# >>Aluno = >>Professor (herança)
# --Aluno: Limite 3 livros simultaneos
# --Professor: Limite 5 livros simultaneos

# ----- Regras de negocio -----
# Um livro só pode ser emprestado se estiver disponível.
# Usuários não podem exceder seu limite de empréstimos.
# Lance exceções personalizadas (ex: LimiteEmprestimosExcedido,
# LivroIndisponivel).
from classes.biblioteca import Biblioteca
from classes.livros import Livros
from classes.usuario import Usuario
from classes.menu import Menu
Menu.show()
