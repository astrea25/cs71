def is_balanced(inp):
    print(f"Processing {inp}")
    state = 'q0'
    stack = ['Z']
    brackets = {">":"<", "}":"{", "]":"[", ")":"("}
    opening = {"<", "{", "[", "("}
    
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

    if state == 'q2':
        print(f"ID: ({state}, E, {get_stack_str(stack)})")
        print("q2 is a final state.")
        print(f"{inp} is valid and has balanced brackets.")
        return True
    else:
        print(f"Invalid string. String ended in non-final state {state}.")
        return False

def main1(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    is_balanced(clean_line)
                    print("")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    input_file = './input.txt'
    main1(input_file)

