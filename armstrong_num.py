num=int(input("Enter a number: "))
def check(num):
 num1=len(str(num))
 sum=0
 temp=num
 while temp>0:
    digit= temp%10
    sum+=digit**num1
    temp//=10
 return num==sum

if check(num):
    print("This is an armstrong number.")
else:
    print("This is not an armstrong number")        


