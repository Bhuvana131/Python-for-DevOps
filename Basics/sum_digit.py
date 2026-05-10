
n = int(input("Enter the number:"))

temp = n

sum = 0

while(n>0):
    rem = n%10
    sum = sum+rem
    n = n//10

print("Sum_of_digits :",sum)