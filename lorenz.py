x0 = 1
y0 = 1
z0 = 1

h = 0.01
s = 10
r = 28
b = 8/3

for i in range(30000):
    x1 = h*s*(y0-x0) + x0
    y1 = h*(x0*(r-z0)-y0) + y0
    z1 = h*(x0*y0 - b*z0) + z0
    x0 = x1
    y0 = y1
    z0 = z1
    print x1,y1,z1

# con gnuplot en 3d
# splot 'r.dat' with lines
# solo la primera coordenada
# plot 'r.dat' using 1 with lines
