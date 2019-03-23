import math

x = list(map(int,input().split()))
y = list(map(int,input().split()))

log_value_x = x[1]
log_value_y = y[1]

sign_x = 1
sign_y = 1

if x[0]<0:
	x[0]=abs(x[0])
	sign_x = -1 if x[1]%2!=0 else 1

if y[0]<0:
	y[0]=abs(y[0])
	sign_y = -1 if y[1]%2!=0 else 1

if 

