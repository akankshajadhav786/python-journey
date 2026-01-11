# DAY3 PYTHON JOURNEY
#if-else conditionals 
print("Welcome to rollercoaster")
height=int(input("Enter the height of candidate in cm"))
if height<180:
    print("eligible to ride")
else:
    print("Not eligible to ride")    

#even odd
number=int(input("Enter the number"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#nested if else
print("Welcome to rollercoaster")
height=int(input("Enter the height of candidate in cm"))
if height<180:
    print("eligible to ride")
    age=int(input("Enter your age"))
    if age<18:
        print("Please pay 50 rupees")
    else:
        print("Please pay 100 rupees")
else:
    print("Not eligible to ride")  

#elif: can be used when multiple conditions are mentioned 
print("Welcome to rollercoaster")
height=int(input("Enter the height of candidate in cm"))
if height<180:
    print("eligible to ride")
    age=int(input("Enter your age"))
    if age<10:
        print("Please pay 20 rupees")
    elif 10<=age<18:
        print("please pay 50 rupees")
    else:
        print("Please pay 100 rupees")
else:
    print("Not eligible to ride")  

#PIZZA ORDERING PROGRAM

bill=0
print("welcome to the pizza ordering counter\nSmall pizza (s) : $15\nMedium pizza (M) : $20\nlarge pizza (L): $25")
pizza_size=input("Which pizza you want to order?\nS, M or L")

if pizza_size == "S":
    bill=15
    pepperoni=input("Do you want pepperoni on yout pizza? Y or N")
    if pepperoni=="Y":
        bill+=2
    cheese=input("Do you want to add cheese? Y or N")
    if cheese=="Y":
        bill+=1
    print(f"total bill = ${bill}")

elif pizza_size == "M":
    bill=20
    pepperoni=input("Do you want pepperoni on yout pizza? Y or N")
    if pepperoni=="Y":
        bill+=3
    cheese=input("Do you want to add cheese? Y or N")
    if cheese=="Y":
        bill+=1
    print(f"TOTAL BILL = ${bill}")

elif pizza_size == "L":
    bill=25
    pepperoni=input("Do you want pepperoni on yout pizza? Y or N")
    if pepperoni=="Y":
        bill+=3
    cheese=input("Do you want to add cheese? Y or N")
    if cheese=="Y":
        bill+=1
    print(f"TOTAL BILL = ${bill}")
else:
    print("Invalid choice!")

# DAY3: PROJECT - TREASURE ISLAND
print("Welcome to Treasure Island\nYour mission is to find the treasure")
direction=input("Do you want to go left or right?\n")
if direction=="left":
    action=input("There is water ahead, do you want to swim or wait?\n")
    if action=="wait":
        door=input("which door you wanna choose?\nred\nblue\nyellow\ntell:")
        if door == "yellow":
            print("YOU WIN!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
     print("Game Over!")
