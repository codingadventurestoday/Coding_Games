
import random as ran 
import time 

# have the computer guess a number 
def letsPlay(name):
    game_on = True
    count = 0  
    min = 1
    max = 25 
    while game_on == True: 
        computer_guess = ran.randint(min, max) 
        check = input(f'Is your number {computer_guess}? ')

        # if the number is guessed we end the while loop 
        if check.lower() == 'yes':
            count +=1
            print(f'Woah it took me {count} tries, but I got your number {name}!')
            game_on = False 

        #if the number isn't guess we change the max or min based off the user 
        elif check.lower() == 'no':
            count += 1 
            adjustment = input(f'Is your secret number higher or lower than {computer_guess}? ')
            if adjustment.lower() == 'higher':
                min = computer_guess + 1 

            elif adjustment.lower() == 'lower':
                max = computer_guess - 1 

            else:
                 print('I\'m not sure what you meant there. Let me guess another number then')
                

        else:
            print('Hmmm, I am not sure what you mean.... tell me if yes or no please!')


# tell user to pick a number 
start = True 
while start == True:
    play = input('How about we play a game? ')

    if play.lower() == 'yes':
        name = input('Great! What\'s your name ')
        print(f'Alright {name} pick a number between 1 and 25. I bet you I can guess it in 8 ties!')
        time.sleep(1)
        print('Do you have your number? I am ready!')
        time.sleep(1.5)
        letsPlay(name)

        continue 

    elif play.lower() == 'no': 
        print('That\'s a bummer. Let\'s play some other time then')
        start = False 
    
    else: 
        print('I\'m not sure what you mean by that. Let\'s try again. Tell me yes if you would like to play. Otherwise tell me no ')
