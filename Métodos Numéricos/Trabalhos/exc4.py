#O objetivo deste código é calcular uma aproximação do valor de π (pi) utilizando a série de Leibniz. A série de Leibniz é uma série infinita que converge para π/4. Este método é uma forma simples e clássica de calcular o valor de π através de uma série alternada de frações.

from decimal import Decimal  # Importa a classe Decimal do módulo decimal
import math  # Importa o módulo math para operações matemáticas

l = math.pi / 4.0  # Calcula o valor de pi dividido por 4 e armazena na variável l

i = 0.0  # Inicializa o contador i com 0.0
x = 0  # Inicializa a variável x com 0

# Loop para calcular a série de Leibniz para pi/4
while i < 50:
    x = x + ((-1.0)**i) / (2.0*i + 1.0)  # Adiciona o próximo termo da série à variável x
    i = i + 1  # Incrementa o contador i

# Imprime o valor calculado de pi/4 e o valor da série
print 'valor de PI / 4 = ', l, 'valor do somatório = ', x
print 'Fim!!!'  # Imprime mensagem de fim