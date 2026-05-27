class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def som(self) -> str:
        return "Som genérico"


class Cao(Animal):
    def som(self) -> str:
        return "Au au"


class Gato(Animal):
    def som(self) -> str:
        return "Miau"


def fazer_som(animal: Animal) -> str:
    # mesma "mensagem" (som), comportamentos diferentes (polimorfismo)
    return f"{animal.nome}: {animal.som()}"
