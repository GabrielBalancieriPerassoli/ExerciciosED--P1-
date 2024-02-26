class Fila:
    def __init__(self, tam_max):
        self.TamMax = tam_max
        self.Elem = [None] * tam_max
        self.Inicio = -1
        self.Fim = -1

    def InicializaFila(self):
        self.Inicio = -1
        self.Fim = -1

    def FilaVazia(self):
        return self.Inicio == self.Fim

    def FilaCheia(self):
        return self.Inicio == -1 and self.Fim == self.TamMax - 1

    def DeslocaFila(self):
        desloc = self.Inicio + 1
        for i in range(self.Inicio + 1, self.Fim + 1):
            self.Elem[i - desloc] = self.Elem[i]
        self.Inicio = -1
        self.Fim -= desloc

    def InsereFila(self, x):
        if not self.FilaCheia():
            if self.Fim == self.TamMax - 1:
                self.DeslocaFila()
            self.Fim += 1
            self.Elem[self.Fim] = x

    def RemoveFila(self):
        if not self.FilaVazia():
            self.Inicio += 1
            x = self.Elem[self.Inicio]
            if self.FilaVazia():
                self.Inicio = -1
                self.Fim = -1
            return x

    def PrimeiroDaFila(self):
        if not self.FilaVazia():
            return self.Elem[self.Inicio + 1]
        else:
            return "<ERRO>"
