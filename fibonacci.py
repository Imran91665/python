num=int(input("enter the numbers: "))
fibo=[0,1]
i=2
while i<=num:
    next_fibo=fibo[i-1]+fibo[i-2]
    fibo.append(next_fibo)
    i+=1
    
    print(next_fibo) 