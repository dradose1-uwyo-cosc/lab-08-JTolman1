# Jared Tolman
# UWYO COSC 1010
# Nov 10th, 2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to: Help received from TA and Google searches
# For part 2, I tried to get zero inputs to work, but for some reason the fix broke the other condition on each if/elif line allowing
# values that should have been flagged as 'False' to pass through.


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(string):
    # Converts and checks if a string is an integer or a float.
    if string.isdigit() or (string[0] == '-' and string[1:].isdigit()):
        return int(string)
    
    try:
        if string.count('.') == 1:
            float1 = float(string)
            if float1.is_integer():
                return int(float1)
            return float1
    except ValueError:
        pass
    
    return False

string_input=input(f"Please enter a numerical value to test part 1: ")
print(convert(string_input))

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,x_low,x_up):
    x_values=range(x_low,x_up+1)
    y_values=[]
    for x in x_values:
        y=m*x+b
        y_values.append(y)
    return y_values

state=True
while state==True:
    m1=input(f"Please enter a value for slope: ")
    m=convert(m1)
    b1=input(f"Please enter a value for y-intercept: ")
    b=convert(b1)
    x_low1=input(f"Please enter an integer for a lower bound for x: ")
    x_low=convert(x_low1)
    x_up1=input(f"Please enter an integer for an upper bound for x: ")
    x_up=convert(x_up1)
    if convert(m1)==False:# and m!=0:
        print(f"Enter a supported value for slope")
        continue
    elif convert(b1)==False:# and b!=0:
        print(f"Enter a supported value for y-intercept")
        continue
    elif convert(x_low1)==False:# and b!=0:
        print(f"Enter an integer for the lower x bound")
        continue
    elif "." in x_low1:
        print(f"Enter an integer for the lower x bound")
        continue
    elif convert(x_up1)==False:# and b!=0:
        print(f"Enter an integer for the upper x bound")
        continue
    elif "." in x_up1:
        print(f"Enter an integer for the upper x bound")
        continue
    elif x_low>=x_up:
        print(f"Upper x bound must be greater than lower x bound")
        continue
    print(f"The y-values of this function are {slope_intercept(m,b,x_low,x_up)}")
    choice=input(f"Please type 'exit' to exit, otherwise press 'Enter': ")
    if choice.lower()=='exit':
        state=False


print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_formula(a,b,c):
    x1=((-1)*b+(b**(2)-4*a*c)**(1/2))/(2*a)
    x2=((-1)*b-(b**(2)-4*a*c)**(1/2))/(2*a)
    return print(f"The roots of the function are '{x1}' and '{x2}'")

state1=True
while state1==True:
    a=input(f"Please enter a value for a: ")
    a=convert(a)
    b=input(f"Please enter a value for b: ")
    b=convert(b)
    c=input(f"Please enter a value for c: ")
    c=convert(c)
    if a==False and a!=0:
        print(f"Enter a supported value for a")
        continue
    elif b==False and b!=0:
        print(f"Enter a supported value for b")
        continue
    elif c==False and c!=0:
        print(f"Enter a supported value for c")
        continue
    print(quadratic_formula(a,b,c))
    choice1=input(f"Please type 'exit' to exit, otherwise press 'Enter': ")
    if choice1.lower()=='exit':
        state1=False