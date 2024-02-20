class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] #Stack to store result and sign
        result = 0
        sign = 1
        i = 0

        while i < len(s):
            
            if s[i].isdigit():
                val = int(s[i])

                while i + 1 < len(s) and s[i+1].isdigit():
                    val = val * 10 + int(s[i+1]) #Handle multi-digit numbers by combining consecutive digits
                    i += 1
                    
                result += val * sign #Update result
            elif s[i] == '+':
                sign = 1 #If the current character is '+', it sets the sign to positive
            elif s[i] == '-':
                sign = -1 #If the current character is '-', it sets the sign to negative
            elif s[i] == '(': #If the current character is '(', it pushes the current result and sign onto the stack, resets the result and sets the sign to positive
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')': #If the current character is ')', it calculates the new result by popping the previous sign and result from the stack then updating the current result
                result = result * stack.pop() + stack.pop()
            i += 1
        return result
    
if __name__ == "__main__":
    solution_instance = Solution()
    user_input_str = input("s = ")
    print(solution_instance.calculate(user_input_str))