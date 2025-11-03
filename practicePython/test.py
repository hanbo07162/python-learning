import matplotlib.pyplot as plt
import numpy as np  
# 创建2个子图
plt.subplot(2, 1, 1)  # 
x=np.array(np.linspace(0,10,100))
plt.plot(x, np.sin(x))
ax1 = plt.gca()  # 获取第1个子图的坐标轴
ax1.set_title('Sin(x)')

plt.subplot(2,1,2)  # 第2个子图
plt.plot(x, np.cos(x))
ax2 = plt.gca()  # 获取第2个子图的坐标轴
ax2.set_title('Cos(x)')

plt.tight_layout()  # 调整布局
plt.show()