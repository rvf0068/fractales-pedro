import random

p1x=-0.5
p1y=0
p2x=0.5
p2y=0
p3x=0
p3y=1

def midway(x,y):
    a=(1.0*x+y)/2
    return a

x0=0
y0=0.5

for i in range(100000):
    r=int(3*random.random())+1
    if r==1:
        x1=midway(x0,p1x)
        y1=midway(y0,p1y)
    elif r==2:
        x1=midway(x0,p2x)
        y1=midway(y0,p2y)
    else:
        x1=midway(x0,p3x)
        y1=midway(y0,p3y)
    print '%10.4f' %x0, '%10.4f' %y0
    x0=x1
    y0=y1

