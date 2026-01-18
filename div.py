try:
  a=int(input("Enter first number:"))
  b=int(input("Enter second number:"))
  print(f"Addition:{a+b}")
  print(f"Subtartion:{a-b}")
  print(f"Multiplication:{a*b}")
  if b!=0:
    print(f"Division:{a/b}")
  else:
    print("Division not possible by zero.")  
except ValueError:
  print("Please enter valid number.")
  
