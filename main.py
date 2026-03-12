def is_balanced(inp):
    print(f"Processing {inp}")
    state = 'q0'
    stack = ['Z']
    
    def get_stack_str(s):
        return "".join(reversed(s))

    for i, char in enumerate(inp):
        print(f"ID: ({state}, {inp[i:]}, {get_stack_str(stack)})")
        
        if state == 'q0':
            if char == '!':
                state = 'q1'
                stack.append('!')
            else:
                print(f"Invalid string. Failed at position {i+1}.")
                print(f"Remaining unprocessed input string: {inp[i:]}")
                return False

        elif state == 'q1':
            if char == 'x':
                continue
            elif char in opening:
                stack.append(char)
            elif char in brackets:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    print(f"Invalid string. Failed at position {i+1}.")
                    print(f"Remaining unprocessed input string: {inp[i:]}")
                    return False
            elif char == '!':
                if stack[-1] == '!':
                    stack.pop()
                    state = 'q2'
                else:
                    print(f"Invalid string. Failed at position {i+1}.")
                    print(f"Remaining unprocessed input string: {inp[i:]}")
                    return False
            else:
                print(f"Invalid string. Failed at position {i+1}.")
                print(f"Remaining unprocessed input string: {inp[i:]}")
                return False
        
        elif state == 'q2':
            print(f"Invalid string. Failed at position {i+1}.")
            print(f"Remaining unprocessed input string: {inp[i:]}")
            return False

    print(f"ID: ({state}, E, {get_stack_str(stack)})")
    if state == 'q2':
        print("q2 is a final state.")
        print(f"{inp} is valid and has balanced brackets.")
        return True
    else:
        print(f"Invalid string. {state} is not a final state.")
        return False

def evaluate(inp):
    content = inp.strip('!')
    stack = [0]
    for char in content:
        if char == 'x':
            stack[-1] += 1
        elif char in opening:
            stack.append(char)
            stack.append(0)
        elif char in closing:
            inner_count = stack.pop()
            opening_bracket = stack.pop()
            
            if opening_bracket == "<":
                result = 2 * inner_count
            elif opening_bracket == "{":
                result = inner_count + 1
            elif opening_bracket == "[":
                result = 0
            elif opening_bracket == "(":
                result = max(0, inner_count - 1)
            else:
                result = 0
            stack[-1] += result

    total_X = stack[0]
    return total_X

def main1(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    valid_strings[clean_line] = is_balanced(clean_line)
                    print("")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def main2(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line and valid_strings[clean_line]:
                    total_X = evaluate(clean_line)
                    print(f"{clean_line} - Resulting number of x's: {total_X}")
                else:
                    print(f"{clean_line} - Invalid string.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    valid_strings = {}
    brackets = {">":"<", "}":"{", "]":"[", ")":"("}
    opening = {"<", "{", "[", "("}
    closing = {">", "}", "]", ")"}
    input_file = './input.txt'
    main1(input_file)
    main2(input_file)

