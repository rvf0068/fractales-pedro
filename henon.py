x0 = 1
y0 = 1
a = 1.4
b = 0.3
for i in range(500000):
    x1 = 1 - a*x0*x0 + y0
    y1 = b*x0
    x0 = x1
    y0 = y1
    print x1, y1
