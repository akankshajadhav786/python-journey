# DAY2 PYTHON JOURNEY

#Subscrpting: pulling out a particular charactor from a string 
print("Akanksha"[0]) #can count backwards as -1

# Data types: String, Integer, Float and Boolean

# String: Any thing written inside the " " is considered as a String 
print("123456")

# Integer : whole number
print(345)
print(67+90)
print(-90)
print(90+(-56))

# Float: Floating point number
print(3.14)

#Boolean: determines True or False
print(True)
print(False)

# Type checking: type keyword determines the data type
print(type(1234))
print(type("loka"))
print(type(True))
print(type(12.34))

#Type casting/ type conversion: str(),bool(), int(), float()
print(int("123"))#this will convert string into an integer
print("Number of letters in yout name: "+str(len(input("Enter your name\n"))))

#Mathematical operations
print("My age: "+"20")
print(4 + 4) # Addition
print(6 - 9) # Sub
print(9 * 9) # multiplication
print(2 / 4) # divison: always returns a floating point answer
print(2 // 4) # // works as divison but the answer is simply an integer by removing the decimal points.
print(2 ** 2) #Exponent
# PRIORITY ORDER : PEMDASLR
# # ()
# # **
# # * OR / (equal priority so execute from Left to right)
# # + OR - (equal priority so execute from Left to right)
print(9/9+6-4+5*2)

#round()
bmi=90/1.65**2
print(round(bmi))

#assignment operator +=, -=, *=, /=
score=0
score+=1
print(score)

#F strings
height=153
weight=52
age=20
print(f"Your age is {age}\nYour height is {height}\nYour weight is {weight}")

name=input("Enter your name")
age=input("Enter your age")
print(f"Name: {name}\nAge: {age}")

#Project : Tip calculator 
print("Welcome to the tip calculator!")
Bill_amount=float(input("what was the total bill? $"))
total_tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
people=int(input("how many people to split the bill"))
tip_percentage=total_tip/100*Bill_amount+Bill_amount
bill_per_person=round(tip_percentage/people,2)
print(f"Each person should pay: {bill_per_person}")



