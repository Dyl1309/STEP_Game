import random
rock = 1
paper = 2
scissors = 3
gun = 12345
while True:
    symbol = random.randint(1, 3)
    user = int(input("INPUT YOUR SYMBOL 1:ROCK 2:PAPER 3:SCISSORS:"))
    print(symbol)
    if user == symbol:
        print("TIE")
    elif(user == 1 and symbol == 3) or \
        (user == 2 and symbol == 1) or \
        (user == 3 and symbol == 2):
            print("WIN")
    elif(user == 1 and symbol == 2) or \
        (user == 2 and symbol == 3) or \
        (user == 3 and symbol == 1):
            print("LOSS")
    if user == 12345:
        print("WIN")       
        break