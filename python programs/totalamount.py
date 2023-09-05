print("enter the quantity")
qty=int(input())
if(qty>1000):
	amt=qty*100
	dis=amt/100*10
	tna=amt-dis
	print("the net amunt of products is Rs",tna)
else:
	tna=qty*100
	print("the net amount of products is Rs",tna)