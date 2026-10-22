
from itertools import product

# Regra conforme a especificação
def regra(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)


# Encontra os pares independentes para MC/DC
def pares_independentes(decisao, n):
    tabela = list(product([False, True], repeat=n))
    pares = {i: [] for i in range(n)}

    for linha1 in tabela:
        for linha2 in tabela:
            diferencas = [
                i for i in range(n)
                if linha1[i] != linha2[i]
            ]

            if len(diferencas) == 1:
                if decisao(*linha1) != decisao(*linha2):
                    i = diferencas[0]
                    par = (linha1, linha2)

                    if (linha2, linha1) not in pares[i]:
                        pares[i].append(par)

    return pares


# Exemplo de execução
pares = pares_independentes(regra, 4)

for condicao, lista in pares.items():
    print(f"Condição {condicao}: {len(lista)} pares")
    for par in lista:
        print(par)
