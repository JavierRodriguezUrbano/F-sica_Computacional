import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


datos0=np.loadtxt("Voluntario2/Oscilador/Datos0/probabilidad.txt")
datos1=np.loadtxt("Voluntario2/Oscilador/Datos1/probabilidad.txt")
datos2=np.loadtxt("Voluntario2/Oscilador/Datos2/probabilidad.txt")
datos3=np.loadtxt("Voluntario2/Oscilador/Datos3/probabilidad.txt")
Teorico=[[] for _ in range(4)]

N=5000
h=1.0/N
w=200
E=[w*(0+1.0/2),w*(1+1.0/2),w*(2+1.0/2),w*(3+1.0/2)]
xo=[4.0*E[0]/(w*w),4.0*E[1]/(w*w),4.0*E[2]/(w*w),4.0*E[3]/(w*w)]
equilibrio=0.5
Pi=3.14159265359
limite=0.01

R=[np.zeros(N) for _ in range(4)]

x=np.arange(0,N,1)
for k in range(0,4):
    for j in range(0,N,1):
        if (xo[k]-(j*h-equilibrio)**2)<=0:
               Teorico[k].append(limite)
        else:
            Teorico[k].append(h/((Pi)*(np.sqrt(xo[k]-(j*h-equilibrio)**2))))

fig, ax =plt.subplots(2,2)
l=0

onda0, =ax[0,0].plot(x,R[0])
clasico0, =ax[0,0].plot(x,Teorico[0]) 
onda1, =ax[0,1].plot(x,R[1])
clasico1, =ax[0,1].plot(x,Teorico[1]) 
onda2, =ax[1,0].plot(x,R[2])
clasico2, =ax[1,0].plot(x,Teorico[2]) 
onda3, =ax[1,1].plot(x,R[3])
clasico3, =ax[1,1].plot(x,Teorico[3]) 
for k in range(0,2):
     for j in range(0,2):
        ax[k,j].set_xlabel('x (0.0001)')
        ax[k,j].set_ylabel('Probabilidad')
        ax[k,j].set_title(f'Estado estacionario n={l}')
        ax[k,j].set(ylim=[0,limite])
        l=l+1
plt.tight_layout()
tiempo=datos0.shape[0]

#V = np.zeros(N + 1)

#V[:] = (2 * np.pi * nciclos / N)**2 * (0.6)

#ax.plot(x, V, color='red', lw=1.5, label='Contorno del Potencial', linestyle='--')
#ax.legend(loc='upper right')


def animate(i):
    for j in range(0,N-1,1):
            R[0][j]=datos0[i,j]
            R[1][j]=datos1[i,j]
            R[2][j]=datos2[i,j]
            R[3][j]=datos3[i,j]
    onda0.set_ydata(R[0])
    onda1.set_ydata(R[1])
    onda2.set_ydata(R[2])
    onda3.set_ydata(R[3])
    return onda0,clasico0,onda1,clasico1,onda2,clasico2,onda3,clasico3,
      
anim = ani.FuncAnimation(fig, animate, interval=50, frames=tiempo)
anim.save(filename="Voluntario2/Imagenes/Estacionarios/Probabilidad_5000_nc30.gif", writer="pillow")