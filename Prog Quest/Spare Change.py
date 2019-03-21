denominations=int(input())
values=list(map(int,input().split()))
amount=int(input())

ways=[]
for i in range(amount):
    ways+=[0]
    
for i in range(amount):
    for value in values:
        p=i- value
        if p==-1:
            ways[i]+=1
        if p>=0:
            ways[i]+=ways[p]

print(ways[amount-1])