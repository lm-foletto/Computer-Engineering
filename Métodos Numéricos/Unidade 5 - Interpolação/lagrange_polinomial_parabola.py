import matplotlib.pyplot as plt

# Dados do exercicio
X = [0.0, 0.5, 1.0]
Y = [1.3, 2.5, 0.9]

# Funcao que calcula o valor do polinomio para um dado x
def calculaP(x):
    valor = 0
    for k in range(len(Y)):
        lk = 1.0
        for i in range(len(X)):
            if k != i:
                lk = lk*(x - X[i])/(X[k]-X[i])
        valor = valor +Y[k]*lk 
    return valor
print ("P(",0.23,")", calculaP(0.23))

# Cria a lista de pontos e calcula os valores para p plot
Xplot = []
Yplot = []
n = 20              # Numero de divisoes do intervalo de plot
dx = (X[-1]-X[0])/n # Incremento em x

# Preenche as listas X e Y para o plot 
for i in range(n+1):
    x = X[0] + i*dx
    y = calculaP(x)
    Xplot.append(x)
    Yplot.append(y)

# Plota
plt.plot(X, Y, "ro") # Plota os pontos dados 
plt.plot(Xplot, Yplot, "-") # Plota o polinomio com linha
#plt.grid(True) # Cria uma grid
plt.show() # Mostra


