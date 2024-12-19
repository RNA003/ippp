import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def infix_to_postfix(expression):

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    # neg handle
    expression = expression.replace("--","+")
    expression = expression.replace("- ","-")

    for char in expression:
        if char.isdigit():
            output.append(char)
        elif char.isalpha():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        elif char == '-':
            if not stack or stack[-1] in ('(', '+', '-'):
                output.append('0')
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infix_to_prefix(expression):

    reversed_expression = expression[::-1]
    reversed_postfix = infix_to_postfix(reversed_expression)
    return reversed_postfix[::-1]

def evaluate_postfix(expression):

    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char.isalpha():
            stack.append(sp.Symbol(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2
            stack.append(result)

    return stack.pop()

def handle_variable_expression(expression):

    # x = sp.Symbol('x')
    # y = sp.sympify(expression)
    #
    # # Convert to postfix and evaluate
    # postfix_expression = infix_to_postfix(expression)
    # result = evaluate_postfix(postfix_expression)
    #
    # # Plot the function based on the result (numeric or symbolic)
    # if isinstance(result, sp.Symbol):
    #     print("Expression is symbolic. Plotting cannot be done directly.")
    # else:
    #     x_vals = np.linspace(-2, 2, 100)  # Adjust the range as needed
    #     y_vals = []
    #     for val in x_vals:
    #         try:
    #             y_vals.append(float(result.subs(x, val)))
    #         except ValueError:
    #             # Handle complex values or other errors
    #             y_vals.append(np.nan)
    #
    #     plt.plot(x_vals, y_vals)
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid(True)
    #     plt.show()

    x = sp.Symbol('x')
    y = sp.sympify(expression)

    postfix_expression = infix_to_postfix(expression)
    result = evaluate_postfix(postfix_expression)

    if isinstance(result, sp.Symbol):
        print("this is symb")
    else:
        x_vals = np.linspace(-10, 10, 100)
        y_vals = [result.subs(x, val) for val in x_vals]
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    x = sp.Symbol('x')
    y = sp.sympify(expression)

    # Plot the function
    x_vals = np.linspace(-10, 10, 100)
    y_vals = [y.subs(x, val) for val in x_vals]
    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def main():
    while True:
        expression = input("Enter an infix expression (or 'q' to quit): ")
        if expression == 'q':
            break

        # postfix_expression = infix_to_postfix(expression)
        # prefix_expression = infix_to_prefix(expression)


        try:
            if any(char.isalpha() for char in expression):
                handle_variable_expression(expression)
            else:
                
                postfix_expression = infix_to_postfix(expression)
                prefix_expression = infix_to_prefix(expression)
                result = evaluate_postfix(postfix_expression)
                print("Postfix expression:", postfix_expression)
                print("Prefix expression:", prefix_expression)
                print("Result:", result)

            # if any(char.isalpha() for char in expression):
            #     handle_variable_expression(expression)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

# infix_expression = "2*(3-1+5^2)"
# postfix_expression = infix_to_postfix(infix_expression)
# prefix_expression = infix_to_prefix(infix_expression)
#
# print("Postfix expression:", postfix_expression)  # Output: 231-52^+*
# print("Prefix expression:", prefix_expression)    # Output: *2+3-1^52
#
# postfix_expression = "231-52^+*"
# result = evaluate_postfix(postfix_expression)
# print("Result:", result)  # Output: 44
#
# expression = "x^2 + 2*x - 1"
# handle_variable_expression(expression)
# print(handle_variable_expression(expression))
#
# infix_expression = "2*(3-1+5^2)"
# postfix_expression = infix_to_postfix(infix_expression)
# prefix_expression = infix_to_prefix(infix_expression)
#
# print("Postfix expression:", postfix_expression)
# print("Prefix expression:", prefix_expression)
#
# result = evaluate_postfix(postfix_expression)
# print("Result:", result)
#
# # Example with variables and plotting
# expression = "x^2 + 2*x - 1"
# handle_variable_expression(expression)