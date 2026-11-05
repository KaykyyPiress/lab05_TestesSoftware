a) Foi começado com vazio porque é o caso mais simples, já que não tem nenhuma palavra para contar. Depois coloquei o teste com uma palavra só, porque ele exige apenas contar uma ocorrência. Assim, fica mais fácil seguir o TDD, começando pelo básico e adicionando as outras regras aos poucos.

c) 
0e19064 (HEAD -> main) GREEN: conta uma palavra
d37960e RED: uma palavra retorna uma ocorrencia
e86b9cc GREEN: retorna dicionario vazio
b39af3c RED: texto vazio devolve dicionario vazio

d)
Até agora, nenhum teste novo passou de primeira, pois os dois falharam na fase RED, como esperado no TDD.
O teste de texto vazio passou quando adicionamos o segundo teste, porque já tinha sido implementado na fase GREEN anterior.
Os testes continuam na suíte, pois ajudam a garantir que as funcionalidades já implementadas não parem de funcionar quando modificarmos o código.

e)
O Mutmut gerou 2 mutantes, e os 2 foram mortos pelos testes, resultando em um Mutation Score de 100%. Isso mostra que os testes conseguiram identificar todas as alterações feitas nessa versão do código.