#DETECTING A PALINDROME NUMBER WITHOUT CONVERTING IT INTO A STRING

class Solution:

    def __init__(self, num):
        self.num = num

    def is_Palindrome(number):

        isPalindrome = True

        reverse = []

        numero = number

        if numero < 0:

            isPalindrome = False

        else:

            while numero > 0:
                reverse.append(numero % 10)
                numero //= 10

            original = reverse[::-1]

            for x in range(len(original) - 1):

                if original[x] != reverse[x]:
                    isPalindrome = False
                    break

        if isPalindrome:
            return True
        else:
            return False
        
            



number = int(input("Enter the number to detect:"))

Variable = Solution

print(Variable.is_Palindrome(number))