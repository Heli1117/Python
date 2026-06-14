age = int(input("Enter age: "))
day = input("Enter day type (weekday/weekend): ")

if age < 12:
    price = 100
elif age <= 59:
    price = 200
else:
    price = 150

if day.lower() == "weekend":
    price = price + (price * 0.20)

print("Ticket Price: ₹", price)