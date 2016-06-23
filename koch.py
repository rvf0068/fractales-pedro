import random
import cmath
a=0.6+0.37j
z0=0.2+0.1j
for i in range(100000):
    r = int(100*random.random()) + 1
    if r <= 50:
        z1 = a*z0.conjugate()
    else:
        z1 = a + (1-a)*z0.conjugate()
    print '%10.4f' %z0.real, '%10.4f' %z0.imag
    z0=z1
