

n=int(input())


i=1
p=n
while n>1:
    i+=1
    if n%i==0:
        p*=(1-1/i)
        while n%i==0:
            n/=i


print(round(p))
