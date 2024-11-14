#O valor de Euler (e) é uma constante matemática fundamental aproximadamente igual a 2.71828. Ele é a base dos logaritmos naturais e aparece frequentemente em várias áreas da matemática, especialmente em cálculos envolvendo crescimento exponencial, decaimento exponencial, e em muitas fórmulas de cálculo e análise matemática.

from decimal import Decimal  # Importa a classe Decimal do módulo decimal
import random as r  # Importa o módulo random com o alias r
import numpy as np  # Importa a biblioteca numpy para operações matemáticas

e = np.e  # Atribui o valor de Euler (e) da biblioteca numpy à variável e

# Define uma lista de valores para testar
v = [0.1, 0.01, 0.032, 0.0432, 0.3, 0.009, 0.05, 0.5, 0.001, 0.0001]

# Define a função f1 usando uma expressão lambda
f1 = lambda x: e**(1.0/x) / (1.0 + e**(1.0/x))

# Define a função f2 usando uma expressão lambda
f2 = lambda x: 1.0 / (e**(-1.0/x) + 1.0)

# Define a função func1 que tenta calcular f1 e lida com possíveis erros de overflow
def func1(i):
    try:
        return f1(i)
    except:
        return 'OverflowError'

# Define a função func2 que tenta calcular f2 e lida com possíveis erros de overflow
def func2(i):
    try:
        return f2(i)
    except:
        return 'OverflowError'

# Loop para calcular e imprimir os resultados de f1 e f2 para cada valor em v
for i in v:
    print '\nPara o valor de x =', i, '\n\n\tf1', func1(i), 'f2', func2(i)