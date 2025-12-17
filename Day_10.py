# calculator program application
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = int(input("Enter the first number: "))
for val in operations:
    print(val)
operator = input("Enter among the above operations: ")
n2 = int(input("Enter the second number: "))

print(f"{n1} {operator} {n2} = {operations[operator](n1, n2)}")