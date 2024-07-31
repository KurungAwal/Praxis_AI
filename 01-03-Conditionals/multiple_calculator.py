import os

os.system('cls')

add = "add"
substract = "substract"
multiple = "multiple"
divide = "divide"

print("Welcome to calculator!")

while True:

    input_calculate = input("What do you want? Add, substract, multiple or divide? ")

    if input_calculate == add:
        input1 = input("Input your first number: ")
        print("---------------------------")
        input2 = input("Input your second number: ")
        print("---------------------------")
        result = print("Result: ", int(input1) + int(input2))
        print("---------------------------")
            
    elif input_calculate == substract:
        input1 = input("Input your first number: ")
        print("---------------------------")
        input2 = input("Input your second number: ")
        print("---------------------------")
        result = print("Result: ", int(input1) + int(input2))
        #yesorno = input("Want to calculate again? yes/no")

    elif input_calculate == multiple:
        input1 = input("Input your first number: ")
        print("---------------------------")
        input2 = input("Input your second number: ")
        result = print("Result: ", int(input1) + int(input2))
        print("---------------------------")
        
    elif input_calculate == divide:
        input1 = input("Input your first number: ")
        print("---------------------------")
        result = print("Result: ", int(input1) + int(input2))
        print("---------------------------")

    else:
        print("Invalid input")
        






