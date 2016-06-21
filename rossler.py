x0 = 1
y0 = 1
z0 = 1
h = 0.01
a = 0.1
b = 0.1
c = 14

for i in range(30000):
    x1 = h*(-y0-z0) + x0
    y1 = h*(x0+a*y0) + y0
    z1 = h*(b+z0*(x0-c)) + z0
    x0 = x1
    y0 = y1
    z0 = z1
    print x1,y1,z1
