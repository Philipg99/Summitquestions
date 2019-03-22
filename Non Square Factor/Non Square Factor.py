
n= int(input())
c=0
i=1
while n>1:
	i+=1
	if n%i==0:
		c+=1
		while n%i==0:
			n//=i

print(2**c-1)