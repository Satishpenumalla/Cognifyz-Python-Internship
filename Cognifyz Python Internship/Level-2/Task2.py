import random

def guess_number(a, b):
    rand_int = random.randint(a, b)

    while True:

        number = int(input(f"Guess the number between {a} and {b}: "))

        if rand_int < number:
          print("The entered number is too high.")
        elif rand_int > number:
          print("The entered number is too low.")
        else:
          print("Congratulations! You guessed the right number.")
          break
        

a, b = map(int, input("Enter the range to guess the number : ").split())
guess_number(a, b)
