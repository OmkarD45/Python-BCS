def pattern():
	i=1
	for i in range (1,5):
		j=4
		k=1
		while(j>=i):
			print(k,end='  ')
			k=k+1
			j=j-1
		print("\n")
pattern()