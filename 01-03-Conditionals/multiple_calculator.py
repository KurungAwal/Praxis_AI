import os

os.system('cls')


add = "add"
substract = "substract"
multiple = "multiple"
divide = "divide"
quit = "quit"



print("Welcome to calculator!")



     
while True:    

            input_calculate = input("What do you want? Add, substract, multiple, divide or quit? ")


            if input_calculate == add:
                input1 = input("Input your first number: ")
                print("---------------------------")
                input2 = input("Input your second number: ")

                try:
                    input1 != int
                    input2 != int

                except:
                    print("Next")
                    print("--------------------------")

                result = print("Result: ", int(input1) + int(input2))
                    
            elif input_calculate == substract:
                input1 = input("Input your first number: ")
                print("---------------------------")
                input2 = input("Input your second number: ")

                try:
                    input1 != int
                    input2 != int

                except:
                    print("Next")
                    print("--------------------------")

                result = print("Result: ", int(input1) - int(input2))
                #yesorno = input("Want to calculate again? yes/no")

            elif input_calculate == multiple:
                input1 = input("Input your first number: ")
                print("---------------------------")
                input2 = input("Input your second number: ")

                try:
                    input1 != int
                    input2 != int

                except:
                    print("Next")
                    print("--------------------------")

                result = print("Result: ", int(input1) * int(input2))
                
            elif input_calculate == divide:
                result = print("Result: ", int(input1) + int(input2))
                ainput1 = input("Input your first number: ")
                print("---------------------------")
                input2 = input("Input your second number: ")

                try:
                    input1 != int
                    input2 != int

                except:
                    print("Next")
                    print("--------------------------")

                result = print("Result: ", int(input1) / int(input2))

            elif input_calculate == quit:
                break

            else:
                print("Invalid input")
            






