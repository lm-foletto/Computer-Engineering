# O objetivo deste código é calcular o logaritmo natural (ln) de um número x utilizando uma série de Taylor. O cálculo continua até que o erro entre a iteração atual e a anterior seja menor que 0.0001, garantindo uma aproximação precisa do logaritmo natural.

def func(x):
    n = 1  # Inicializa o contador n com 1
    lna = 0  # Inicializa lna (logaritmo natural anterior) com 0
    err = 10.0  # Inicializa o erro com um valor alto para entrar no loop
    ln = 0  # Inicializa ln (logaritmo natural atual) com 0

    # Loop para calcular o logaritmo natural usando a série de Taylor até que o erro seja menor que 0.0001
    while err > 0.0001:
        if n % 2 == 1:  # Se n é ímpar
            ln = lna + ((x - 1) ** n) / n  # Adiciona o termo da série
        else:  # Se n é par
            ln = lna - ((x - 1) ** n) / n  # Subtrai o termo da série

        err = abs(ln - lna)  # Calcula o erro aproximado
        lna = ln  # Atualiza o valor anterior do logaritmo natural
        n += 1  # Incrementa o contador n

    return ln, n  # Retorna o valor calculado do logaritmo natural e o número de iterações

# Chama a função func com x = 0.8 e armazena os resultados em x e n
x, n = func(0.8)

# Imprime o valor calculado do logaritmo natural e o número de iterações
print 'Este eh o valor', x, ' com aproximacao menor que 0.0001 com ', n, ' repeticoes'