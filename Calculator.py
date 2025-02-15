# Python program to create a simple calculator

# 3 Steps to Build Calculator Program
# 1.Functions for Operations
# 2.User Input
# 3.Print Result


# Step 1 Functions for operations

# Function to add numbers

def add(num1, num2):
    return num1+num2

# Function to sub numbers

def sub(num1, num2):
    return num1-num2

# Function to multiply numbers

def multiply(num1, num2):
    return num1*num2

# Function to divide numbers

def divide(num1, num2):
    return num1/num2

# Function to average numbers

def avg(num1, num2):
    return (num1+num2)/2

# Step 2 User Input

while True:
 print('''Please Select a Operation:
 1. Addition
 2. Substraction
 3. Multiplication
 4. Division
 5. Average''')

 select = int(input("Select a Operation from 1,2,3,4,5: "))
 a=int(input("Enter First Number: "))
 b=int(input("Enter Second Number: "))

# Step 3 Print Results

 if select == 1:
    print(f"{a}+{b}= ",add(a,b))
 elif select == 2:
    print(f"{a}-{b}= ",sub(a,b))
 elif select == 3:
    print(f"{a}*{b}= ",multiply(a,b))
 elif select == 4:
    print(f"{a}/{b}= ",divide(a,b))
 elif select == 5:
    print(f"({a}+{b})/2= ",avg(a,b))
 else:
    print("Invalid Operation please select again!")
 repeat2 = input("Do you want to repeat with Main Menu?: ") 
 if repeat2 == "no" or repeat2 == "No":
    break