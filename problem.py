x=list(map(int, input("(0,0): ").split()))
y=list(map(int, input("(0,1): ").split()))
z=list(map(int, input("(0,2): ").split()))
a=list(map(int, input("(1,0): ").split()))
b=list(map(int, input("(1,1): ").split()))
c=list(map(int, input("(1,2): ").split()))
d=list(map(int, input("(2,0): ").split()))
e=list(map(int, input("(2,1): ").split()))
f=list(map(int, input("(2,2): ").split()))
row1=x+y+z
row2=a+b+c
row3=d+e+f
col1=x+a+d
col2=y+b+e
col3=z+c+f
print(row1,[sum(row1)])
print(row2,[sum(row2)])
print(row3,[sum(row3)])

print(col1,[sum(col1)])
print(col2,[sum(col2)])
print(col3,[sum(col3)])
# print(sum(row1))
#list(map(int(row1).split()) 