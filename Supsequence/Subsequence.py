
l = int(input())

seq = list(map(int,input().split()))

lseq=[]

for i in range(l):
	lseq+=[1]

for i in range(1,l):
	ml=0
	cl=0
	for j in range(i):
		if seq[j]<=seq[i]:
			cl=lseq[j]
			if cl>ml:
				ml=cl
	lseq[i]=ml+1

print(max(lseq))
