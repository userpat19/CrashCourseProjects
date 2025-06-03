class Solution(object):
    def isPalindrome(self, x):

        palindrome = True
        
        self.x = x

        reverse_list = []

        while self.x > 0:
            reverse_list.append(self.x % 10)
            self.x //= 10


        for x in len(reverse_list):

            if reverse_list.reverse()[x-1] != reverse_list[x-1]:
                palindrome = False

        if palindrome:
            return "true"
        else:
            return "false"
        

num = 121

var = Solution()

print(var.isPalindrome(num))