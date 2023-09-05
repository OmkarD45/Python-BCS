yos=int(input("enter year of service"))
sal=int(input("enter the salary"))
if yos>5:
	bonus=sal*0.05
	tsal=sal+bonus
	print("the bonus is RS",bonus," and the total salary is RS",tsal)
else:
	print("year os service is less than 5 years salary is RS",sal)