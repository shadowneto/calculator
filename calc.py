'''
FELIX ONGARO OMBONGI
SCT211-0017/2022
'''

#This is a simple python calculator that takes an expression from the user and evaluates it
print('This calcuator can only do +, -, *, /, % \
       use ** for power   not ^,  do not also use parenthesis')
print('To use this calculator enter an entire expression below e.g., 2+3*5 :')

while True:
    try:
        expression = input("Enter your expression: ")
        result = eval(expression)
        print(result)
    except NameError:
        print("Please enter real numbers only")
    

    continuearthmetic = input("Type y to do another expression, q to QUIT:").lower()
    if continuearthmetic == 'q':
        break
    else:
        continue

