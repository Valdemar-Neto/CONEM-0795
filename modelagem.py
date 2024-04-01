# -*- coding: utf-8 -*-
"""modelagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vDEPaN92WY4tuXrsbbFbN1GeMvmKzQfA
"""

import numpy as np
import matplotlib.pyplot as plt

def deslocamento(r, w, theta, l):
    """
    Calcula o deslocamento da manivela.

    Argumentos:
    r -- Valor de r
    w -- Valor de w (omega)
    theta -- Valor do ângulo (em graus)
    l -- Valor de l

    Retorna:
    O deslocamento calculado
    """
    result = r * np.cos(np.deg2rad(theta)) + np.sqrt(l ** 2 - r ** 2 * np.sin(np.deg2rad(theta)) ** 2)
    return result


def velocidade(r, w, theta, l):
    """
    Calcula a velociade da manivela.

    Argumentos:
    r -- Valor de r
    w -- Valor de w (omega)
    theta -- Valor do ângulo (em graus)
    l -- Valor de l

    Retorna:
    A velocidade da menivela
    """
    return -w * r * np.sin(np.deg2rad(theta)) - (w * r ** 2 * np.sin(np.deg2rad(theta)) * np.cos(np.deg2rad(theta))) / (np.sqrt(l ** 2 - r ** 2 * np.sin(np.deg2rad(theta)) ** 2))

def aceleracao(r, w, theta, l):
    """
    Calcula a aceleração da manivela.

    Argumentos:
    r -- Valor de r
    w -- Valor de w (omega)
    theta -- Valor do ângulo (em graus)
    l -- Valor de l

    Retorna:
    A aceleração da manivela
    """
    return -w**2 * r * np.sin(np.deg2rad(theta)) - (w **2* r ** 2 *(np.cos(np.deg2rad(theta))**2-np.sin(np.deg2rad(theta))**2)) / (np.sqrt(l ** 2 - r ** 2 * np.sin(np.deg2rad(theta)) ** 2))-(w **2 * r ** 4 * np.sin(np.deg2rad(theta))**2  * np.cos(np.deg2rad(theta))**2)/(np.sqrt((l ** 2 - r ** 2 * np.sin(np.deg2rad(theta)) ** 2)**3))

"""### Deslocamento

"""

# Valores dos parâmetros
w = 20 / 9.5492965964254
l = 230
theta_values = np.linspace(0, 360, 100)  # valores de ângulo (de 0 a 360 graus)
r_values = (
    1, 3, 15, 21
)
pontos =[14,15,19,1]
# Plot do gráfico para diferentes valores de r
for (r, p) in zip(r_values, pontos):
    deslocamentos = deslocamento(r, w, theta_values, l)
    plt.plot(theta_values, deslocamentos, label=f'P{p}, r={r}')


plt.xlabel('Ângulo (graus)')
plt.ylabel('Deslocamento (mm)')
plt.grid(True)
plt.legend()
plt.show()

# Valores dos parâmetros
w = 20 / 9.5492965964254
l = 230
theta_values = np.linspace(0, 360, 30)  # valores de ângulo (de 0 a 360 graus)
r_values = [1, 3, 16.5, 21, 17]  # raio
pontos =[14,15,19,0, 10]

# Plot do gráfico para diferentes valores de r
for (r, p) in zip(r_values, pontos):
    deslocamentos = deslocamento(r, w, theta_values, l)
    deslocamentos -= l  # Subtraindo l dos deslocamentos para ajustar a linha de 0 em y
    plt.plot(theta_values, deslocamentos, label=f'P{p}, r={r}')

des = deslocamento(16.5, w, theta_values, l)
print(des.max() - des.min())
plt.xlabel('Ângulo (graus)')
plt.ylabel('Deslocamento (mm)')
plt.grid(True)
plt.legend()


plt.text(200, -25, r'$r \cdot \cos(\theta) + \sqrt{l^2 - r^2 \cdot \sin^2(\theta)}$', fontsize=12)

plt.xlim(0, 400)  # Definindo os limites do eixo x
plt.ylim(-30,30)  # Definindo os limites do eixo y
plt.show()

"""### Velocidade"""

# Valores para os parâmetros
r = 15  # raio
w = 20/9.5492965964254  # frequência angular
theta_values = np.linspace(0, 360,  100)  # valores de ângulo (de 0 a 360 graus)
l = 230  # comprimento

# Calculando os valores de velocidade
velocities = velocidade(r, w, theta_values, l)
vel2 = velocidade(1,w,theta_values, l)
vel3 = velocidade(3,w, theta_values,l)
vel4 = velocidade(21, w, theta_values, l)

# Plotando o gráfico

plt.plot(theta_values, vel2, label=f'P{14}, r=1')
plt.plot(theta_values, vel3, label=f'P{15}, r=3')
plt.plot(theta_values, velocities, label=f'P{19}, r=19')
plt.plot(theta_values, vel4, label=f'P{0}, r=21')
plt.xlabel('Ângulo (graus)')
plt.ylabel('Velocidade (mm/s)')
plt.grid(True)

# Adicionando a equação ao gráfico
plt.text(130, -40, r'$v(\theta) = -w \cdot r \cdot \sin(\theta) - \frac{w \cdot r^2 \cdot \sin(\theta) \cdot \cos(\theta)}{\sqrt{l^2 - r^2 \cdot \sin^2(\theta)}}$', fontsize=12)

plt.legend()
plt.show()

# Valores para os parâmetros
r = [1, 3, 16.5, 21, 17]  # raio
w = 120/9.5492965964254  # frequência angular
theta_values = np.linspace(0, 360,  100)  # valores de ângulo (de 0 a 360 graus)
l = 230  # comprimento


# Calculando os valores de velocidade
velocities = velocidade(r[0], w, theta_values, l)
vel2 = velocidade(r[1],w,theta_values, l)
vel3 = velocidade(r[2],w, theta_values,l)
vel4 = velocidade(r[3], w, theta_values, l)
vel5 = velocidade(r[4], w, theta_values, l)

print(vel3.max())

# Plotando o gráfico

plt.plot(theta_values, velocities, label='P14, r=1')
plt.plot(theta_values, vel2, label='P15, r=3')
plt.plot(theta_values, vel3, label=f'P19, r=16,5')
plt.plot(theta_values, vel4, label='P0, r=21')
plt.plot(theta_values, vel5, label = 'P10, r = 17')
plt.xlabel('Ângulo (graus)')
plt.ylabel('Velocidade (mm/s)')
plt.grid(True)

# Adicionando a equação ao gráfico
plt.text(130, -250, r'$v(\theta) = -w \cdot r \cdot \sin(\theta) - \frac{w \cdot r^2 \cdot \sin(\theta) \cdot \cos(\theta)}{\sqrt{l^2 - r^2 \cdot \sin^2(\theta)}}$', fontsize=12)


plt.xlim(0, 400)  # Definindo os limites do eixo x
plt.ylim(-400, 400)  # Definindo os limites do eixo y

plt.legend()
plt.show()

"""### Aceleração"""

r = [1, 3, 16.5, 21, 17]  # raio
w = 120/9.5492965964254  # frequência angular
theta_values = np.linspace(0, 360,  100)  # valores de ângulo (de 0 a 360 graus)
l = 230  # comprimento


ac = aceleracao(r[0], w, theta_values, l)
ac2 = aceleracao(r[1],w,theta_values, l)
ac3 = aceleracao(r[2],w, theta_values,l)
ac4 = aceleracao(r[3], w, theta_values, l)
ac5 = aceleracao(r[4], w, theta_values, l)

print(ac3.max())


plt.plot(theta_values, ac, label='P14, r=1')
plt.plot(theta_values, ac2, label='P15, r=3')
plt.plot(theta_values, ac3, label=f'P19, r=16,5')
plt.plot(theta_values, ac4, label='P0, r=21')
plt.plot(theta_values, ac5, label = 'P10, r = 17')
plt.xlabel('Ângulo (graus)')
plt.ylabel('Aceleracao (mm/s²)')
plt.grid(True)
plt.legend(loc='best')

equation_text = r'$a(\theta) = -\omega^2 \cdot r \cdot \sin(\theta) - \frac{\omega^2 \cdot r^2 \cdot (\cos(\theta)^2-\sin(\theta)^2)}{\sqrt{l^2 - r^2 \cdot \sin(\theta)^2}} - \frac{\omega^2 \cdot r^4 \cdot \sin(\theta)^2 \cdot \cos(\theta)^2}{\sqrt{(l^2 - r^2 \cdot \sin(\theta)^2)^3}}$'
plt.text(200, -3500, equation_text, fontsize=11, ha='center')

plt.xlim(-10, 400)  # Definindo os limites do eixo x
plt.ylim(-4000, 4000)  # Definindo os limites do eixo y

plt.show()