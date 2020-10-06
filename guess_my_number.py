# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import random
MIN=0
MAX=1000
if __name__ == '__main__':
    number_to_guess=random.randint(MIN,MAX)
    print('hey, Try to guess a number between %d and %d'%(MIN,MAX))

    while True:
        user_imput=input('your guess?')
        try:
            user_attempt=int(user_imput)
            if user_attempt==number_to_guess:
                print('fantastic, you could find the number i had in mind')
                break
            elif user_attempt < number_to_guess:
                print('too low')
            else:
                print('too high')
        except ValueError:
            print('You joker... that was not an integer')
            
