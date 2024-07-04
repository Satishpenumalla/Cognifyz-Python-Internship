import random

rand_int = random.randint(1,100)
print("Guess the number between 1 and 100")
def guess_number():
    while True:
        number = int(input("Guess the number : "))

        if rand_int < number:
            print("The entered number is too high.")
        elif rand_int > number:
            print("The entered number is too low.")
        else:
            print("Congratulations! You guessed the right number.")
            break


guess_number()




