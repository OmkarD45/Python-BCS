class CreditCard:
	def get(self):
		print("enter information")
		self.cno=int(input("enter card number"))
		self.cust=input("enter customer name")
		self.bal=int(input("enter the balance"))
	def view(self):
		print("CARD NO: \t",self.cno)
		print("CARD HOLDER NAME: \t", self.cust)
		print("BANK BALANCE: \t", self.bal)
	def used(self):
		self.amt=int(input("enter the amount foor withdraw:\t"))
		if(self.amt>self.bal):
			print("insufficient balance to withdraw")
		else:
			self.bal=self.bal-self.amt
	def pay(self):
		self.amt=int(input("enter amount for deposit:\t"))
		self.bal=self.bal+self.amt
cc=CreditCard()
cc.get()
cc.view()
cc.used()
cc.view()
cc.pay()
cc.view()
