class Hissi:

    def __init__(self, alin, ylin):
        self.alin_kerros=alin
        self.ylin_kerros=ylin
        self.kerros = self.alin_kerros

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Olet kerroksessa {self.kerros}.")
        if self.kerros > self.ylin_kerros:
            self.kerros = self.ylin_kerros
            print(f"Olet kerroksessa {self.kerros}, etkä voi mennä ylemmäs.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Olet kerroksessa {self.kerros}")
        if self.kerros < self.alin_kerros:
            self.kerros = self.alin_kerros
            print(f"Olet kerroksessa {self.kerros}, etkä voi mennä alemmas.")

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        if self.kerros < self.alin_kerros:
            self.kerros = self.alin_kerros
        if self.kerros > self.ylin_kerros:
            self.kerros = self.ylin_kerros
        print(f"Olet kerroksessa {self.kerros}")

class Talo:
    def __init__(self, ylin, alin, hissi):
        self.alin_kerros=alin
        self.ylin_kerros=ylin
        self.hissi=hissi

    def aja_hissia(self, hissi, kerros):
        self.hissi=hissi
        Hissi.kerros = kerros
        print(f"Ajoit hissiä {hissi} ja olet kerroksessa {kerros}")

    def palohalytys(self):
        self.kerros = self.alin_kerros
        print(f"PALOHÄLYTYS!!!! Hissi {self.hissi} siirtyy kerrokseen {self.kerros}")



h = Hissi(0,5)
h2 = Hissi(0, 5)
h3 = Hissi(0, 5)

h.siirry_kerrokseen(5)

Talo.aja_hissia(h,1, 4)
Talo.aja_hissia(h2, 2, 3)
Talo.aja_hissia(h3, 3, 2)
Talo.palohalytys(h)
Talo.palohalytys(h2)
Talo.palohalytys(h3)





