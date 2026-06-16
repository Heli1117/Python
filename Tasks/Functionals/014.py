def total(*numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result

# Example
print(total(1, 2, 3))        
print(total(10, 20, 30, 40)) 

