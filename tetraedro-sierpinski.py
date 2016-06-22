import random

p1x=0
p1y=0
p1z=0
p2x=1
p2y=0
p2z=0
p3x=0
p3y=1
p3z=0
p4x=0
p4y=0
p4z=1

def midway(x,y):
    a=(1.0*x+y)/2
    return a

x0=0.1
y0=0.2
z0=0.3

for i in range(10000):
    r=int(4*random.random())+1
    if r==1:
        x1=midway(x0,p1x)
        y1=midway(y0,p1y)
        z1=midway(z0,p1z)
    elif r==2:
        x1=midway(x0,p2x)
        y1=midway(y0,p2y)
        z1=midway(z0,p2z)
    elif r==3:
        x1=midway(x0,p3x)
        y1=midway(y0,p3y)
        z1=midway(z0,p3z)
    else:
        x1=midway(x0,p4x)
        y1=midway(y0,p4y)
        z1=midway(z0,p4z)
    print '%10.4f' %x0, '%10.4f' %y0, '%10.4f' %z0
    x0=x1
    y0=y1
    z0=z1

