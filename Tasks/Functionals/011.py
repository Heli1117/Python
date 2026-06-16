def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    result = []
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)
    return result

# Example
print(primes_in_range(1, 20))



