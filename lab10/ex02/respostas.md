c) O teste test_duas_prioritarias_seguidas obrigou a criar um contador para controlar o limite de duas prioritárias consecutivas, garantindo que uma normal seja atendida depois delas.

Já o teste test_zerar_contagem_apos_normal obrigou a zerar esse contador após atender uma senha normal, permitindo chamar mais duas prioritárias em seguida.

d) Limite de prioritárias sem normais

O teste test_mais_de_duas_prioritarias_sem_normal mostra isso. Nele, colocamos quatro senhas prioritárias e nenhuma normal na fila. O teste verifica que todas são atendidas em sequência, mostrando que o limite de duas só vale quando existe uma senha normal esperando.

e) Ao executar o Mutmut, encontrei 6 mutantes sobreviventes, sendo 3 no método emitir() e 3 no método chamar().