
n = int(input("Enter the number:"))

a = 0
b = 1
while(n>0):
    print(a,end = " ")
    a,b = b,a+b
    