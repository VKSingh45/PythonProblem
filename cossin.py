import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,20,0.1)
a=np.cos(x)
b=np.sin(x)
plt.plot(a,a,'b')
plt.plot(b,a,'y')
plt.show()
