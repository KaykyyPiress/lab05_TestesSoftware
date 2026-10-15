from hypothesis import given, strategies as st
from src.intervalos import normalizar, mesclar


@given(
    st.lists(
        st.tuples(
            st.integers(min_value=0, max_value=50),
            st.integers(min_value=0, max_value=50)
        )
    )
)
def test_normalizar(intervalos):
    resultado = normalizar(intervalos)

    assert len(resultado) == len(intervalos)

    for ini, fim in resultado:
        assert ini <= fim



entradas = st.lists(
    st.tuples(
        st.integers(min_value=0, max_value=50),
        st.integers(min_value=0, max_value=50)
    )
)


# 1: idempotência
@given(entradas)
def test_idempotencia(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    assert mesclar(resultado) == resultado


# 2: ordem e ausência de sobreposição
@given(entradas)
def test_ordem_sem_sobreposicao(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    for ini, fim in resultado:
        assert ini <= fim

    for i in range(len(resultado) - 1):
        assert resultado[i][1] < resultado[i + 1][0]


# 3: todos os intervalos estão contidos
@given(entradas)
def test_contencao(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    for ini, fim in intervalos:
        assert any(
            r_ini <= ini and fim <= r_fim
            for r_ini, r_fim in resultado
        )

#--
def mesclar(intervalos):
    resultado = []

    for ini, fim in sorted(intervalos):
        if resultado and ini <= resultado[-1][1]:
            resultado[-1] = (
                resultado[-1][0],
                max(resultado[-1][1], fim)
            )
        else:
            resultado.append((ini, fim))

    return resultado