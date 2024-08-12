def factorial(n):
  if n == 0:  # Base case
    return 1
  else:  # Recursive case
    return n * factorial(n - 1)
num = factorial(100)
print(num)