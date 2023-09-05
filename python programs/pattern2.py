def pattern():
	i=1
	j=1
	for i in range (1,5):
		for j in range(i,0,-1):
			print(j,end='  ')
		print("\n")
pattern()