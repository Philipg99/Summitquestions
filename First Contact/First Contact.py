trans={'nul':0,'eyns':1,'tsvey':2,'dray':3,'fier':4,'finef':5,'zeks':6,'zibn':7,
		'achet':8,'nayn':9,'tsen':10,'elf':11,'tsvelf':12,'draytsn':13,'fertsn':14,
		'fuftsn':15}

n1 = input().split()
n2 = input().split()

x=0
y=0

for i in n1:
	x=x*16+trans[i]

for i in n2:
	y=y*16+trans[i]

print(x*y)
