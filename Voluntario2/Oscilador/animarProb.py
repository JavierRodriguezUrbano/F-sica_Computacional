import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


datos=np.loadtxt("Voluntario2/Oscilador/DatosGaussCentrada/probabilidad.txt")
Teorico=[]

N=5000
h=1.0/N
w=200
n=20
E=w*(n+1.0/2)
xo=4.0*E/(w*w)
equilibrio=0.5
Pi=3.14159265359
limite=0.01

R=np.zeros(N)

x=np.arange(0,N,1)

for j in range(0,N,1):
        if (xo-(j*h-equilibrio)**2)<=0:
               Teorico.append(limite)
        else:
            Teorico.append(h/((Pi)*(np.sqrt(xo-(j*h-equilibrio)**2))))

fig, ax =plt.subplots()

onda, =ax.plot(x,R) # los vmin vmax es para identificar cada color con 0 o 1, animated=True ayuda a Blit=true con la memoria
#clasico, =ax.plot(x,Teorico) # los vmin vmax es para identificar cada color con 0 o 1, animated=True ayuda a Blit=true con la memoria
tiempo=datos.shape[0]
ax.set_xlabel('x (0.0001)')
ax.set_ylabel('Probabilidad')
#ax.set(ylim=[-0.05,0.05])
ax.set(ylim=[0,limite])

#V = np.zeros(N + 1)

#V[:] = (2 * np.pi * nciclos / N)**2 * (0.6)

#ax.plot(x, V, color='red', lw=1.5, label='Contorno del Potencial', linestyle='--')
#ax.legend(loc='upper right')


def animate(i):
    for j in range(0,N-1,1):
            R[j]=datos[i,j]
    onda.set_ydata(R)
    return onda,
      
anim = ani.FuncAnimation(fig, animate, interval=50, frames=tiempo)
anim.save(filename="Voluntario2/Imagenes/GaussianaCentrada/Probabilidad.gif", writer="pillow")