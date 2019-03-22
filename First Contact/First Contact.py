trans={'nul':0,'Eyns':1,'Tsvey':2,'Dray':3,'Fier':4,'Finef':5,'Zeks':6,'Zibn':7,
		'Achet':8,'Nayn':9,'Tsen':10,'Elf':11,'Tsvelf':12,'Draytsn':13,'Fertsn':14,
		'Fuftsn':15,'Zekhtsn':16}

n1 = input().split()
n2 = input().split()

x=0
y=0

for i in n1:
	x=x*16+trans[i]

for i in n2:
	y=y*16+trans[i]

print(x*y)