import random 
import time


number= random.randint(1,100)
def intro():
    print('Hi there!')
    global name
    name=input('What is your name?')
    print(name,'we are going to play a game!')
    print('I am thinking of a number 1-100 try and guess it!')
    if number%2 == 0:
        x='even'
    else:
        x='odd'
    print('\n The number is an {} number!'.format(x))
    time.sleep(0.5)
    print('Try to guess it haha!')
def pick():
    guesstaken = 0
    while guesstaken < 6:
        time.sleep(0.5)
        userguess = int(input('GUESS NOW!'))
        try:
            if userguess <=100 and userguess >=1:
                guesstaken = guesstaken+1
                if guesstaken < 6:
                    if userguess < number:
                        print('The number is too low!')
                    if userguess > number:
                        print('The number is too high!')
                    if userguess != number:
                        time.sleep(1)
                        print('Try Again!')
                    if userguess == number:
                        break
            if userguess > 100 or userguess < 1:
                        print('Retry the number within the given range please!')   
        except:
            print('You have not entered a number sadly so please retry!')
    if userguess == number:
        guesstaken=str(guesstaken)
        print('You have got the number correct good job!{} in {} guesses.'.format(name,guesstaken))
    if userguess != number:
        print('The number I was thinking of is:',number)
playagain = 'yes'
while playagain == 'yes' or playagain == 'y' or playagain == 'Y' or playagain == 'Yes':
    intro()
    pick()
    playagain = input('Do you want to play again?')
