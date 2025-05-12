import matplotlib.pyplot as plt

alturas = [150, 185, 160, 190, 175, 172]
pesos = [60, 100, 70, 120, 80, 65]

plt.bar(alturas, pesos)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso')
plt.show()