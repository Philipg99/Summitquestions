
size = int(input())

seq = list(map(int,input().split()))

lseq=[]

lseq+=[[seq[0]]]


for i in range(1,len(seq)):

	if seq[i]<lseq[0][0]:
		lseq[0][0]=seq[i]

	for j in range(len(lseq)):

		if seq[i]>lseq[j][-1]:
			temp=lseq[j]+[seq[i]]
			if len(temp)>len(lseq):
				lseq+=[temp]
			else:
				if temp[-1]<lseq[j+1][-1]:
					lseq[j+1]=temp


print(len(lseq[-1]))
