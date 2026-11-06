class Fila:
    def __init__(self):
        self.aguardando = 0
        self._normais_emitidas = 0
        self._prioritarias_emitidas = 0

    def emitir(self, tipo):
        self.aguardando += 1

        if tipo == "prioritaria":
            self._prioritarias_emitidas += 1
            return f"P{self._prioritarias_emitidas}"

        self._normais_emitidas += 1
        return f"N{self._normais_emitidas}"