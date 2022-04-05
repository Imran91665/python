class shopping:
    cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)
customer1=shopping()
customer1.add_to_cart(input("Select your item: "))
       
customer2=shopping()
customer2.add_to_cart(input("Select your item: "))
        
customer3=shopping()
customer3.add_to_cart(input("Select your item: "))
        
customer4=shopping()
customer4.add_to_cart(input("Select your item: "))
        
customer5=shopping()
customer5.add_to_cart(input("Select your item: "))
print("Your items are: ",customer1.cart)
#print(customer2.cart)
#print(customer3.cart)
#print(customer4.cart) 
#print(customer5.cart)        
#customer1=shopping()
#customer1.add_to_cart(input("Select your item: "))
#print(customer1.cart)        