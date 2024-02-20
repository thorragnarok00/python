
def is_valid_number(self, s):
    """
    :type s: str
    :rtype: bool
    """
    n = s.strip()

    passed_dot = passed_e = passed_digit = False

    for i, char in enumerate(n):
        if char in '+-':
            if i > 0 and n[i-1].lower() != 'e':
                return False
        elif char == '.':
            if passed_dot or passed_e: return False
            passed_dot = True
        elif char.lower() == 'e':
            if passed_e or not passed_digit:
                return False
            passed_e, passed_digit = True, False
        elif char.isdigit():
            passed_digit = True
        else:
            return False
    return passed_digit
    
def user_input():

    user_input_str= input("Your input: ")
    print(is_valid_number(is_valid_number, user_input_str))

if __name__ == "__main__":
    user_input()