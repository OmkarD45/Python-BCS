def product(cid,cname):
	pname=""
	rate=""
	qty=""
	print("enter the product details\n")
	pname=input("enter the product name\t")
	qty=int(input("enter the quantity\t"))
	rate=int(input("enter the rate\n"))
	cal(cid,cname,pname,qty,rate)
def cal(cid,cname,pname,qty,rate):
	amt=0
	sum=0
	amt=qty*rate
	sum=sum+amt
	print("customer id=  ",cid)
	print("customer name=  ",cid)
	print("product=",pname,"\tqty=",qty,"\trate",rate,"\t")
	print("total bill amount :",sum)
id=int(input("enter the customer id"))
name=input("enter the customer name")
product(id,name)