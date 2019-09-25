#RAHUL KUKREJA
#ROLL NO.- 2018254
#SECTION B GROUP 7

import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Ellipse

def mul_matrix(a,b):
	c=[]
	for i in range(len(a)):
		c.append([])
		for k in range(len(b[0])):
			p=0
			for j in range(len(a[0])):
				p=p+(a[i][j]*b[j][k])
			c[i].append(p)

	return c

def string_to_list(s):
	l= s.split(" ")
	for i in range(len(l)):
		l[i]=float(l[i])

	return l

def scale(x,y,sx,sy):
	xs,ys=[],[]
	s=[[sx,0,0],[0,sy,0],[0,0,1]]
	for i in range(len(x)):
		c=[[x[i]],[y[i]],[1]]
		l=mul_matrix(s,c)
		xs.append(l[0][0])
		ys.append(l[1][0])

	return (xs,ys)

def rotate(x,y,theta):
	xr,yr=[],[]
	theta=math.radians(theta)
	r=[[math.cos(theta),-1*math.sin(theta),0],[math.sin(theta),math.cos(theta),0],[0,0,1]]
	for i in range(len(x)):
		c=[[x[i]],[y[i]],[1]]
		l=mul_matrix(r,c)
		xr.append(round(l[0][0],2))
		yr.append(round(l[1][0],2))

	return (xr,yr)

def translate(x,y,dx,dy):
	xt,yt=[],[]
	t=[[1,0,dx],[0,1,dy],[0,0,1]]
	for i in range(len(x)):
		c=[[x[i]],[y[i]],[1]]
		l=mul_matrix(t,c)
		xt.append(l[0][0])
		yt.append(l[1][0])

	return (xt,yt)

def draw_polygon(x,y):
	x.append(x[0]);y.append(y[0])
	plt.plot(x,y)
	plt.pause(0.0001)
	x.pop(len(x)-1);y.pop(len(y)-1)

def draw_circle(xy,width,height,angle):
	#plt.gcf().clear()
	xy=tuple(xy)
	ellipse=Ellipse(xy=xy, width=width, height=height,angle=angle,fill=False)
	plt.gca().add_patch(ellipse)
	plt.axis('scaled')
	plt.pause(0.0001)

plt.ion()
object_shape=input()
if object_shape=='disc':
	s=input()
	xt,xs,yt,ys=[],[],[],[]
	xt.append(int(s[0]))
	yt.append(int(s[2]))
	xs.append(int(s[4]))
	ys.append(int(s[4]))
	command=''
	angle=0
	draw_circle(xt+yt,2*xs[0],2*ys[0],angle)
	while command!='quit':
		command=input()
		if command!='quit':
			cmd=string_to_list(command[2:])
			if command[0]=='S':
				xs,ys=scale(xs,ys,cmd[0],cmd[1])
				draw_circle(xt+yt,2*xs[0],2*ys[0],angle)
			elif command[0]=='R':
				xt,yt=rotate(xt,yt,cmd[0])
				draw_circle(xt+yt,2*xs[0],2*ys[0],angle+cmd[0])
				angle= angle+cmd[0]
			elif command[0]=='T':
				xt,yt=translate(xt,yt,cmd[0],cmd[1])
				draw_circle(xt+yt,2*xs[0],2*ys[0],angle)

		print(''.join(map(str,xt))+" "+''.join(map(str,yt))+" "+''.join(map(str,xs))+" "+''.join(map(str,ys)))

if object_shape=='polygon':
	x1=input()
	y1=input()
	x=string_to_list(x1)
	y=string_to_list(y1)
	draw_polygon(x,y)
	command=''
	while command!='quit':
		command=input()
		if command!='quit':
			cmd=string_to_list(command[2:])
			if command[0]=='S':
				x,y=scale(x,y,cmd[0],cmd[1])
				draw_polygon(x,y)
			elif command[0]=='R':
				x,y=rotate(x,y,cmd[0])
				draw_polygon(x,y)
			elif command[0]=='T':
				x,y=translate(x,y,cmd[0],cmd[1])
				draw_polygon(x,y)

		x1='';y1=''
		for i in range(len(x)):
			x1=x1+str(x[i])+" "
		for i in range(len(y)):
			y1=y1+str(y[i])+" "

		print(x1[:-1])
		print(y1[:-1])

