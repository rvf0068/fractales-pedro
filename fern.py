import random


x0=0
y0=0

for i in range(350000):
	
	r=int(100*random.random())+1
	
	if r==1:
		x1=0
		y1=0.16*y0
	elif r<=8:
		x1=0.2*x0-0.26*y0
		y1=0.23*x0+0.22*y0+1.6
	elif r<=15:
		x1=-0.15*x0+0.28*y0
		y1=0.26*x0+0.24*y0+0.44
	else:
		x1=0.85*x0+0.04*y0
		y1=-0.04*x0+0.85*y0+1.6
	print '%10.4f' %x0,'%10.4f' %y0	   
	x0=x1
	y0=y1
	