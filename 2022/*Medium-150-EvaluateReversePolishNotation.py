'''
stack

stack = new Stack()
for each token in tokens:
    if token is a number:
        stack.push(token)
    else (token is operator):
        number_2 = stack.pop()  
        number_1 = stack.pop()
        result = apply_operator(token, number_1, number_2)
        stack.push(result)
return stack.pop()

time: O(N)
space: O(N)
'''
def evalRPN(self, tokens: List[str]) -> int:
        
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }
    
    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()



'''
recursion
time: O(N**2)
space: O(1)
'''
def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        
        current_position = 0
        
        while len(tokens) > 1:
            
            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-*/":
                current_position += 1
        
            # Extract the operator and numbers from the list.
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])
            
            # Calculate the result to overwrite the operator with.
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)
            
            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1
        
        return tokens[0]

