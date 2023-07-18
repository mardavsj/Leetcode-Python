class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        xor2=0
        n=len(nums)
        for i in range(n):
            xor1^=nums[i]
            xor2^=i+1
        return xor1^xor2