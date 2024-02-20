class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip('"\'')

        passed_dot = passed_e = passed_digit = False

        for i, char in enumerate(s):
            if char in '+-':
                if i > 0 and s[i-1].lower() != 'e': #If the sign is not in the beginning and the preceding character is not e, it's invalid
                    return False
            elif char == '.':
                if passed_dot or passed_e: #If the . is preceded by . or exponent e, it's invalid
                    return False
                passed_dot = True
            elif char.lower() == "e": 
                if passed_e or not passed_digit: #If the e is preceded by another e or there's no digit before it, it's invalid
                    return False
                passed_e, passed_digit = True, False
            elif char.isdigit():
                passed_digit = True
            else:
                return False
        return passed_digit

if __name__ == "__main__":
    solution_instance = Solution()
    user_input_str = input("s = ")
    result = solution_instance.isNumber(user_input_str)
    print(str(result).lower())