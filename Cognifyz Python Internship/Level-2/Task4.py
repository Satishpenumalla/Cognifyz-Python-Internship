def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Enter the number of terms for Fibonacci sequence: "))
if n <= 0:
   print("Please enter a positive integer.")
else:
  fib_seq = fibonacci_sequence(n)
  print(f"Fibonacci sequence up to {n} terms:")
  print(fib_seq)
