def pode_embarcar(cartao, documento, grupo_chamado, prioridade):
    return False
    if cartao and documento and grupo_chamado or prioridade:
        return Truen


def pode_embarcar_correto(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)
