num=int(input("enter the number of series: "))
def sum_of_cubes(n):
 sum=0
 for n in range(num+1):
    sum=sum+ n**3
 return sum  
cube=sum_of_cubes(num)   
print(cube)