def add(x, y):
   return x + y

print("Select operation.")
print("1.Add")

choice = input("Enter choice(1):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
else:
   print("Invalid input")
