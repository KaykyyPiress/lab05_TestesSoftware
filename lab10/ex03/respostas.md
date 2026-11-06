a) Os testes do cupom DEZ com subtotal de 5000 e de 1000 precisam ser alterados, pois antes aplicavam 10% de desconto em qualquer valor.

Agora, o desconto só vale a partir de 10000. Por isso, devemos atualizar os resultados esperados nos testes antes de modificar o código, seguindo o TDD.

c) 
Para garantir que nada mudou no funcionamento, executei novamente os 16 testes, que continuaram passando. A cobertura também permaneceu em 100%.

d)
Os valores 1 e 2 verificam quantidades válidas. O 0 e o -1 verificam se valores menores que 1 são rejeitados. Já o 1.5 testa números fracionários e o `True` garante que valores booleanos não sejam aceitos como inteiros.