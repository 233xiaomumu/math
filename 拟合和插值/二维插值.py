import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 原始数据#test
x = np.arange(1, 6)        # x方向: 1-5
y = np.arange(1, 4)        # y方向: 1-3
temps = np.array([
    [82, 81, 80, 82, 84],
    [79, 63, 61, 65, 81],
    [84, 84, 82, 85, 86]
])

# 创建网格坐标
X, Y = np.meshgrid(x, y)

# 绘制原始数据 - 3D曲面和散点
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111, projection='3d')

# 绘制网格面
ax1.plot_wireframe(X, Y, temps, color='b', linewidth=0.5)

# 绘制散点（红色实心点）
ax1.scatter(X.flatten(), Y.flatten(), temps.flatten(), 
            c='r', s=50, depthshade=True)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Temperature')
ax1.set_title('Original Temperature Data')
ax1.set_xlim(1, 5)
ax1.set_ylim(1, 3)
ax1.view_init(30, 45)
plt.tight_layout()
plt.show()

# 插值处理 - 使用 griddata 替代 RectBivariateSpline
xi = np.linspace(1, 5, 21)    # x方向插值点 (1-5, 21个点)
yi = np.linspace(1, 3, 11)    # y方向插值点 (1-3, 11个点)

# 准备插值点
points = np.array([(i, j) for j in y for i in x])
values = temps.flatten()

# 创建插值网格
Xi, Yi = np.meshgrid(xi, yi)

# 进行三次样条插值
Zi = griddata(points, values, (Xi, Yi), method='cubic')

# 绘制插值后的曲面
fig2 = plt.figure(figsize=(10, 6))
ax2 = fig2.add_subplot(111, projection='3d')

# 绘制光滑曲面
surf = ax2.plot_surface(Xi, Yi, Zi, cmap='viridis', alpha=0.8, edgecolor='none')

# 添加颜色条
fig2.colorbar(surf, ax=ax2, shrink=0.5, aspect=5, label='Temperature')

# 添加原始数据点
ax2.scatter(X.flatten(), Y.flatten(), temps.flatten(), 
           c='r', s=50, depthshade=True)

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Temperature')
ax2.set_title('Interpolated Temperature Surface (Cubic Spline)')
ax2.view_init(30, 45)
plt.tight_layout()
plt.show()