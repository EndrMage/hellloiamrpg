import random
guess=input("I thought of a random number between 1 and 100. Try to guess it! ")
number=random.randint(0,100)
while int(guess)!=int(number):
    guess = input("Guess again! ")
    if(int(guess)==int(number)):
        print("Yes! Well done!")
        break
    if(int(guess)<int(number)):
        print("No. Bigger!")
    if(int(guess)>int(number)):
        print("No. Smaller!")


