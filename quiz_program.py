
quiz = {
    "question 1": {
        "question": "What is the captial of France?",
        "answer": "Paris"
    },
    "question 2": {
        "question": "What is the captial of Germany?",
        "answer": "Berlin"
    },
    "question 3": {
        "question": "What is the captial of England?",
        "answer": "London"
    },
    "question 4": {
        "question": "What is the captial of Spain?",
        "answer": "Madrid"
    },
    "question 5": {
        "question": "What is the captial of Portugal?",
        "answer": "Lisbon"
    },
    "question 6": {
        "question": "What is the captial of Italy?",
        "answer": "Rome"
    },
    "question 7": {
        "question": "What is the captial of Switzerland?",
        "answer": "Bern"
    },
    "question 8": {
        "question": "What is the captial of Austria?",
        "answer": "Vienna"
    },
}

score = 0
num_of_questions = 8

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print(f"Your score is {score}")
    else:
        print('Incorrect')
        print(f"Your score is {score}")


print(f"Your final score is {score}")
print(f"Your final percentage is {score/num_of_questions * 100} %")