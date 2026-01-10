# Day 5: python journey
#for loop in list
#syntax- for variable_name in list_name:
favourites=["strawberry","apple","grapes","banana"]
for fruit in favourites:
    print(fruit)
    print(fruit +" ice-cream")

#excercise 1:
student_score=[123,453,454,342,112,156]
max = 0
for score in student_score:
    if score>max:
        max=score
    
print(max)

sum=0
for score in student_score:
    sum+=score
print(sum)

#range() with for loop 
sum=0
for number in range(1,101):     #this will loop between 1 to 100
    sum+=number
print(sum)

#excercise: 
for number in range(1,101):
    if(number%3==0 and number%5==0):
        strings="FizzBuzz"
        number=strings
        print(number)
    elif(number%3==0):
        strings="Fizz"
        number=strings
        print(number)
    elif(number%5==0):
        strings="Buzz"
        number=strings
        print(number)
    
    else:
        print(number)

#DAY 5 PROJECT :PASSWORD GENERATOR 

import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|","\\",":",";","\"","'","<",">",",",".","?","/"]
print("Welcome to Password Generator")
#Takes user input and convert it into integer type
user_ch_letter=int(input("How many letter you wnat to have in your password?\n"))
user_ch_numbers=int(input("How many numbers you want in your password?\n"))
user_ch_symbols=int(input("How many symbols you want in your password\n"))

#It will pick the random samples from the list and store it as a list in the variables 
letus=random.sample(letters,user_ch_letter)
num=random.sample(numbers,user_ch_numbers)
sym=random.sample(symbols,user_ch_symbols)

#concatenate as a list
password_list=letus+num+sym

#converst list into string
password = "".join(password_list)

print(f"password={str(password)}")