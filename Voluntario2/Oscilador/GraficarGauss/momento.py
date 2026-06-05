import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt("Voluntario2/Oscilador/DatosGaussCentrada/p_esperado.txt")

resultado=[]
w=200
sigma=1.0/10
xo=0.5
s=7.03619e-05
equilibrio=0.5
xc=equilibrio-np.sqrt(sigma*sigma/2.0 + (xo-equilibrio)*(xo-equilibrio))
pc=np.sqrt(1/(2.0*sigma*sigma))

Teorico=[]
for i in range(0,len(datos),1):
    resultado.append(datos[i])
    Teorico.append(pc*np.cos(w*i*s)-w*(xc-equilibrio)*np.sin(w*i*s)/2)
T=np.arange(0,len(datos),1)*5000.0/(len(datos)-1)
fig, ax =plt.subplots()
#ax.set_title('')
print(T.shape)
print(len(datos))
ax.set_xlabel('Tiempo(0.0001)')
ax.set_ylabel('<x>')

#ax.set(ylim=[0,1.5]) #comentar para ver crecimiento debido error numerico
ax.scatter(T,resultado, label='Simulación')
ax.plot(T,Teorico, color='red', label='Teórico')
ax.set_title('Onda inicial Gaussiana x0=0.3')
ax.legend()


plt.show()
fig.savefig("Voluntario2/Imagenes/GaussianaCentrada/P.png")