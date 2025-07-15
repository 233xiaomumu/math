import numpy as np
import scipy
import scipy.interpolate
import matplotlib.pyplot as plt
x=[2,3,5,6,7,8,10]
y=[7.5,6.9,9,11.7,18.6,20.8,15.6]
xnew=np.arange(2,10.5,0.5)
f_line= scipy.interpolate.interp1d(x,y)
f_linear = scipy.interpolate.interp1d(x, y)  # 默认线性插值
f_cubic = scipy.interpolate.interp1d(x, y, kind='cubic')  # 三次样条插值
f_nearest = scipy.interpolate.interp1d(x, y, kind='nearest')  # 最近邻插值

print(f_linear(9))

plt.plot(x,y,'o')
plt.plot(xnew,f_linear(xnew))
plt.plot(xnew,f_cubic(xnew))
plt.show()