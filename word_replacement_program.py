def replace_word():

    str = "Greetings, Ladies and Gentlemen. My name is Rehaan and I shall be you host today."
    print(str)
    word_to_replace = input("What word would you like to replace: ")
    word_replacement= input ("What is your replacement: ")

    print(str.replace(word_to_replace, word_replacement))

replace_word()