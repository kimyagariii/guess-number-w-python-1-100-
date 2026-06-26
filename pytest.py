import random
number=random.randint(1,100)
print("hi! wellcome to the guessing number game, you have to guess a number between 1 and 100.remember!you only have 5 chance to guess it.HAVE FUN;)")
chance=5
counter=0
while counter<chance:
    counter+=1
    guess=int(input("guess a number dude:"))
    if guess==number:
        print("yeah,you did it well!")
        break
    elif counter>=chance and guess!=number:
        print(f'oops!the number was {number},maybe next time buddy.')
    elif guess>number:
        print('guess is higher than number')
    elif guess<number:
        print('guess is lower than number')