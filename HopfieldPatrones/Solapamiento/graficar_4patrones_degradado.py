import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


N=4900  #si se quiere cambiar a solapamientos de otro conjunto de patrones cambiar a los guardados en Aleatorios
datos = np.loadtxt("HopfieldPatrones/Solapamiento/Aleatorios/Solapamiento20.txt")
datos3 = np.loadtxt("HopfieldPatrones/Solapamiento/Aleatorios/Solapamiento30.txt")
datos5 = np.loadtxt("HopfieldPatrones/Solapamiento/Aleatorios/Solapamiento40.txt")
datos10 = np.loadtxt("HopfieldPatrones/Solapamiento/Aleatorios/Solapamiento50.txt")

cmap=plt.cm.inferno

patron1=[]


T=[]

for i in range(0,len(datos),1):
    patron1.append(datos[i])
    T.append(i)




fig, ax =plt.subplots(2,2)
#ax.set_title(r"Temperatura {kb(J/K) T(K)}")
ax[0,0].set_title(r"Solapamiento para 20 patrones a T=0.0001")
ax[0,0].set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax[0,0].set_ylabel('Solapamiento normalizado')
for i in range(0,datos.shape[1],1):
    color = cmap(i / datos.shape[1])
    ax[0,0].plot(T,datos[:,i], marker='o',color=color)


ax[0,1].set_title(r"Solapamiento para 30 patrones a T=0.0001")
ax[0,1].set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax[0,1].set_ylabel('Solapamiento normalizado')
for i in range(0,datos3.shape[1],1):
    color = cmap(i / datos3.shape[1])
    ax[0,1].plot(T,datos3[:,i], marker='o',color=color)

ax[1,0].set_title(r"Solapamiento para 40 patrones a T=0.0001")
ax[1,0].set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax[1,0].set_ylabel('Solapamiento normalizado')
for i in range(0,datos5.shape[1],1):
    color = cmap(i / datos5.shape[1])
    ax[1,0].plot(T,datos5[:,i], marker='o',color=color)

ax[1,1].set_title(r"Solapamiento para 50 patrones a T=0.0001")
ax[1,1].set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax[1,1].set_ylabel('Solapamiento normalizado')
for i in range(0,datos10.shape[1],1):
    color = cmap(i / datos10.shape[1])
    ax[1,1].plot(T,datos10[:,i], marker='o',color=color)




plt.tight_layout()
plt.show()