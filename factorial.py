#factorial=n*(n-1)*(n-2)....*1

num1=int(input("Enter the number: "))
def factorial(num1):
        fact = 1
        while num1>1:
             
            fact *= num1
            num1 -= 1
            print(fact)
        else:
            print("Sorry, The num can not be factorial")    
    
factorial(num1)
   
