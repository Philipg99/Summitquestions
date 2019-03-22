
no = int(input())
val = list(map(int,input().split()))

def fact(n):
	f=1
	for i in range(1,n+1):
		f*=i
	return f

total = sum(val)*fact(no-1)*int('1'*no)

print(total)
