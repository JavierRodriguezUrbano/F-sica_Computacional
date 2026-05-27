import numpy as np
import matplotlib.pyplot as plt

N=4900   
datos = np.loadtxt("HopfieldPatrones/Solapamiento/LosTresFísicos/SolapamientoT0.0.txt")
datos1= np.loadtxt("HopfieldPatrones/Solapamiento/LosTresFísicos/SolapamientoT0.001.txt")
datos2= np.loadtxt("HopfieldPatrones/Solapamiento/LosTresFísicos/SolapamientoT0.01.txt")
datos3= np.loadtxt("HopfieldPatrones/Solapamiento/LosTresFísicos/SolapamientoT0.1.txt")
patronuno=[]
patrondos=[]
patrontres=[]
patronuno1=[]
patrondos1=[]
patrontres1=[]
patronuno2=[]
patrondos2=[]
patrontres2=[]
patronuno3=[]
patrondos3=[]
patrontres3=[]
T=[]

for i in range(0,len(datos),1):
    patronuno.append(datos[i][0])
    patrondos.append(datos[i][1])
    patrontres.append(datos[i][2])
    patronuno1.append(datos1[i][0])
    patrondos1.append(datos1[i][1])
    patrontres1.append(datos1[i][2])
    patronuno2.append(datos2[i][0])
    patrondos2.append(datos2[i][1])
    patrontres2.append(datos2[i][2])
    patronuno3.append(datos3[i][0])
    patrondos3.append(datos3[i][1])
    patrontres3.append(datos3[i][2])
    T.append(i)




fig, ax =plt.subplots(2,2,figsize=(5,5))
ax[0,0].set_title(r"Temperatura 0.0{kb(J/K) T(K)}")
ax[0,0].set_xlabel('0,5 Pasos Montecarlo(2450 neuronas)')
ax[0,0].set_ylabel('Solapamiento normalizado')
ax[0,0].plot(T,patronuno, marker='o',color='blue', label="Newton")
ax[0,0].plot(T,patrondos, marker='o',color='red', label="Maxwell")
ax[0,0].plot(T,patrontres, marker='o',color='green', label="Einstein")
ax[0,0].legend()


ax[1,0].set_title(r"Temperatura 0.01{kb(J/K) T(K)}")
ax[1,0].set_xlabel('0,5 Pasos Montecarlo(2450 neuronas)')
ax[1,0].set_ylabel('Solapamiento normalizado')
ax[1,0].plot(T,patronuno2, marker='o',color='blue', label="Newton")
ax[1,0].plot(T,patrondos2, marker='o',color='red', label="Maxwell")
ax[1,0].plot(T,patrontres2, marker='o',color='green', label="Einstein")
ax[1,0].legend()


ax[0,1].set_title(r"Temperatura 0.001{kb(J/K) T(K)}")
ax[0,1].set_xlabel('0,5 Pasos Montecarlo(2450 neuronas)')
ax[0,1].set_ylabel('Solapamiento normalizado')
ax[0,1].plot(T,patronuno1, marker='o',color='blue', label="Newton")
ax[0,1].plot(T,patrondos1, marker='o',color='red', label="Maxwell")
ax[0,1].plot(T,patrontres1, marker='o',color='green', label="Einstein")
ax[0,1].legend()

ax[1,1].set_title(r"Temperatura 0.1{kb(J/K) T(K)}")
ax[1,1].set_xlabel('0,5 Pasos Montecarlo(2450 neuronas)')
ax[1,1].set_ylabel('Solapamiento normalizado')
ax[1,1].plot(T,patronuno3, marker='o',color='blue', label="Newton")
ax[1,1].plot(T,patrondos3, marker='o',color='red', label="Maxwell")
ax[1,1].plot(T,patrontres3, marker='o',color='green', label="Einstein")
ax[1,1].legend()

plt.tight_layout()
plt.show()