from allpairspy import AllPairs

PARAMS = [
    ["Correios", "Jadlog", "Loggi"],
    ["caixa", "envelope", "tubo"],
    ["com seguro", "sem seguro"],
    ["normal", "expressa", "agendada"],
]

def gerar_pairwise():
    return list(AllPairs(PARAMS))

from itertools import combinations

def pares_de(casos):
    pares = set()

    for caso in casos:
        for i, j in combinations(range(len(caso)), 2):
            pares.add((i, caso[i], j, caso[j]))

    return pares