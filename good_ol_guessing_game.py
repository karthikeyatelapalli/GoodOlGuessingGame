# Description
# Good ol Guessing Game
''' This program asks the user to predict a number within the range of 1 and 100 (inclusive) in as
little as 10 tries. The application counts the number of guesses made by the user while randomly
selecting a number from the specified range. The software determines whether the user's guess falls
within the acceptable range and offers recommendations to assist in making the right guess. The
program ends the loop and congratulates the user, displaying the number of tries it took them to
guess the number, if they correctly estimate the number within the allotted number of attempts.
The program shows the user the right answer if the user makes an incorrect guess
after the allotted number of tries.'''


import random

# This generates a random number between 1 and 100 
random_number = random.randint(1, 100)


i = 1

# Takes input from user which is a number between 1 and 100 (inclusive)
user_number = int(input("Enter a number between 1 and 100 (inclusive): "))

while i < 10:

    # If the person's guess is equal to the random number, prints this message.
    if user_number == random_number:
        print("You guessed it right!! You got it in {} guesses!".format(i))
        break

    # If the person's guess is outside the range of 1 to 100 (inclusive). It tell the person to enter the number again. 
    elif user_number < 1 or user_number > 100:
        user_number = int(input("Really? Enter another guess between 1 to 100: "))

    # If the person's guess is lower than the random number, it tells the person that the number is low and to enter the number again. 
    elif user_number < random_number:
        user_number = int(input("Too low. Enter another guess: "))

    # If the person's guess is higher than the random number, it tells the person that the number is high and to enter the number again.
    else:
        user_number = int(input("Too high. Enter another guess: "))

     
    i += 1

# If the person didn't guess the number in 10 attempt it prints the number at last and exits the loop.
else:
    print("Sorry, the number was {} ".format(random_number))
