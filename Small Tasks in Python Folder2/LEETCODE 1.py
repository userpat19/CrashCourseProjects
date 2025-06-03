# TWO SUM

class Solution(object):

    def two_sum(self, nums, target):

        self.nums = nums
        self.target = target

        seen = {}

        for i, num in enumerate(self.nums):

            diff = self.target - num


            if diff in seen:

                return[seen[diff], i]
            
            seen[num] = i

        return []




list_num = [1,2,5,6,7,8,5,3,4]

target_num = 13

var = Solution()

print(var.two_sum(list_num, target_num))