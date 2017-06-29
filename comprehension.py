# This is a simple guessing game,in which the user has 5 possibilities to find out what number was created randomly.

import random  # Import the random module

guessesTaken = 0  # Make a variable named 'guessesTaken', assign to it the value 0

print('Hello! What is your name?')  # Print out the string in the argument list to the console
myName = input()  # Ask for user input and assign it to a variable named 'myName'

number = random.randint(1, 20)  # Generate a random number between 1 and 20 and assign its value to variable 'number'

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Print out the concatenated string with the value of 'myName'

while guessesTaken < 6:  # Iterate until the variable 'guessesTaken' is smaller than 6
    print('Take a guess.')  # Print out this string
    guess = input()  # Assign the user input to a variable named 'guess'
    guess = int(guess)  # Convert the 'guess' variable's type to integer

    guessesTaken += 1  # Increment the value of 'guessesTaken' by 1

    if guess < number:  # Check whether the value of 'guess' is smaller than the value of 'number' in a condition
        print('Your guess is too low.')  # If the condition is evaluated True, print out this string to the console

    if guess > number:  # Check whether the value of 'guess' is bigger than the value of 'number'
        print('Your guess is too high.')  # If the condition is True print this string to the console

    if guess == number:  # Check whether the values of 'guess' and 'number' variables are equal
        break  # If the condition True, exit from the while loop with the break statement

if guess == number:  # Checks whether the value of 'guess' and 'number' are equal
    guessesTaken = str(guessesTaken) # If the condition is evaluated True, convert the variable 'guessesTaken' type to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Print to the console this concatenated string with the value of 'myname' and 'guessesTaken'

if guess != number:  # Checks whether the value of 'guess' is not equal with the value of 'number'
    number = str(number)  # If the condition is True, convert the type of the 'number' variable to string
    print('Nope. The number I was thinking of was ' + number) # Print out to console this concatenated strig which contains the value of the variable 'number'
