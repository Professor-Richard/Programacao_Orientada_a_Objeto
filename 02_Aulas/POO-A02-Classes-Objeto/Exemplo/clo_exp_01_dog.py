class Dog():
    def __init__(self, nome, comida, sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono

    def comer(self):
        if self.comida > 0:
            print(f'{self.nome}Comeu uma ração')
            self.comida -= 1
        else:
            print('Não tem comida')

    def dormir(self):
        if self.sono == True:
            self.sono = False
            print("Dormiu")
        else:
            print('Sem sono')

    def time(self):
        self.sono = True
        self.comida = 0
        print(f'{self.nome} está com fome e com sono')
