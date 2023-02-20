''' 

Implement a calculator for simple arithmetic expressions in revese polish 
notation. (4 points)

The reverse polish notation notation 

Reverse Polish notation (RPN) is a mathematical notation in which every
operator follows all of its operands. It is also known as postfix
notation and does not need any parentheses as long as each operator has a fixed
number of operands. For instance, the expression

    5 + ((1 + 2) * 4) − 3

is written in RPM as

    5 1 2 + 4 * + 3 −

(see Wikipedia for more details.)

Algorithm:

Datastructure: A stack (list) which stores the operands

while there are input tokens left
    read the next token from input.
    if the token is a value
        push (append) it onto the stack.
    otherwise, the token must be an operator (+, -, *, /)
        pop (remove) the last two operators from the stack
        apply the operator to these two values
        push the result to the stack

When applied to well-formed input, the stack will contain a single value
at the end.

NOTE: 

Your implementation should raise an ArithmeticException when the function is
applied to a string which is not a well-formed expression. For instance,

$ python3 calc.py "5 1 2 + 4 * + 3 −"
14

$ python3 calc.py '5 1 2 + 4 * + 3'
Invalid input

$ python3 calc.py '5 + 2'
Invalid input

'''

import sys

def calc(tokens):
    stack = []

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            # Pop the last two operands from the stack if possible , if its not possible then its not well formed expression
            try:
                operand2 = stack.pop()
                operand1 = stack.pop()
            except IndexError:
                return "Invalid input"


            # Apply the operator to the operands
            #eval functuion takes in the arguments and evaluate them as the input to the python. 
            # for example given the arguments 1 , + and 2..it will process it as 1+2 and will return 3. 
            # I found this function by googling about this as i had heard about this. more details of the function are here: https://realpython.com/python-eval-function/  
            result = eval(f"{operand1} {token} {operand2}")

            # Push the result to the stack
            stack.append(result)
        else:
            # Token is an operand, so push it to the stack
            stack.append(int(token))

    # the stack should have only one value as mentioned in the question
    if len(stack) != 1:
        return "Invalid input"

    return stack[0]

def main():
    try:
        print(calc(sys.argv[1].split()))
    except ArithmeticError:
        print('Invalid input')

if __name__ == '__main__':
    main()
