# mymath package implementation
class MyMath:
    @staticmethod
    def power(x, n):
        res = 1
        for i in range(n):
            res *= x
        return res

    @staticmethod
    def factorial(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


# Calculate cos(x) using Maclaurin series
def cos_maclaurin(x, n_terms):
    cos_x = 0
    for k in range(n_terms):
        sign = (-1) ** k
        numerator = MyMath.power(x, 2 * k)
        denominator = MyMath.factorial(2 * k)
        term = sign * numerator / denominator
        cos_x += term
    return cos_x


# Plot the series with matplotlib
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-10, 10, 1000)
y_values = np.cos(x_values)
plt.plot(x_values, y_values, label='cos(x)')

n_terms = 10
y_values_approx = np.zeros_like(x_values)
for i, x in enumerate(x_values):
    y_values_approx[i] = cos_maclaurin(x, n_terms)
plt.plot(x_values, y_values_approx, label=f'cos(x) approx. ({n_terms} terms)')

plt.legend()
plt.show()
