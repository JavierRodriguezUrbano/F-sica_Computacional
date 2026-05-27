import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


N=4900  #si se quiere cambiar a solapamientos de otro conjunto de patrones cambiar a los guardados en Aleatorios
datos = np.loadtxt("HopfieldPatrones/Solapamiento/Solapamiento.txt")


cmap=plt.cm.inferno

patron1=[]


T=[]

for i in range(0,len(datos),1):
    patron1.append(datos[i])
    T.append(i)




fig, ax =plt.subplots()
#ax.set_title(r"Temperatura {kb(J/K) T(K)}")
ax.set_title(r"Solapamiento para 100 patrones a T=0.0001")
ax.set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax.set_ylabel('Solapamiento normalizado')
for i in range(0,datos.shape[1],1):
    color = cmap(i / datos.shape[1])
    ax.plot(T,datos[:,i], marker='o',color=color)



plt.show()