import random
from time import process_time_ns

computer_guessed_number = random.randint(1, 100)
continue_game = True

while(continue_game):
    user_guess = int(input("Uzmini skatli starp 1 un 100: "))

    if user_guess == computer_guessed_number:
        print('Tu uzvarēji!')
        continue_game = False
    elif user_guess < computer_guessed_number:
        print('Vairāk')
    elif user_guess > computer_guessed_number:
        print('Mazāk')
    else:
        print('Notika kļūda')

print('Game over!')
