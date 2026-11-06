
class Fila:
    def __init__(self):
        self.aguardando = 0

    def emitir(self, tipo):
        self.aguardando += 1

        if tipo == "prioritaria":
            return "P1"

        return "N1"
