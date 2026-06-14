for num in range(1, 10000):
    temp = num
    digits = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10
    if total == num:
        print(num)