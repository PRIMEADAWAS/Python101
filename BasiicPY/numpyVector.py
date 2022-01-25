import numpy as np
import math
from numpy import (dot, arccos, clip)
from numpy.linalg import norm

u = [2, 0]
v = [1, 0]
c = dot(u, v)/norm(u)/norm(v)  # -> cosine of the angle
angle = arccos(clip(c, -1, 1))  # if you really want the angle
degree = angle * 180 / math.pi
print(degree)
