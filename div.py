try:
  a=int(input("Enter first number:"))
  b=int(input("Enter second number:"))
  print(f"Addition:{a+b}")
  print(f"Subtartion:{a-b}")
except ValueError:
  print("Please enter valid number.")
  
