def calculator(a, b, operation):
    operations = {
        "add"      : lambda a, b: a + b,
        "subtract" : lambda a, b: a - b,
        "multiply" : lambda a, b: a * b,
        "divide"   : lambda a, b: a / b
    }
    return operations[operation](a, b)

# Examples
print(calculator(10, 5, "add"))       
print(calculator(10, 5, "subtract"))  
print(calculator(10, 5, "multiply"))  
print(calculator(10, 5, "divide"))    