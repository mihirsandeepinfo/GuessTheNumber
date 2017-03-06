import random

def is_valid_num(s):
    if s.isdigit() and 1<= int(s) <=100:
        return True
    else:
        return False

def main():
    number = random.randint(1,100)
    guessed_number = False
    guess = input("Enter a number between 1 and 100: ")
    num_guesses = 0
    while not guessed_number:
        if not is_valid_num(guess):
            guess = input("Wont count that one. Number between 1 and 100 please: ")
            continue
        else:
            num_guesses+=1
            guess = int(guess)

        if guess<number:
            guess = input("Too Low: ")
        elif guess>number:
            guess = input("Too High: ")
        else:
            print("You got it in",num_guesses,"tries")
            guessed_number=True

main()
