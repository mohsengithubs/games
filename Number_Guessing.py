from random import randint


def start(f, t):
    global magic_number
    global attempts

    magic_number = randint(int(f), int(t))
    attempts = 0

    print("______________________")
    print(f"guess the number between {f} and {t}")


def check_win(player_guess):
        if player_guess > magic_number:
            print("to big")
        elif player_guess < magic_number:
            print("to small")
        elif player_guess == magic_number:
            return True



if __name__ == "__main__":
    try:
        f = input("enter the first number: ")
        t = input("enter the last number: ")
        if int(t) < int(f):
            raise ValueError('last number must be greater than the first number')
        
        start(f,t)


        while True:
            guess = int(input())
            attempts += 1

            if check_win(guess):
                print("You won! - Number of attempts: " + str(attempts))
                keep_playing = input("keep plying? (y/n)")
                if keep_playing.lower() == "y":
                    attempts == 0
                else:
                    quit()
                start(f,t)
            else:
                check_win(guess)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    