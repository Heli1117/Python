a=int(input("Enter first: "))
b=int(input("Enter second: "))
c=int(input("Enter third: "))
if a>=b and a>=c:
    print(a,"is largest")
elif b>=a and b>=c:
    print(b,"is largest")
else:
    print(c,"is largest")