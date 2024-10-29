

class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.currentKerros = alinKerros

    #Metodi jolla hissin kerrosta siirretään
    def siirry_kerrokseen(self, targetKerros):
        if self.alinKerros > targetKerros or self.ylinKerros < targetKerros:
            print("Ei olemassaoleva kerros!")
            return
        if self.currentKerros > targetKerros:
            self.kerros_alas()
        elif self.currentKerros < targetKerros:
            self.kerros_ylös()
        if self.currentKerros != targetKerros:
            self.siirry_kerrokseen(targetKerros)
        return


    #Metodi jolla hissi liikkuu ylös
    def kerros_ylös(self):
        self.currentKerros +=1
        return

    #Metodi jolla hissi liikkuu alas
    def kerros_alas(self):
        self.currentKerros -= 1
        return


h = Hissi(1, 6)
h.siirry_kerrokseen(1)
print(h.currentKerros)
h.siirry_kerrokseen(5)
print(h.currentKerros)
h.siirry_kerrokseen(3)
print(h.currentKerros)
h.siirry_kerrokseen(8)
print(h.currentKerros)