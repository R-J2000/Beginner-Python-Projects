# In a madlib, the user is given a paragraph with specific blanks in it. 
# The user is prompted to fill in the blanks, which are used to fill in the blanks.


# Prompt responses asked to the user, which once provide, will fill in the blanks for the madlib
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")


madlib = f"Computer programmming is so {adj}! It makes me so excited all time \
because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

# Lessons 
# 1. Always save
# 2. The format for the input operation is [name = input("Prompt: ")]
# 3. [f"...{variable}..."] is the most concise way to string concatenate in Python. 