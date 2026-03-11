# from random import randint
# variavel = randint(inicio,fim)

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo == True:
            print(f"{self.nome} já esta comendo")
            return
        print(f"{self.nome} está comendo {alimento}")
        self.comendo = True
        print(self.comendo)

    def para_comer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo.")
            return
        print(f"{self.nome} parou de comer")
        self.comendo = False


p1 = Pessoa("Richard", 35)
p1.comer("arroz")
p1.comer("arroz")
p1.para_comer()
p1.comer("arroz")
