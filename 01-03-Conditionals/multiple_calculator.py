import os
import getpass

os.system('cls')


# add = "add"
# substract = "substract"
# multiple = "multiple"
# divide = "divide"



math = ("add", "substract", "multiple", "divide", "quit")

w = math[0]
x = math[1]
y = math[2]
z = math[3]
a = math[4]


input1 = input2 = 0
buffer = ""
buffer2 = ""



def calculator():

           
           while True:    


                print("----------------------------------------------------------------")

                input_calculate = input("What do you want? Add, substract, multiple, divide or quit? ") 
                input_calculate = input_calculate.lower()

                if input_calculate == a:
                    exit()

                while True:
                        buffer = input("Input your first number: ")
                        try:
                            input1 = int(buffer)
                            break
                        except:
                            print("Invalid input")

                while True:
                        buffer2 = input("Input your second number: ")
                        try:
                            input2 = int(buffer2)
                            break
                        except:
                            print("Invalid input")

                print("----------------------------------------------------------------")

                if input_calculate == w:
                    result = print("Result: ", int(input1) + int(input2))
                        
                elif input_calculate == x:
                    result = print("Result: ", int(input1) - int(input2))
                    #yesorno = input("Want to calculate again? yes/no")

                elif input_calculate == y:
                    result = print("Result: ", int(input1) * int(input2))
                    
                elif input_calculate == z:
                    result = print("Result: ", int(input1) / int(input2))

                else:
                    print("Invalid input") 

print("Welcome new user!")


user = input("Input your new username: ") #Pada website, variabel akan diambil dari database website itu sendiri
password = getpass.getpass("Input you new password: ")
        

print("----------------------------------------------------------------")


while True:
      
    print("Please Login")
    user_in = input("Input the username: ")
    pw_in = getpass.getpass("Input your password: ")

    if user_in == user and password == pw_in:
            
            print("----------------------------------------------------------------")
            print("Welcome to this calculator " + user)
            calculator()


    else:
            print("----------------------------------------------------------------")
            print("Access denied")
            print("----------------------------------------------------------------")