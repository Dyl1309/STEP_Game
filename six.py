name = str(input("WHAT IS YOUR NAME?"))
print("Hello "+name)
import random
number = random.randint(1, 100)
counter =0
while True:
    guess = int(input("WHAT IS YOUR GUESS - 1-100?")) 
    if guess < number:
        print("HIGHER")
        counter+=1
    elif guess > number:
        print("LOWER")
        counter+=1
    elif guess == number:
        print("CONGRATS "+name + str(counter )+" GUESSES")
        break
    

