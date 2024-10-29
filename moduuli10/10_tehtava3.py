
class Talo:
    def __init__(self, alinKerros, ylinKerros, hissienLkm):
        self.hissiLista =[]
        for i in range(hissienLkm):
            self.hissiLista.append(Hissi(alinKerros, ylinKerros))

    #Ajetaan talon hisseillä 1-joku, ja kohdekerros. Jos ei onnistunut kerrotaan siitä
    def ajaHissiä(self, hissiNumero, targetKerros):
        if self.hissiLista[hissiNumero-1].currentKerros == targetKerros:
            print(f"Hissi {hissiNumero} on jo pyydetyssä kerroksessa!\n")
            return
        print(f"Ajetaan hissi {hissiNumero}: kerroksesta {self.hissiLista[hissiNumero - 1].currentKerros} kerrokseen {targetKerros}")
        if (targetKerros < self.hissiLista[hissiNumero-1].alinKerros
            or targetKerros > self.hissiLista[hissiNumero-1].ylinKerros):
            print(f"Hissi numero {hissiNumero}: {targetKerros} ei ole määritetty kerros\n")
            return
        self.hissiLista[hissiNumero-1].siirry_kerrokseen(targetKerros)
        print(f"Hissi numero {hissiNumero} on saapunut kerrokseen {self.hissiLista[hissiNumero-1].currentKerros}\n")
        return

    #Palohälytys ajetaan kaikki hissit pohjakerrokseen
    def paloHälytys(self):
        print("Palohälytys ajetaan kaikki hissit pohjakerrokseen!\n")
        for i in range(len(self.hissiLista)):
            self.ajaHissiä(i+1, self.hissiLista[i].alinKerros)
        return

class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.currentKerros = alinKerros

    #Metodi jolla hissin kerrosta siirretään
    def siirry_kerrokseen(self, targetKerros):
        while self.currentKerros > targetKerros:
            self.kerros_alas()
        while self.currentKerros < targetKerros:
            self.kerros_ylös()
        return

    #Metodi jolla hissi liikkuu ylös
    def kerros_ylös(self):
        self.currentKerros +=1
        print(f"Hissi liikkuu ylös {self.currentKerros}")
        return

    #Metodi jolla hissi liikkuu alas
    def kerros_alas(self):
        self.currentKerros -= 1
        print(f"Hissi liikkuu alas {self.currentKerros}")
        return


talo1 = Talo(1, 6, 3)
talo1.ajaHissiä(1,3)
talo1.ajaHissiä(3,5)
talo1.ajaHissiä(1,1)
talo1.ajaHissiä(2,3)
talo1.paloHälytys()

talo2 = Talo(-2, 10,4)
talo2.ajaHissiä(3,30)
talo2.ajaHissiä(2, 6)
talo2. ajaHissiä(4,-1)
talo2.paloHälytys()

talo1.ajaHissiä(2,5)