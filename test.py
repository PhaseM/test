import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, tan
m = np.random.random([100,100])
for i, v in np.ndenumerate(m):
    x = i[0]
    y = i[1]
    m[x,y] += sin(x/10)*5+cos(y/10)*5
plt.imshow(m)
plt.show()