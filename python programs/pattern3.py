def pattern():
	i=1
	m=0
	k=0
	for i in range(1,6):
		m=m+i
		k=m
		for j in range(1,i+1):
			print(k,end='  ')
			k=k-1
		print("\n")
		
pattern()