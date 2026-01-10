# Randomisation: creates random number and list 
import random 
number= random.randint(1,10)
print(number)

#list: variable = [item1, item2]
state =["maharashtra", "punjab","haryana","delhi"]
print(state[0])
state[1]="rajasthan"#replacing the item in the list 
print(state)
state.append("up")#to add the item in the end of the list
print(state)
state.extend(["bihar","tamil nadu"])#to add this list to actually existing list 
print(state)
state.insert(2,"karnataka")#inserting at a specific position
print(state)
state.remove("up")#removes item from the list
print(state)
state.pop(0)#removes the item at that specified position, if not specified removes the last item
print(state)

#excercise: random+list
import random
friends=["alice","bob","charlie","david","emanuel"]
print(random.choice(friends))

#nested list 
fruits=["cherry","apples","banana","grapes"]
nuts=["almond","pista","cashew"]
no_of_fruits=len(fruits)
print(fruits[no_of_fruits-1])#to avoid indexerror: list out of range

breakfast_mix=[fruits,nuts]#inserting 2 lists in one
print(breakfast_mix)
print(breakfast_mix[1][2])
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])#fruits = 0 and vegetable =1 in dirty_dozen so [1][1 meaning the first [1] represents the list of vegetables and then [1] is the item at position 1 that is kale


#DAY4:PROJECT: ROCK PAPER SCISSOR GAME
import random
scissor='''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#user side
user_choice=int(input("what do you wnat to choose:\nType 0 for rock\nType 1 for paper\nType 2 for scissor\n"))
if(user_choice==0):
    print(rock)
elif(user_choice==1):
    print(paper)
elif(user_choice==2):
    print(scissor)
else:
    print("invalid")
    exit()
#computer side
print("Computer chose:\n")
comchoice=["rock","paper","scissor"]
computer=random.choice(comchoice)
if(computer=="rock"):
    print(rock)
if(computer=="paper"):
    print(paper)
if(computer=="scissor"):
    print(scissor)

#result calculation
if(user_choice==0 and computer=="rock"):
    print("Tie")
elif(user_choice==0 and computer=="paper"):
    print("Computer won")
elif(user_choice==0 and computer=="scissor"):
    print("You won")
elif(user_choice==1 and computer=="paper"):
    print("Tie")
elif(user_choice==1 and computer=="rock"):
    print("You won")
elif(user_choice==1 and computer=="scissor"):
    print("computer won")
elif(user_choice==2 and computer=="scissor"):
    print("Tie")
elif(user_choice==2 and computer=="paper"):
    print("You won")
elif(user_choice==2 and computer=="rock"):
    print("computer won")




