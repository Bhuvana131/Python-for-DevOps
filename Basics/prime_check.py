
n = int(input("Enter the number:"))
flag = False

for i in range (2,n):
    if n%i == 0:
        flag = True
        print(n,"is not a Prime")
        break

if not flag:
    print(n," is a Prime ")