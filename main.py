# Trivia Time Game
import random
import os
from colorama import Fore
import csv
import time
from magicsound import magicsound

# Used in Main Game Loop to test if player is still playing
still_playing = 1
# Variable to store the players choice in the Main Menu
opt = 0
# Tracks the high score for each session
high_score = 0
# Initialize the questions list
questions = []


# This function will load the questions for the provided genre
def load_questions(genre):
    global questions
    with open(genre, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        questions = list(reader)


# This function will select a random question and display the question with the available answers in the correct format.
def display_question(ran_num, genre):
    # Pick a random number and pull the question and answers form the questions list.
    while ran_num in questions_asked:
        ran_num = random.randint(0, len(questions)-1)

    questions_asked.append(ran_num)

    question = questions[ran_num][0]
    answer1 = questions[ran_num][1]
    answer2 = questions[ran_num][2]
    answer3 = questions[ran_num][3]
    corr_ans = questions[ran_num][4]
    # Allow access to the global variable 'score'
    global score
    # Variable to hold the players guess.
    guess = 0

    # Display question and answers; accept the players guess and update the score
    while guess == 0:
        os.system('cls')
        print(Fore.WHITE)
        print("Your score is: " + Fore.GREEN + f"{score}")
        print(Fore.WHITE + "")
        print("The Category is: " + Fore.CYAN + f"{genre}")
        print(Fore.WHITE + "")
        print("Question number " + Fore.YELLOW + f"{rnd}" + Fore.WHITE + " of " + Fore.YELLOW + f"{rounds}")
        print(Fore.WHITE + "")
        print(f"{question}:")
        print(f"   1. {answer1}")
        print(f"   2. {answer2}")
        print(f"   3. {answer3}")
        print("")
        try:
            guess = int(input("Pick your answer and press ENTER: " + Fore.BLUE))
            print(Fore.WHITE + "")
        except ValueError:
            print(Fore.RED + "That is not a valid selection.")
            input(Fore.WHITE + "Press ENTER to continue")
            guess = 0
            continue

        if guess < 1 or guess > 3:
            print(Fore.RED + "That is not a valid selection.")
            input(Fore.WHITE + "Press ENTER to continue")
            guess = 0
            continue
        elif guess == corr_ans:
            magicsound("correct_answer.wav", False)
            flashy_words("You got it right!")
            score = score + 1
        else:
            magicsound("buzzer.wav", False)
            print(Fore.RED + "You guessed wrong!")
            time.sleep(0.7)


# This function takes a text string and makes it change colors letter by letter
def flashy_words(text):
    # Create a list to hold the text
    lets_to_flash = []
    # Separate the text into individual letters
    lets_to_flash[:0] = text
    # Create a list to hold the color formatting - RED, GREEN, BLUE, YELLOW, and CYAN
    color_format = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN]
    # Get the number of letters in the text
    num_of_letters = len(lets_to_flash)
    # ANSI sequence to clear a line
    clear_line = '\x1b[2K'
    # ANSI sequence to move the cursor up one line
    up_line = '\033[1A'

    # Outer loop iterates once per letter and changes the color order
    for a in range(1, num_of_letters):
        c = 0
        # Inner loop iterates once per letter and applies the color to each letter
        for b in range(0, num_of_letters):
            if b == num_of_letters-1:
                print(color_format[c] + lets_to_flash[b])
            else:
                print(color_format[c] + lets_to_flash[b], end='')
            c += 1
            if c == 5:
                c = 0
        print(up_line + "\r", end=clear_line)
        time.sleep(0.15)
        swap = color_format[4]
        color_format.pop(4)
        color_format.insert(0, swap)


os.system('cls')
print("")
print("")

# displays the splash screen
flashy_words("Welcome to Trivia Time!")

# Main game loop
while still_playing:
    # Display the main menu
    os.system('cls')
    print(Fore.WHITE)
    print("     Main Menu")
    print("---------------------")
    print("1. Start a new game")
    print("2. See the High Score")
    print("3. Exit")
    print("")
    # If anything other than a number is entered display an error message
    try:
        opt = int(input("Make a selection: " + Fore.BLUE))
        print(Fore.WHITE)
    except ValueError:
        print(Fore.RED + "That is not a valid selection.")
        input(Fore.WHITE + "Press ENTER to continue")
        continue
    if opt == 1:
        # Creates a list to store the questions that were already asked so there are no repeats.
        questions_asked = []
        # Sets the number of questions asked for each game
        rounds = 5
        rnd = 1
        # Set the score to 0
        score = 0
        genre_opt = 0

        # Ask what Genre the questions should come from
        while genre_opt == 0:
            os.system('cls')
            print("Select a Category:")
            print("---------------")
            print("1. Animals")
            print("2. History")
            print("3. Geography")
            print("4. Random Category")
            print("")
            try:
                genre_opt = int(input("Make a selection: " + Fore.BLUE))
                print(Fore.WHITE)
            except ValueError:
                print(Fore.RED + "That is not a valid selection.")
                input(Fore.WHITE + "Press ENTER to continue")
                genre_opt = 0
                continue

            if genre_opt == 4:
                genre_opt = random.randint(1, 3)
            if genre_opt == 1:
                genre_opt = "Animals"
                genre_file = "animals.csv"
            elif genre_opt == 2:
                genre_opt = "History"
                genre_file = "history.csv"
            elif genre_opt == 3:
                genre_opt = "Geography"
                genre_file = "geography.csv"
            else:
                print(Fore.RED + "That is not a valid selection.")
                input(Fore.WHITE + "Press ENTER to continue")
                genre_opt = 0
                continue
        load_questions(genre_file)
        # round loop
        while rnd <= rounds:
            display_question(random.randint(0, len(questions)-1), genre_opt)
            rnd = rnd + 1
        if score > high_score:
            high_score = score
            os.system('cls')
            print("")
            print("")
            magicsound("high_score.wav", False)
            flashy_words(f"You set a new High Score: {high_score}")
    elif opt == 2:
        os.system('cls')
        print("")
        print("The high score is: " + Fore.GREEN + f"{high_score}")
        print(Fore.WHITE + "")
        input("Press ENTER to continue")
    elif opt == 3:
        still_playing = 0
    else:
        print(Fore.RED + "That is not a valid selection")
        input(Fore.WHITE + "Press ENTER to continue")
