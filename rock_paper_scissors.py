import random


# Set up a rock-paper-scissor game with the computer
def play():
    # Get the user and computer to make their choices
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors?: ")
    computer = random.choice(['r', 'p', 's'])

    # Compare picks
    if user == computer:
        return 'Its a Tie!'

    if is_win(user, computer):
        return'You Won!'

    return 'You Lost!'

# Function used to assess who satisfies the win condition 
def is_win(player, opp):

    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') or (player == 'p' and opp == 'r'):
        return True

# Prints final result    
print(play())

# Lessons
# 1. Learned about the function random.choice([...])
# 2. Learned the importance of PRINTING your results at different stages