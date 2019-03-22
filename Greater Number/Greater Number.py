import math

x = list(map(int,input().split()))
y = list(map(int,input().split()))

sx=1
sy=1

if x[0]<0:
	x[0]*=-1
	if x[1]%2!=0:
		sx=-1

if y[0]<0:
	y[0]*=-1
	if y[1]%2!=0:
		sy=-1

if x[0]==0 and y[0]==0:
	print(0)

elif x[0]==0:
	print(1)

elif y[0]==0:
	print(0)

elif sx*x[1]*math.log(x[0],10) >= sy*y[1]*math.log(y[0],10):
	print(0)
else:
	print(1)