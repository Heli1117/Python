s=input("Enter string:")
if s.isdigit():
    print("Only digits")
elif s.isalpha():
    print("Only letters")
else:
    print("Mix of both")