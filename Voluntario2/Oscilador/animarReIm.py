import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

datos=np.loadtxt("Voluntario2/Oscilador/DatosGaussCentrada/real.txt")
datos1=np.loadtxt("Voluntario2/Oscilador/DatosGaussCentrada/imaginario.txt")

N=5000
h=1/N


R=np.zeros(N+1)
R1=np.zeros(N+1)
x=np.arange(0,N+1,1)

fig, ax =plt.subplots()

onda, =ax.plot(x,R, label='Real') # los vmin vmax es para identificar cada color con 0 o 1, animated=True ayuda a Blit=true con la memoria
onda1, =ax.plot(x,R1, color='red', label='Imaginaria')
tiempo=datos.shape[0]
ax.set_xlabel('x (0.0001)')
ax.set_ylabel('Phi')
ax.set_title('Onda Gaussiana centrada')
#ax.set(ylim=[-0.05,0.05])
ax.set(ylim=[-3,3])

#V = np.zeros(N + 1)

#V[:] = (2 * np.pi * nciclos / N)**2 * (0.6)

#ax.plot(x, V, color='red', lw=1.5, label='Contorno del Potencial', linestyle='--')
ax.legend(loc='upper right')


def animate(i):
    for j in range(0,N+1,1):
            R[j]=datos[i,j]
            R1[j]=datos1[i,j]
    onda.set_ydata(R)
    onda1.set_ydata(R1)
    return R,R1,
      
anim = ani.FuncAnimation(fig, animate, interval=50, frames=tiempo)
anim.save(filename="Voluntario2/Imagenes/GaussianaCentrada/RealImaginaria.gif", writer="pillow")