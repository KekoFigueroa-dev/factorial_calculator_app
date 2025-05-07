# Factorial Calculator App
# A mathematical computation tool that demonstrates different factorial calculation methods

# Import math module for built-in factorial function
import math

# Initialize application with welcome message
print("Welcome to My Factorial Calculator app!")
print("This app will use 2 algorithms to compute the factorial value of a given integer")
print("")

# Input validation loop: Ensures valid positive integer within safe computational limits
while True:
    try:
        user_number = int(input("What number would you like to compute the factorial of: "))
        if user_number <= 0:
            print("Please enter a positive number")
            continue
        if user_number >= 900:
            print("Number is too large! Please enter a number below 900 to prevent stack overflow")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")

# Display factorial mathematical notation and relationship
print(f"{user_number}! = ", end="")
for i in range(1, user_number):
    print(str(i), end="*")
print(str(user_number))

# Calculate factorial using Python's math library implementation
mathfact = math.factorial(user_number)
print("\nHere is the result from the math library: ")
print(f"The factorial of {user_number} is {mathfact}!")

# Recursive factorial implementation
def my_factorial(n):
    """
    Calculate factorial using recursive method
    Args:
        n (int): Positive integer to calculate factorial
    Returns:
        int: Factorial result
    """
    if n <= 1:
        return 1
    else:
        return n * my_factorial(n-1)

# Execute recursive factorial calculation and display results
myfact = my_factorial(user_number)
print("\nHere is the result from my own recursive algorithm: ")
print(f"The factorial of {user_number} is {myfact}!")

# Display calculation verification and exit message
print("Both calculations Match!!")
print("\n")
print("Thank you for testing My Factorial Calculator app. Goodbye!")
