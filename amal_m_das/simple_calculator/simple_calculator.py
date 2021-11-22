def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = int(input("Enter choice(1/2/3/4): "))

    if choice in [1,2,3,4]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        }
        sel_operation = operations.get(choice)
        result = sel_operation(num1, num2)
        print(result)
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
          
    else:
        print("Invalid Input")
