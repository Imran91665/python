len=int(input("how many number: "))
total=0
for i in range(0,len):
    elements=float(input("enter your element: "))
    total+=elements
average=total/len
print(average)    
