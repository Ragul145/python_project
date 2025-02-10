import random

words = ("apple","mango","orange","coconut","pineapple")

# dictionary of key:(tuple)
hang_man = {0: ("   ",                
                "   ",
                "   "),

            1: (" o ",
                "   ",
                "   "),

            2: (" o ",
                " | ",
                "   "),

            3: (" o ",
                "/| ",
                "   "),

            4: (" o ",
                "/|\\",
                "   "),

            5: (" o ",
                "/|\\",
                "/  "),

            6: (" o ",
                "/|\\",
                "/ \\")}

def display_man(wrong_guess):
    for line in hang_man[wrong_guess]:
        print(line)

# hint is going to be a list[],a list[] of underscore chars of each letter that we guess right we'll flip one of those underscore to be a letter, if the letter is correct 
def display_hint(hint):
    print(" ".join(hint))

# with in the function we will display the correct ans either when we lose the game or win the game
def display_ans(answer):
    print(" ".join(answer))

# To cotain the main body of the code of our program
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set() # we call empty set , Normally in python we can't create an empty set , we have to use 'set()'function   
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("ENTER A LETTER :").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(f"{guess} is Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")  

        guessed_letters.add(guess)      

           
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guess += 1  

        if "_" not in hint:
            display_man(wrong_guess) 
            display_ans(answer)
            print("YOU WIN !")
            is_running = False

        elif wrong_guess >= len(hang_man) -1:
            display_man(wrong_guess)
            display_ans(answer)
            print("YOU LOSE !")
            is_running = False

if __name__ == "__main__":
    main()
