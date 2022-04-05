num=int(input("enter a number: "))

def is_prime(num):
 for i in range(2,num):
  if num%i ==0:
    return False
 return True
def all_prime(num):   
 
 prime=[]
 for n in range(2,num+1):
  
    if is_prime(n) is True:  
     prime.append(n)
     
 return prime
  

primes=all_prime(num)
print(primes)