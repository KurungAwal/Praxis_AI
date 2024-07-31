import getpass


print("Hello User!")
print("----------------------------------------------------------------")


user = input("Input your new username: ") #Pada website, variabel akan diambil dari database website itu sendiri
password = getpass.getpass("Input you new password: ")

print("----------------------------------------------------------------")

user_in = input("Input the username: ")
pw_in = getpass.getpass("Input your password: ")

if user_in == user and password == pw_in:
    print("Welcome to this app " + user)
else:
    print("You are a stranger!")
    
    




