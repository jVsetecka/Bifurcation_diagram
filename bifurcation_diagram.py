import matplotlib.pyplot as plt
import math

beta = 0
beta_values = []
x_values = []

while beta <= 4:
    xold = 0.5
    for i in range(1000):
        xnew = ((xold - math.pow(xold, 2)) * beta) # x + 1 = beta*x*(1-x)
        xold = xnew
    xss = xnew
    for i in range(10000):
        xnew = ((xold - math.pow(xold, 2)) * beta)
        xold = xnew
        beta_values.append(beta)
        x_values.append(xnew)

        # Do not display values with small difference
        if math.fabs(xnew - xss) < .001:
            break
    beta = beta + 0.01

plt.title("Logistic map")
plt.scatter(beta_values, x_values, s=1, marker='.')
plt.show()
