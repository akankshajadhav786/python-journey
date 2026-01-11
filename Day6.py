#functions in python 
#defining the function- def funtion_name():
#calling the function-function_name()
import random
def game():
    print("welcome to guessing game")
    a=int(input("Select the number between 1 to 10\n"))
    b=random.randint(1,10)
    if(a==b):
        print("Yayy! YOU WON")
    else:
        print("Better luck next time")

game()
