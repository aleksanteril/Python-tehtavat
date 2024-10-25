
class Talo:
    def __init__(self, alinKerros, ylinKerros, hissienLkm):
        self.hissiLista =[]
        for i in range(hissienLkm):
            self.hissiLista.append(Hissi(alinKerros, ylinKerros))

    #Ajetaan talon hisseillä 1-joku, ja kohdekerros. Jos ei onnistunut kerrotaan siitä
    def ajaHissiä(self, hissiNumero, targetKerros):
        if not self.hissiLista[hissiNumero-1].siirry_kerrokseen(targetKerros):
            print(f"Hissi numero {hissiNumero}, ei ole määritetty kerros")
            return
        print(f"Hissi numero {hissiNumero} on kerroksessa {self.hissiLista[hissiNumero-1].currentKerros}")
        return


class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.currentKerros = alinKerros

    #Metodi jolla hissin kerrosta siirretään
    def siirry_kerrokseen(self, targetKerros):
        if self.alinKerros <= targetKerros <=self.ylinKerros:
            if self.currentKerros > targetKerros:
                self.kerros_alas()
            elif self.currentKerros < targetKerros:
                self.kerros_ylös()
            if self.currentKerros != targetKerros:
                self.siirry_kerrokseen(targetKerros)
            return True
        return False

    #Metodi jolla hissi liikkuu ylös
    def kerros_ylös(self):
        self.currentKerros +=1
        return

    #Metodi jolla hissi liikkuu alas
    def kerros_alas(self):
        self.currentKerros -= 1
        return


talo1 = Talo(1, 6, 3)
talo1.ajaHissiä(1,3)
talo1.ajaHissiä(3,5)
talo1.ajaHissiä(1,1)
talo1.ajaHissiä(2,8)