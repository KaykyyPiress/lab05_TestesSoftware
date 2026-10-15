#Lab 07

### 1 - a) 

Combinações completas: 3 × 3 × 2 × 3 = 54 combinações.
Mínimo pairwise: 9 casos de teste.

O maior número de pares ocorre entre dois parâmetros com 3 opções cada.  Como cada teste cobre apenas um desses pares e é possível cobrir todos os demais pares com os mesmos 9 testes.

### 2 - b)

O teste identificou que o adicional de R$ 8
da região norte não é aplicado para encomendas leves.

### 2 -c)
O adicional de R$ 8 da região norte não é aplicado
   quando o peso é leve (4 falhas).
O limite incorreto de R$ 60 reduz o valor do frete
   pesado, expresso e destinado ao norte (2 falhas).
O teste completo identificou os dois
defeitos da implementação, enquanto o pairwise anterior
não detectou o segundo defeito.

### 2 - d)
- **Defeito 1 (2-way):** Envolve peso leve e região norte.
  O pairwise encontrou porque garante a cobertura de todos os pares.

- **Defeito 2 (3-way):** Envolve peso pesado, entrega expressa
  e região norte. O pairwise não encontrou porque não garante
  a cobertura de combinações de três parâmetros.

### 2 - e) 
função "Esperado" criado;


### 3 - c)
- Idempotência: passou.
- Ordem e ausência de sobreposição: passou.
- Contenção dos intervalos: falhou.

**Contraexemplo mínimo:**
Entrada: [(0, 2), (1, 1)]

- Resultado obtido: [(0, 1)]
- Resultado esperado: [(0, 2)]

**Defeito:** A função substitui o limite final do
intervalo anterior sem verificar se o novo limite
é maior, podendo diminuir um intervalo já existente.

### 3 - d)
### d) Correção da função
0
A função mesclar()  foi corrigida utilizando max()
para preservar o maior limite final durante a união.

**Resultado:** Após a correção, todas as propriedades
foram satisfeitas.

**Primeira entrada:** A lista vazia [] é o caso
mais simples da estratégia st.lists(), pois ela
permite listas com zero elementos.

O Hypothesis prioriza casos simples e extremos,
embora a ordem exata de execução possa variar.
