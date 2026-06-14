correct_user = "admin"
correct_pass = "1234"
attempts = 0

while attempts < 3:
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if user == correct_user and pwd == correct_pass:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Invalid Credentials")
        if attempts == 3:
            print("Account Locked")