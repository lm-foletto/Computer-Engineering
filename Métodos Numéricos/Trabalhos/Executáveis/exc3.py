#sO objetivo do algoritmo é calcular o valor de Euler (e) com uma precisão especificada, utilizando a série de expansão. O algoritmo itera até que o erro entre o valor calculado e o valor anterior seja menor que 0.0001, garantindo assim uma aproximação precisa do número de Euler.

from decimal import Decimal  # Importa a classe Decimal do módulo decimal
import numpy as np  # Importa a biblioteca numpy para operações matemáticas

i = 0.0  # Inicializa o contador i com 0.0
err = 10.0  # Inicializa o erro com um valor alto para entrar no loop
ea = 0.0  # Inicializa o valor aproximado de e com 0.0

# Loop para calcular o valor de e usando a expansão em série até que o erro seja menor que 0.0001
while err > 0.0001:
    # Realiza a operação para descobrir o valor de e (Euler) usando a expansão em série
    e = ea + (1.0 / np.math.factorial(i))

    # Incrementa o contador i
    i += 1.0

    # Calcula o erro aproximado
    err = abs((e - ea) / e)
    ea = e  # Atualiza o valor aproximado de e

    # Imprime o valor atual de e, o erro e o contador
    print ea, 'Error = ', err, 'i = ', i

# Imprime o resultado final e compara com o valor de e da biblioteca numpy
print 'resultado ', ea, ' eh mais proximo de e da bib-math=', np.e
print 'Erro aproximado = ', err