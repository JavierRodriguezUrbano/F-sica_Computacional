import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt("Voluntario2/Oscilador/DatosGaussCentrada/Heisenberg_esperado.txt")

resultado=[]

Teorico=[]
for i in range(0,len(datos),1):
    resultado.append(datos[i])
    Teorico.append(0.5)
T=np.arange(0,len(datos),1)*5000.0/(len(datos)-1)
fig, ax =plt.subplots()
#ax.set_title('')
print(T.shape)
print(len(datos))
ax.set_xlabel('Tiempo(0.0001)')
ax.set_ylabel('Δ x Δ p')

#ax.set(ylim=[0,1.5]) #comentar para ver crecimiento debido error numerico
ax.scatter(T,resultado, label='Simulación')
ax.plot(T,Teorico, color='red', label='Teórico')
ax.set_title('Onda inicial Gaussiana')
ax.legend()


plt.show()
fig.savefig("Voluntario2/Imagenes/GaussianaCentrada/Heisenberg.png")