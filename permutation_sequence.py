class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(map(str, range(1, 10))) #List of numbers from 1 to 9
        k -= 1
        factorial = [1] * n #Initialize a list to store factorials

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i #Calculate factorials
        result = []
        
        for i in range(n):
            index = k // factorial[n - 1 - i] #Get the index of the current digit
            result.append(nums[index]) #Append the selected digit to result
            nums.pop(index) #Remove the selected digit from the available numbers in nums
            k = k % factorial[n - 1 - i] #Update k for next iteration
        return ''.join(result)

if __name__ == "__main__":
    solution_instance = Solution()
    n = int(input("n = "))
    k = int(input("k = "))
    print(solution_instance.getPermutation(n, k))
