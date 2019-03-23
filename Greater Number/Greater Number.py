import math

x = list(map(int,input().split()))
y = list(map(int,input().split()))


sign_x = 1
sign_y = 1

#if the base is negative
if x[0]<0:
	x[0]=abs(x[0])
	sign_x = -1 if x[1]%2!=0 else 1

if y[0]<0:
	y[0]=abs(y[0])
	sign_y = -1 if y[1]%2!=0 else 1

#------------------------

# if either one of the bases are zero
if x[0] == 0 or y[0] == 0:
	if sign_x*x[0]*x[1] >= sign_y*y[0]*y[0]:
		print(0)
	else:
		print(1)

#------------------------------------

else:
	# if rasied to zero
	if x[1]!=0:
		valx=sign_x*x[1]*math.log(x[0])
	else:
		valx=1
	
	if y[1]!=0:
		valy=sign_y*y[1]*math.log(y[0])
	else:
		valy=1
	#--------------------
	
	if valx >= valy:
		print(0)
	else:
		print(1)
