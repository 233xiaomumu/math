import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.interpolate
x0=np.arange(0,1.2,0.2)
y0=np.array([5,4.71,4.31,4,3.9,3.5])

y0new=np.arange(5,3.5,-0.05)
xnew=-y0new

x=-y0
y=x0

plt.plot(x,y)

cub=scipy.interpolate.CubicSpline(x,y)
y_cub=cub(xnew)

plt.plot(xnew,y_cub)

plt.show()
