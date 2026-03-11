# configuracoes.py

from raca import Raca
from vocacao import Vocacao

RACAS = {
    "Elfo": Raca("Elfo", 1, 0, 0, 2),
    "Anão": Raca("Anão", 0, 2, 3, -1),
    "Humano": Raca("Humano", 1, 1, 1, 1),
}

VOCACOES = {
    "Guerreiro": Vocacao("Guerreiro", 3, 2, 5, 0),
    "Arqueiro": Vocacao("Arqueiro", 2, 0, 0, 3),
    "Paladino": Vocacao("Paladino", 2, 3, 4, 0),
}
