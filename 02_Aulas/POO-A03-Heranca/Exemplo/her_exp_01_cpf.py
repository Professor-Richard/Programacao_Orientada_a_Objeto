class Pessoa:
    "Criando a classe Pessoa"
    def __init__(self,nome,idade):
        "definindo o que todas as pessoas tem em comum" 
        self.nome=nome
        self.idade=idade
    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade}."

class Professor(Pessoa):
    def __init__ (self,nome,idade,disciplina):
        super().__init__(nome,idade)
        self.disciplina=disciplina

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} e leciono {self.disciplina}."

    

pessoa1=Pessoa("Aluno", 18)
professor1=Professor("Richard",34,"POO")
# print(professor1.apresentar())
# print(professor1.materia("POO"))
print(pessoa1.apresentar())
print(professor1.apresentar())
