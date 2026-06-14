numbers = [12, 45, 3, 67, 21, 9]

largest = numbers[0]
smallest = numbers[0]
total = 0

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
    total += n

average = total / len(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)