# Factorial Calculator App

A Python application that demonstrates factorial calculations using both built-in and recursive implementations, with built-in safety limits to prevent stack overflow.

## Description

This application showcases two different approaches to factorial calculation:
- Python's built-in math.factorial() implementation
- Custom recursive algorithm implementation

The app includes input validation and stack overflow prevention, making it suitable for educational and practical use.

## Features

- Input validation with upper limit (900) to prevent stack overflow
- Visual representation of factorial mathematical notation
- Dual calculation methods for result verification
- User-friendly error handling
- Stack overflow prevention
- Clear output formatting

## How to Use

1. Run the program
2. Enter a positive integer (1-899) when prompted
3. The program will display:
   - Factorial notation (e.g., 5! = 1*2*3*4*5)
   - Math library calculation result
   - Custom recursive algorithm result
   - Verification of matching results

## Example Output
```
Welcome to My Factorial Calculator app!
What number would you like to compute the factorial of: 5
5! = 1*2*3*4*5
Here is the result from the math library:
The factorial of 5 is 120!
Here is the result from my own recursive algorithm:
The factorial of 5 is 120!
Both calculations Match!!
```

## Requirements
- Python 3.x
- math library (included in Python standard library)

## Installation
1. Clone this repository
2. No additional packages needed
3. Run `python factorial_calculator.py`

## Author
Sergio Figueroa