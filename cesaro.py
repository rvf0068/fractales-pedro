import random
import cmath
a=0.4+0.4j
z0=0.2+0.1j
for i in range(100000):
    r = int(100*random.random()) + 1
    if r <= 50:
        z1 = a*z0
    else:
        z1 = a + (1-a)*z0
    print '%10.4f' %z0.real, '%10.4f' %z0.imag
    z0=z1
