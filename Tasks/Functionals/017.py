def double(x):
    return x * 2

def apply_twice(func, value):
    first = func(value)
    second = func(first)
    return second

# Example
print(apply_twice(double, 3))  