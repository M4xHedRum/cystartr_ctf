import random

def game():
    remaining_tries = 32
    answer = random.randint(1,1000000000) 
    while remaining_tries > 0:
        try:
            guess = int(input("Guess an integer btw 1 and 1 billion\n")) 
            if guess == answer:
                print("You got it right! DoHCTF{automation_is_king_}\n")
                return
            elif guess < answer:
                print("Higher\n")
            else:
                print("Lower\n")
            remaining_tries -= 1
        except ValueError:
            print("Not a valid integer. Please try again.\n")
    print("Out of tries. Game over!\n")

game()
