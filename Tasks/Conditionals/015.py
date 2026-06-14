num = int(input("Enter a number: "))

# Perfect square check
root = int(num ** 0.5)
is_square = (root * root == num)

# Prime check
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Palindrome check
is_palindrome = (str(num) == str(num)[::-1])

if is_square:
    print("Perfect Square")
if is_prime:
    print("Prime Number")
if is_palindrome:
    print("Palindrome Number")
if not (is_square or is_prime or is_palindrome):
    print("None of the properties match")