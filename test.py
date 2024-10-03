import re
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def validate_expression(expression):
    pattern = r'^[0-9+\-*/().\s]+$'
    return re.match(pattern, expression) is not None

def infix_to_rpn(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    output = []
    operators = []
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        else:
            while operators and precedence[operators[-1]] >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output


# 3. Function to build a binary expression tree from RPN
def rpn_to_tree(rpn):
    stack = []
    for token in rpn:
        if token.isdigit():
            stack.append(Node(token))
        else:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]


# 4. Function to evaluate the expression tree
def evaluate_tree(node):
    if node.left is None and node.right is None:
        return int(node.value)

    left_value = evaluate_tree(node.left)
    right_value = evaluate_tree(node.right)

    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        return left_value / right_value


# 5. Function to print the tree and show step-by-step calculation
def print_tree_step_by_step(node):
    if node is None:
        return
    print_tree_step_by_step(node.left)
    print_tree_step_by_step(node.right)
    if node.left and node.right:
        print(f"Calculating: {node.left.value} {node.value} {node.right.value}")


# Main function to handle user input and display the final result
def calculate(expression):
    if not validate_expression(expression):
        print("Invalid expression!")
        return

    print("Valid expression.")

    rpn = infix_to_rpn(expression)
    print(f"RPN: {rpn}")

    tree = rpn_to_tree(rpn)

    print("Step by step calculation:")
    print_tree_step_by_step(tree)

    result = evaluate_tree(tree)
    print(f"Final result: {result}")


# Example Usage
if __name__ == "__main__":
    user_input = input("Enter a mathematical expression: ")
    calculate(user_input)
