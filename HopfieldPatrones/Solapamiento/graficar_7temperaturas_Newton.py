import numpy as np
import matplotlib.pyplot as plt

N=4900
datos = np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.1.txt")
datos1 = np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.0.txt")
datos2= np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.05.txt")
datos3= np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.07.txt")
datos4= np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.09.txt")
datos5= np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT0.08.txt")
datos6= np.loadtxt("HopfieldPatrones/Solapamiento/Newton/SolapamientoT1.0.txt")

patronuno=[]
patrondos=[]
patrontres=[]
patroncuatro=[]
patroncinco=[]
patronseis=[]
patronsiete=[]

T=[]

for i in range(0,len(datos),1):
    patronuno.append(datos[i])
    patrondos.append(datos1[i])
    patrontres.append(datos2[i])
    patroncuatro.append(datos3[i])
    patroncinco.append(datos4[i])
    patronseis.append(datos5[i])
    patronsiete.append(datos6[i])
    T.append(i)




fig, ax =plt.subplots()
#ax.set_title(r"Temperatura {kb(J/K) T(K)}")
ax.set_title(r"Patrón Newton a varia temperaturas")
ax.set_xlabel('1 Pasos Montecarlo(4900 neuronas)')
ax.set_ylabel('Solapamiento normalizado')
ax.plot(T,patrondos, marker='o',color='black', label="T=0.0")
ax.plot(T,patrontres, marker='o',color='purple', label="T=0.05")
ax.plot(T,patroncuatro, marker='o',color='brown', label="T=0.07")
ax.plot(T,patronseis, marker='o',color='blue', label="T=0.08")
ax.plot(T,patroncinco, marker='o',color='green', label="T=0.09")
ax.plot(T,patronuno, marker='o',color='orange', label="T=0.1")
ax.plot(T,patronsiete, marker='o',color='pink', label="T=1.0")
ax.legend()




plt.show()