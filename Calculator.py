def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible/undefined."
    return x / y

print("Operations that can be performed.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = input("Select the index of operation to be performed:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the Second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Input is invalid")
