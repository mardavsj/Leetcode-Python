class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        length = 1
        previous = nums[0]
        index = 1
        for i in range(1,len(nums)):
            if nums[i] != previous:
                length += 1
                previous = nums[i]
                nums[index] = nums[i]
                index+=1
        return length
input_list = [1,1,2,2,2,3,3,3,3,4,5,5,5,6]
ob1 = Solution()
print(ob1.removeDuplicates(input_list))
        