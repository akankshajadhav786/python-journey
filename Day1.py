#DAY1: PYTHON BASICS

#PRINTING STATEMENTS
print("HELLO WORLD!")
print("Heyy this is my first lesson of python")

#New line: \n
print("hello world\nhello world")

#concatenation of strings 
print("HELLO"+"AKANKSHA")
print("HELLO"+" "+"AKANKSHA")
print("HELLO"+" AKANKSHA")

#Input function
input("what is your name?")
print("Hello "+input("what is your name?")+"!")

#Variables and len()
#len function is used to find the length of the string or no. of characters
name="stuart"
print(name)

name=input("enter your name")
print("The name "+(name)+" has "+str(len(name))+" characters") 
print(len(input("what is your name?")))

username=input("what is yout name?")
length=len(username)
print(length)

#problem:swap the liquids in the glass using variables
g1="milk"
g2="juice"
g3=g1
g1=g2
g2=g3
print("glass1= "+g1)
print("glass2= "+g2)
#varaiable naming: seperate the word by _ , no digit at start, no spaces between the words 

#DAY 1: PROJECT - BAND NAME GENERATOR
print("Welcone to the Band name generator")
city_name=input("What's the name of the city you grew up in?\n")#by inserting \n the cursor occurs on the next line 
pet_name=input("what is your pet's name?\n")
print("Your band name could be "+city_name+" "+pet_name)

