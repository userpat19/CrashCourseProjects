class Solution(object):
    def isPalindrome(self, x):

        palindrome = True

        x = str(x)

        original = [item for item in x]

        reverse = original[::-1]

        for x in range(len(original) - 1):

            if reverse[x] != original[x]:

                palindrome = False
                break

        if palindrome:
            return True
        else:
            return False
        

Variable = Solution()

print(Variable.isPalindrome(1011101))

