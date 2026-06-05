import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt("Voluntario2/Oscilador/Datos0/Heisenberg_esperado.txt")
datos1 = np.loadtxt("Voluntario2/Oscilador/Datos1/Heisenberg_esperado.txt")
datos2 = np.loadtxt("Voluntario2/Oscilador/Datos2/Heisenberg_esperado.txt")
datos3 = np.loadtxt("Voluntario2/Oscilador/Datos3/Heisenberg_esperado.txt")
resultado=[]
resultado1=[]
resultado2=[]
resultado3=[]
Teorico=[]
Teorico1=[]
Teorico2=[]
Teorico3=[]

w=200
for i in range(0,len(datos),1):
    resultado.append(datos[i])
    resultado1.append(datos1[i])
    resultado2.append(datos2[i])
    resultado3.append(datos3[i])
    Teorico.append(0.5)
    Teorico1.append(1.5)
    Teorico2.append(2.5)
    Teorico3.append(3.5)
T=np.arange(0,len(datos),1)*5000.0/(len(datos)-1.0)
fig, ax =plt.subplots(2,2)
#ax.set_title('')
print(T.shape)
print(len(datos))
ax[0,0].set_xlabel('Tiempo(0.0001)')
ax[0,1].set_xlabel('Tiempo(0.0001)')
ax[1,0].set_xlabel('Tiempo(0.0001)')
ax[1,1].set_xlabel('Tiempo(0.0001)')
ax[0,0].set_ylabel('Δ x Δ p')
ax[1,0].set_ylabel('Δ x Δ p')
ax[0,1].set_ylabel('Δ x Δ p')
ax[1,1].set_ylabel('Δ x Δ p')
#ax.set(ylim=[0,1.5]) #comentar para ver crecimiento debido error numerico
ax[0,0].scatter(T,resultado, label='Simulación')
ax[0,1].scatter(T,resultado1, label='Simulación')
ax[1,0].scatter(T,resultado2, label='Simulación')
ax[1,1].scatter(T,resultado3, label='Simulación')

ax[0,0].plot(T,Teorico, color='red', label='Teórico')
ax[0,1].plot(T,Teorico1, color='red', label='Teórico')
ax[1,0].plot(T,Teorico2, color='red', label='Teórico')
ax[1,1].plot(T,Teorico3, color='red', label='Teórico')

ax[0,0].set_title('Autofunción n=0')
ax[0,1].set_title('Autofunción n=1')
ax[1,0].set_title('Autofunción n=2')
ax[1,1].set_title('Autofunción n=3')

ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()

plt.tight_layout()
plt.show()
fig.savefig("Voluntario2/Imagenes/Estacionarios/Heisenberg.png")