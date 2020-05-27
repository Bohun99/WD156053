#Zadanie 1

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax = fig.gca( projection = '3d' )

t = np.linspace( 0 , 2 * np.pi, 100 )
z = t
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x, y , z)
plt.show()

#Zadanie 2

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random


ax = plt.subplot(111, projection="3d")

color = ["r", "b", "m", "c", "g"]
marker = ["p", "h", "X", "D", "*"]

n = 20
for i in range(5):
    x = np.random.rand(n)
    y = np.random.rand(n)
    z = np.random.rand(n)
    ax.scatter(x, y, z, c=color[random.randint(0, 4)], marker=marker[random.randint(0, 4)])

ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
plt.show()

#Zadanie 3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np




X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
#1:
ax = plt.subplot(231, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.colorbar(surf, shrink = 0.5 , aspect = 5 )
#2:
ax = plt.subplot(232, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap =cm.bone,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.colorbar(surf, shrink = 0.5 , aspect = 5 )
#3:
ax = plt.subplot(233, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap =cm.copper,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.colorbar(surf, shrink = 0.5 , aspect = 5 )
#4:
ax = plt.subplot(234, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap =cm.winter,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.colorbar(surf, shrink = 0.5 , aspect = 5 )
#5:
ax = plt.subplot(235, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap =cm.binary,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.colorbar(surf, shrink = 0.5 , aspect = 5 )

plt.show()
