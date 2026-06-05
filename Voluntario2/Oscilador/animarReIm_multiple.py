import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

datos0r=np.loadtxt("Voluntario2/Oscilador/Datos0/real.txt")
datos0i=np.loadtxt("Voluntario2/Oscilador/Datos0/imaginario.txt")
datos1r=np.loadtxt("Voluntario2/Oscilador/Datos1/real.txt")
datos1i=np.loadtxt("Voluntario2/Oscilador/Datos1/imaginario.txt")
datos2r=np.loadtxt("Voluntario2/Oscilador/Datos2/real.txt")
datos2i=np.loadtxt("Voluntario2/Oscilador/Datos2/imaginario.txt")
datos3r=np.loadtxt("Voluntario2/Oscilador/Datos3/real.txt")
datos3i=np.loadtxt("Voluntario2/Oscilador/Datos3/imaginario.txt")

N=5000
h=1/N


R=[np.zeros(N+1) for _ in range(4)]
I=[np.zeros(N+1) for _ in range(4)]
x=np.arange(0,N+1,1)

fig, ax =plt.subplots(2,2)

onda0, =ax[0,0].plot(x,R[0], label='Real') 
imagen0, =ax[0,0].plot(x,I[0], color='red', label='Imaginaria')
onda1, =ax[0,1].plot(x,R[1], label='Real') 
imagen1, =ax[0,1].plot(x,I[1], color='red', label='Imaginaria')
onda2, =ax[1,0].plot(x,R[2], label='Real') 
imagen2, =ax[1,0].plot(x,I[2], color='red', label='Imaginaria')
onda3, =ax[1,1].plot(x,R[3], label='Real') 
imagen3, =ax[1,1].plot(x,I[3], color='red', label='Imaginaria')
tiempo=datos0r.shape[0]
l=0
for k in range(0,2):
      for j in range(0,2):
        ax[k,j].set_xlabel('x (0.0001)')
        ax[k,j].set_ylabel('Onda')
        ax[k,j].set(ylim=[-3,3])
        ax[k,j].set_title(f'Estado estacionario n={l}')
        ax[k,j].legend(loc='upper right')
        l=l+1

plt.tight_layout()
#V = np.zeros(N + 1)

#V[:] = (2 * np.pi * nciclos / N)**2 * (0.6)

#ax.plot(x, V, color='red', lw=1.5, label='Contorno del Potencial', linestyle='--')


def animate(i):
    for j in range(0,N+1,1):
            R[0][j]=datos0r[i,j]
            R[1][j]=datos1r[i,j]
            R[2][j]=datos2r[i,j]
            R[3][j]=datos3r[i,j]
            I[0][j]=datos0i[i,j]
            I[1][j]=datos1i[i,j]
            I[2][j]=datos2i[i,j]
            I[3][j]=datos3i[i,j]
    onda0.set_ydata(R[0])
    onda1.set_ydata(R[1])
    onda2.set_ydata(R[2])
    onda3.set_ydata(R[3])
    imagen0.set_ydata(I[0])
    imagen1.set_ydata(I[1])
    imagen2.set_ydata(I[2])
    imagen3.set_ydata(I[3])
    return onda0,imagen0,onda1,imagen1,onda2,imagen2,onda3,imagen3,
      
anim = ani.FuncAnimation(fig, animate, interval=50, frames=tiempo)
anim.save(filename="Voluntario2/Imagenes/Estacionarios/RealImaginario_5000_nc30.gif", writer="pillow")