#O objetivo deste código é determinar o epsilon da máquina, que é o menor número positivo que, quando adicionado a 1.0, resulta em um valor diferente de 1.0. Este valor é importante em cálculos numéricos para entender a precisão e os limites da representação de números de ponto flutuante no computador.

from decimal import Decimal  # Importa a classe Decimal do módulo decimal

i = 1  # Inicializa o contador i com 1
eps = 1.0  # Inicializa eps com 1.0
eps1 = 0.0  # Inicializa eps1 com 0.0

eps = eps / 2  # Divide eps por 2
eps1 = eps + 1.0  # Adiciona 1.0 a eps e armazena o resultado em eps1

# Loop para encontrar o menor epsilon da máquina
while eps1 > 1.0:
    print i, 'epsilon =', eps  # Imprime o valor atual de i e eps
    eps = eps / 2  # Divide eps por 2
    eps1 = eps + 1.0  # Adiciona 1.0 a eps e armazena o resultado em eps1
    i = i + 1  # Incrementa o contador i

# Imprime o valor final de epsilon da máquina
print 'este eh o epsilon da maquina = ', eps