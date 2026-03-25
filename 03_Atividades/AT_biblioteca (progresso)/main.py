# =========================
# EXCEÇÕES PERSONALIZADAS
# =========================
class LimiteEmprestimosExcedido(Exception):
    def __init__(self, mensagem="O usuário excedeu o limite de empréstimos permitidos."):
        super().__init__(mensagem)


class LivroIndisponivel(Exception):
    def __init__(self, mensagem="O livro não está disponível para empréstimo."):
        super().__init__(mensagem)


class UsuarioNaoEncontrado(Exception):
    def __init__(self, mensagem="Usuário não encontrado."):
        super().__init__(mensagem)


class LivroNaoEncontrado(Exception):
    def __init__(self, mensagem="Livro não encontrado no acervo."):
        super().__init__(mensagem)


class LivroNaoEmprestadoAoUsuario(Exception):
    def __init__(self, mensagem="Este livro não está emprestado para este usuário."):
        super().__init__(mensagem)


# =========================
# CLASSE LIVRO
# =========================
class Livro:
    def __init__(self, isbn: str, titulo: str, autor: str, disponivel: bool = True):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = disponivel

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def disponivel(self) -> bool:
        return self.__disponivel

    def emprestar(self):
        if not self.__disponivel:
            raise LivroIndisponivel(
                f"O livro '{self.__titulo}' já está emprestado.")
        self.__disponivel = False

    def devolver(self):
        self.__disponivel = True

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"ISBN: {self.__isbn} | Título: {self.__titulo} | Autor: {self.__autor} | Status: {status}"


# =========================
# CLASSE USUARIO (ABSTRATA)
# =========================
class Usuario(ABC):
    def __init__(self, matricula: str, nome: str):
        self.__matricula = matricula
        self.__nome = nome
        self.__lista_livros_emprestados = []

    @property
    def matricula(self) -> str:
        return self.__matricula

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def lista_livros_emprestados(self) -> list:
        return self.__lista_livros_emprestados.copy()

    def _adicionar_livro(self, livro: Livro):
        self.__lista_livros_emprestados.append(livro)

    def _remover_livro(self, livro: Livro):
        if livro not in self.__lista_livros_emprestados:
            raise LivroNaoEmprestadoAoUsuario(
                f"O livro '{livro.titulo}' não está emprestado para o usuário {self.__nome}."
            )
        self.__lista_livros_emprestados.remove(livro)

    @property
    @abstractmethod
    def limite_emprestimos(self) -> int:
        pass

    @abstractmethod
    def pegar_emprestado(self, livro: Livro):
        pass

    @abstractmethod
    def devolver_livro(self, livro: Livro):
        pass

    def __str__(self):
        return f"Matrícula: {self.__matricula} | Nome: {self.__nome} | Tipo: {self.__class__.__name__}"


# =========================
# CLASSE ALUNO
# =========================
class Aluno(Usuario):
    @property
    def limite_emprestimos(self) -> int:
        return 3

    def pegar_emprestado(self, livro: Livro):
        if len(self.lista_livros_emprestados) >= self.limite_emprestimos:
            raise LimiteEmprestimosExcedido(
                f"O aluno {self.nome} atingiu o limite de {self.limite_emprestimos} livros."
            )

        livro.emprestar()
        self._adicionar_livro(livro)

    def devolver_livro(self, livro: Livro):
        self._remover_livro(livro)
        livro.devolver()


# =========================
# CLASSE PROFESSOR
# =========================
class Professor(Usuario):
    @property
    def limite_emprestimos(self) -> int:
        return 5

    def pegar_emprestado(self, livro: Livro):
        if len(self.lista_livros_emprestados) >= self.limite_emprestimos:
            raise LimiteEmprestimosExcedido(
                f"O professor {self.nome} atingiu o limite de {self.limite_emprestimos} livros."
            )

        livro.emprestar()
        self._adicionar_livro(livro)

    def devolver_livro(self, livro: Livro):
        self._remover_livro(livro)
        livro.devolver()


# =========================
# CLASSE BIBLIOTECA
# =========================
class Biblioteca:
    def __init__(self):
        self.__acervo = []
        self.__usuarios_cadastrados = []

    @property
    def acervo(self) -> list:
        return self.__acervo.copy()

    @property
    def usuarios_cadastrados(self) -> list:
        return self.__usuarios_cadastrados.copy()

    def adicionar_livro(self, livro: Livro):
        self.__acervo.append(livro)

    def cadastrar_usuario(self, usuario: Usuario):
        self.__usuarios_cadastrados.append(usuario)

    def __buscar_usuario_por_matricula(self, matricula: str) -> Usuario:
        for usuario in self.__usuarios_cadastrados:
            if usuario.matricula == matricula:
                return usuario
        raise UsuarioNaoEncontrado(
            f"Usuário com matrícula '{matricula}' não foi encontrado.")

    def __buscar_livro_por_isbn(self, isbn: str) -> Livro:
        for livro in self.__acervo:
            if livro.isbn == isbn:
                return livro
        raise LivroNaoEncontrado(
            f"Livro com ISBN '{isbn}' não foi encontrado.")

    def registrar_emprestimo(self, matricula: str, isbn: str):
        usuario = self.__buscar_usuario_por_matricula(matricula)
        livro = self.__buscar_livro_por_isbn(isbn)

        usuario.pegar_emprestado(livro)
        print(f"Empréstimo realizado: '{livro.titulo}' para {usuario.nome}.")

    def registrar_devolucao(self, matricula: str, isbn: str):
        usuario = self.__buscar_usuario_por_matricula(matricula)
        livro = self.__buscar_livro_por_isbn(isbn)

        usuario.devolver_livro(livro)
        print(
            f"Devolução realizada: '{livro.titulo}' devolvido por {usuario.nome}.")

    def consultar_livros_emprestados(self):
        print("\n=== LIVROS EMPRESTADOS ===")
        encontrou = False

        for usuario in self.__usuarios_cadastrados:
            livros = usuario.lista_livros_emprestados
            if livros:
                encontrou = True
                print(
                    f"\nUsuário: {usuario.nome} ({usuario.__class__.__name__})")
                for livro in livros:
                    print(f" - {livro.titulo} ({livro.isbn})")

        if not encontrou:
            print("Nenhum livro está emprestado no momento.")

    def listar_acervo(self):
        print("\n=== ACERVO DA BIBLIOTECA ===")
        for livro in self.__acervo:
            print(livro)

    def listar_usuarios(self):
        print("\n=== USUÁRIOS CADASTRADOS ===")
        for usuario in self.__usuarios_cadastrados:
            print(
                f"{usuario} | Livros emprestados: {len(usuario.lista_livros_emprestados)}/{usuario.limite_emprestimos}"
            )


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Cadastro inicial de livros
    livros_iniciais = [
        Livro("LIV001", "Titulo 1", "Autor 1", True),
        Livro("LIV002", "Titulo 2", "Autor 2", True),
        Livro("LIV003", "Titulo 3", "Autor 3", True),
        Livro("LIV004", "Titulo 4", "Autor 4", True),
        Livro("LIV005", "Titulo 5", "Autor 5", True),
    ]

    for livro in livros_iniciais:
        biblioteca.adicionar_livro(livro)

    # Cadastro inicial de usuários
    aluno1 = Aluno("ALUNOXX1", "Nome 1")
    aluno2 = Aluno("ALUNOXX2", "Nome 2")
    professor1 = Professor("PROFXX1", "Professor")

    biblioteca.cadastrar_usuario(aluno1)
    biblioteca.cadastrar_usuario(aluno2)
    biblioteca.cadastrar_usuario(professor1)

    # Exibição inicial
    biblioteca.listar_acervo()
    biblioteca.listar_usuarios()

    print("\n=== TESTES DE EMPRÉSTIMO ===")

    try:
        biblioteca.registrar_emprestimo("ALUNOXX1", "LIV001")
        biblioteca.registrar_emprestimo("ALUNOXX1", "LIV002")
        biblioteca.registrar_emprestimo("ALUNOXX1", "LIV003")

        # Este deve falhar por limite excedido do aluno
        biblioteca.registrar_emprestimo("ALUNOXX1", "LIV004")
    except (LimiteEmprestimosExcedido, LivroIndisponivel, UsuarioNaoEncontrado, LivroNaoEncontrado) as e:
        print(f"Erro: {e}")

    try:
        # Professor empresta livro disponível
        biblioteca.registrar_emprestimo("PROFXX1", "LIV004")

        # Tentativa de emprestar livro já emprestado
        biblioteca.registrar_emprestimo("ALUNOXX2", "LIV004")
    except (LimiteEmprestimosExcedido, LivroIndisponivel, UsuarioNaoEncontrado, LivroNaoEncontrado) as e:
        print(f"Erro: {e}")

    biblioteca.consultar_livros_emprestados()
    biblioteca.listar_acervo()

    print("\n=== TESTE DE DEVOLUÇÃO ===")
    try:
        biblioteca.registrar_devolucao("ALUNOXX1", "LIV002")
    except (UsuarioNaoEncontrado, LivroNaoEncontrado, LivroNaoEmprestadoAoUsuario) as e:
        print(f"Erro: {e}")

    biblioteca.consultar_livros_emprestados()
    biblioteca.listar_acervo()
