import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi)
y = np.sin(x)

plt.plot(x,y)

title = 'sin(x)'

plt.title(title)
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.show()
