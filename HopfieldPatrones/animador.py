import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.colors import ListedColormap




datos = np.loadtxt("HopfieldPatrones/Datos/Datos.txt")
N = 70
R=np.ones((N,N))

cmap=ListedColormap(["black","white"]) #azul para el 0 y rojo para el 1

fig, ax =plt.subplots()

im=ax.imshow(R, cmap=cmap, vmin=0, vmax=1, animated=True) # los vmin vmax es para identificar cada color con 0 o 1, animated=True ayuda a Blit=true con la memoria
tiempo=datos.size//(N*N)
print(datos.size)


def animate(i):
    for j in range(0,N,1):
        for k in range(0,N,1):
            p=j*N+k
            R[j,k]=datos[i,p] 
    im.set_array(R)
    return im,
      
anim = ani.FuncAnimation(fig, animate, interval=10, frames=tiempo, blit =True)
anim.save(filename="HopfieldPatrones/GIFs/prueba.gif", writer="pillow")
