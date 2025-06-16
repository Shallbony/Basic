#write a program to calculaate factorial of given number using for loop

#5!=1X2X3X4X5

n = int(input("Enter the number: "))
product = 1
for i in range(1, n + 1):
    product = product * i


print(f"The factorial of {n} is {product}")
