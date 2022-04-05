num1=float(input("enter 1st number: "))
operator=input("(+-*/): ")
num2=float(input("enter second number: "))
sum=float(num1+num2)
sub=float(num1-num2)
mul=float(num1*num2)
div=float(num1/num2)
def sum():
    sum=float(num1+num2)
    print(sum)

def sub():
    sub=float(num1-num2)
    print(sub)
def mul():
    mul=float(num1*num2)
    print(mul)
def div():
    div=float(num1/num2)
    print(div)


if '+' in operator:
    sum()
if '-' in operator:
    sub()
if '*' in operator:
    mul()
if '/' in operator:
    div()        

