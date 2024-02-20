class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        l = ['0'] * len(s) #Initialize a list with length n of values 0s for tracing valid parentheses

        for i, char in enumerate(s):
            if char =='(':
                stack.append(i) #Push index onto the stack
            else: 
                if stack:
                    if s[i-1] =='(':
                        l[stack.pop()] = '1' #Pop the index of the corresponding open parenthesis and set its value to 1 in l
                        l[i] = '1' #Set the value of the current closing parenthesis to 1 in l

        n = max(len(char) for char in ''.join(l).split('0')) #Join list into string, split at occurrences of 0, and find the maximum length of consecutive sequences of 1
        return n

if __name__ == "__main__":
    solution_instance = Solution()
    user_input_str = input("s = ")
    print(solution_instance.longestValidParentheses(user_input_str))