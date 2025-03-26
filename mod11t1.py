class Julkaisu:

    julkaisujen_lukumäärä = 0

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        Julkaisu.julkaisujen_lukumäärä = Julkaisu.julkaisujen_lukumäärä + 1
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.kirjoittaja}: {self.nimi}, sivumäärä: {self.sivumäärä}")

julkaisut = []
julkaisut.append(Julkaisu("Aku Ankka","Aki Hyyppä", "60"))
julkaisut.append(Julkaisu("Hytti n:o 6", "Rosa Liksom", "200"))

for i in julkaisut:
    i.tulosta_tiedot()