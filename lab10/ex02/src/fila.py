
class Fila:
    def __init__(self):
        self.aguardando = 0
        self._normais_emitidas = 0
        self._prioritarias_emitidas = 0
        self._normais = []
        self._prioritarias = []
        self._prioritarias_seguidas = 0

    def emitir(self, tipo):
        if tipo not in ("normal", "prioritaria"):
            raise ValueError("tipo invalido")

        self.aguardando += 1

        if tipo == "prioritaria":
            self._prioritarias_emitidas += 1
            senha = f"P{self._prioritarias_emitidas}"
            self._prioritarias.append(senha)
            return senha

        self._normais_emitidas += 1
        senha = f"N{self._normais_emitidas}"
        self._normais.append(senha)
        return senha

    def chamar(self):
        if self._prioritarias and self._prioritarias_seguidas < 2:
            self._prioritarias_seguidas += 1
            self.aguardando -= 1
            return self._prioritarias.pop(0)

        if self._normais:
            self._prioritarias_seguidas = 0
            self.aguardando -= 1
            return self._normais.pop(0)

        if self._prioritarias:
            self.aguardando -= 1
            return self._prioritarias.pop(0)

        raise IndexError("fila vazia")
