
#Welcome
def welcome():
    print("Welcome!")
welcome()

#Functions definition
def calculate(): 
    operation = input('''
    Please type the operation you would like to complete: 
    + for addition
    - for subtraction
    / for division
    * for multiplication
    % for module
    Sqrt for square root
    Pow for power
    ''')
    if operation == 'sqrt':
        num1 = float(input("Enter your fisrt number: "))
    else:
        num1 = float(input("Enter your fisrt number: "))
        num2 = float(input("Enter your second number: "))

    import math
#Squareroot    
    if operation == 'sqrt':
        print('{} = '.format(num1))
        print(math.sqrt(num1))        
#Addition
    elif  operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
#Subtraction
    elif operation == '-':
         print('{} - {} ='.format(num1, num2))
         print(num1 - num2)
#Division
    elif operation == '/':
         print('{} / {} ='.format(num1, num2))
         print(num1 / num2)
#Multiplication
    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
#Module
    elif operation == '%':
        print('{} % {} = '.format(num1, num2))
        print(num1 % num2)
#Exponential
    elif operation == 'Pow':
        print('{} ** {} = '.format(num1, num2))
        print(math.pow(num1, num2))
    else:
        print("You have typed an invalid operator, please try again") 

    again()  
def again():
    calc_again = input('''
Would you like to do another operation? 
Type 'Yes' or 'No'.
''')

    if calc_again == 'Yes':
        calculate()

    elif calc_again == 'No':
        print("Okay, see you later!")

    else:    
        print("Invalid")

calculate() 

    


    




