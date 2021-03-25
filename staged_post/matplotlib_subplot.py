import matplotlib.pyplot as plt
import numpy as np

# Functions
x = np.linspace(0,np.pi)
y_1 = np.sin(x)
y_2 = np.sin(x) + np.random.normal(0,0.1,50)
y_3 = np.sin(x) + np.random.uniform(-0.1,0.1,50)
y_4 = np.sin(x) + np.random.normal(0,0.01,50)


## Same Partition
plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
plt.title('subtitle_one')
plt.plot(x,y_1)
plt.subplot(2,2,2)
plt.plot(x,y_2)
plt.title('subtitle_two')
plt.subplot(2,2,3)
plt.plot(x,y_3)
plt.title('subtitle_three')
plt.subplot(2,2,4)
plt.plot(x,y_4)
plt.title('subtitle_four')
plt.suptitle('SUPTITLE', fontsize = 20)
plt.savefig('../img/subplot_same_partition.png')

## Flexible Partition
plt.figure(figsize = (10,10))
plt.subplot(2,1,1)
plt.title('subtitle_one')
plt.plot(x,y_1)
plt.subplot(2,3,4)
plt.plot(x,y_2)
plt.title('subtitle_two')
plt.subplot(2,3,5)
plt.plot(x,y_3)
plt.title('subtitle_three')
plt.subplot(2,3,6)
plt.plot(x,y_4)
plt.title('subtitle_four')
plt.suptitle('SUPTITLE', fontsize = 20)
plt.savefig('../img/subplot_flexible_partition.png')