class Animal:
    """Animal"""

    def __init__(self, nom, dateNais):
        self._nom = nom
        self._dateNais = dateNais
        self.numero = ""
        self.espece = "Animal"

    def getNom(self):
        return self._nom

    def cri(self):
        print("")


class Chat(Animal):
    def __init__(
        self, nom, dateNais, race="Gros Chat", description="Crisse de gros chat"
    ):
        """chat description"""

        Animal.__init__(self, nom, dateNais)
        self._race = race
        self.espece = "Chat"
        self.description = description

    def miaule(self):
        print("Miew!")

    def cri(self):
        self.miaule()


class Chien(Animal):
    def __init__(self, nom, dateNais, race):
        Animal.__init__(self, nom, dateNais)
        self._race = race
        self._espece = "Chien"

    def jappe(self):
        print("Wouf!")

    def cri(self):
        self.jappe()


chat1 = Chat("Gizmo", 2008, description="pas si gros chat")
chien1 = Chien("Rex", 2009, "Doberman")

animaux = [
    Chat("Gizmo", 2008, "Gros Chat"),
    Chien("Rex", 2009, "Doberman"),
    Chat("patate", 2008, "Gros Chat"),
    Chien("chiot", 2009, "Doberman"),
    Chat("chose", 2008, "Gros Chat"),
    Chien("bob", 2009, "Doberman"),
    Chat("jean", 2008, "Gros Chat"),
    Chien("lechien", 2009, "Doberman"),
    Chat("kittycat", 2008, "Gros Chat"),
    Chien("Rex2", 2009, "Doberman"),
]

for animal in animaux:
    animal.cri()

cri = chat1.cri()
cri = chien1.cri()
