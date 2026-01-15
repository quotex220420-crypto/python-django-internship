# Smart Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
elif username == "admin":
    print("Wrong Password")
else:
    print("User Not Found")
