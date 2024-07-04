import random
lower_bound = 1
upper_bound = 50
max_attempts = 10
secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between {0} and {1}: ".format(lower_bound, upper_bound)))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid Input.Please Enter a Number in the specified range")
        except ValueError:
            print("Invalid Input. Please enter a  valid integer.")

def check_guess(secret_number,guess):
    if secret_number == guess:
        return "Correct"
    elif  guess < secret_number:
        print("Your Guess is too Low!🤭 Try Again.")
    else:
        print("Your Guess is too High!🤔 Try Again.")

def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts +=1
        user_guess = get_guess()
        checks = check_guess(secret_number,user_guess)

        if checks == "Correct":
            print(f"Congrats🎊🥳🎉!! You Guessed the secret Number {secret_number} in {attempts} Attempts")  
            won = True
            break
        # else:
        #     print(f"{checks} Try Again")
            
    if not won:
        print("Game Over!🥹 The Secret Number was {}".format(secret_number))

        
if  __name__=="__main__":
    print("\n*************   Welcome to the Number Guessing game🤩  ******************\n")
    play_game()
