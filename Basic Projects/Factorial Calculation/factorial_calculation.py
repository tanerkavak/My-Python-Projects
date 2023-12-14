print("-"*5)

number = int(input("Enter a number: "))
factorial = 1
 
print("-"*5)

if number >= 0:
    for i in range(1, number+1):
        factorial *= i
    print(f"The factorial of the number you entered: {number}! = {factorial}")
else:
    print("Negative numbers have no factorial!")

input()