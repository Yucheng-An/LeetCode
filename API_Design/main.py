import sys
import API

def main():
    if len(sys.argv) < 2:
        print("Run the script with '-help' to see usage information.")
        return

    command = sys.argv[1]
    arguments = sys.argv[2:]  # Additional arguments beyond the command

    if command == "-help":
        print_help()
    elif command == "-sum":
        calculate_sum(arguments)
    else:
        print(f"Unknown command: {command}")
        print("Run the script with '-help' to see usage information.")
    


def print_help():
    help_text = """
    Authors: Ramis H., Yucheng A., Bex A.
    Usage: python script.py [command] [arguments]

    Commands:
    -help               Show this help message and exit.
    -balanced <expression>      Check if mathematical expression is balanced or not. Returns True or False.
    """
    print(help_text)



def check_balanced_expression(expression):
    balance = []
    popped = ''
    for i in expression:
        if i == {'(', '{', '['}:
            balance.append(i)

        elif i == {')', '}', ']'}:
            if not balance:
                return False
            else:
                if balance.pop() == i:
                    balance.pop()
                else:
                    return 'not matched'

    '''
    Initialize an Empty Stack:
        Create an empty stack that will be used to keep track of the opening brackets encountered as we iterate through the expression.
    Traverse the Expression Character by Character:
        Iterate through each character of the string expression:
            If an opening bracket ((, {, [) is encountered, push it onto the stack.
            If a closing bracket (), }, ]) is encountered:
                Check if the stack is empty:
                    If the stack is empty, return False since it means there is a closing bracket without a matching opening bracket.
                Otherwise, pop the top element from the stack. Then,
                    Compare the popped element with the closing bracket:
                        If the popped element does not match (for example, if [ is the last opening but } is encountered), return False.
    Check Stack Finally:
        Check if Stack is Empty:
            If it's empty, return True
            If it's not empty, return False

    :param expression: str - expression entered by user using CLI
    :return: bool - is expression balanced?
    '''
    pass

def process_user_input():
    '''
    We will need function which will allow user to choose menu options in future app.
    '''
    pass

def calculate_sum(arguments):
    try:
        numbers = [float(arg) for arg in arguments]
        result = sum(numbers)
        print(f"The sum of the given numbers is: {result}")
    except ValueError:
        print("Error: Please provide numeric values only for the '-sum' command.")


if __name__ == "__main__":
    main()
    API.count_character_frequency("test")
    # Define the list of values to create a BST
    values = [15, 10, 20, 5, 12, 18, 25]

    # Call the drawtree function
    tree_visual = API.drawtree(values)

    # Print the visual representation of the BST
    for line in tree_visual:
        print(line)

    # Quicksort:
    unsorted_array = [33, 10, 55, 71, 29, 1, 22]
    sorted_array = API.quicksort(unsorted_array)
    print("\n Quicksorted array:", sorted_array, "\n")

    # Bubblesort:
    unsorted_array = [33, 10, 55, 71, 29, 1, 22]
    sorted_array = API.bubble_sort(unsorted_array)
    print("\n Sorted array:", sorted_array)

    
