class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]: #Return immediately if the word is a palindrome already
            return s
        else:
            left = '' #Empty string to build characters from the right side of s and concatenate them to the left
            for i in range(len(s)):
                left += s[(len(s)-1)-i] #Concatenating letters from right to left

                if (left + s) == (left + s)[::-1]: #If left and s is a palindrome, it is the shortest palindrome formed
                    return left + s

if __name__ == "__main__":
    solution_instance = Solution()
    user_input_str = input("s = ")
    print(solution_instance.shortestPalindrome(user_input_str))