class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset={}
        for i in nums:
            if i in hset:
                return True
            hset[i]=1
        return False