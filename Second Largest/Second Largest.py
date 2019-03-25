
n = int(input())
num = list(map(int,input().split()))

sl='NULL'
fl=num[0]

for i in num:
	if i > fl:
		sl=fl
		fl=i

	if sl=='NULL' and fl!=i:
			sl = i
	if sl!='NULL':
		if i>sl and fl!=i:
			sl=i

print(sl)