import random


# Design a small guessing game where the computer selects a random number from the range [1, x].
# Have the user generate guesses that get feedback (Too High, Too Low, or Correct!). Continue until the 
# user guess the random number in the range [1, x] correctly

def guess(x):
    # Computer selects a random number from the range [1, x]
    random_number = random.randint(1, x)

    # Initialize int variable guess
    guess = 0

    # Set up a while loop where the user keeps modifying the guess variable until guess = random_number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low.')
        elif guess > random_number:
            print('Sorry, guess again. Too High.')

    print(f"Yay, congrats. You have guessed the number {random_number}")




# Design a small guessing game where you set a range [1, x] and have a number in from that range in your head.
# Have the computer generate guesses that get feedback (Too High, Too Low, or Correct!) and use that feedback to 
# refine its future guesses.

def computer_guess(x):
    # Establish ranges of guesses
    low = 1
    high = x

    # Initializes feedback
    feedback = ''

    # Set up while loop to repeat the guessing routine whilst  
    while feedback != 'c':

        # Account for the edge case when the range is 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Can be guess = high as well, since low == high

        # Initialize input prompt that allows you to register feedback for the computer    
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??: ').lower()
        # Use feedback to refine future guess range   
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number {guess} CORRECTLY!!')

computer_guess(100)