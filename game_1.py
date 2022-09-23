import random

computer_guessed_number = random.randint(1, 100)
continue_game = True

while(continue_game):
    user_guess = int(input("Uzmini skaitli starp 1 un 100: "))
    #vai user_guess = int(user_guess_string)

    if user_guess == computer_guessed_number:
        print("Wow, tu uzvarēji!")
        continue_game = False
    elif user_guess > computer_guessed_number:
        print("Mazāk!")
    elif user_guess < computer_guessed_number:
        print("Vairāk!")
    else: 
        print("Notika kļūda. Mēģini vēlreiz!")

print("Game over!")
