class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        n = len(nums)
        for i in range(n):
            need = target - nums[i]
            if need in hash:
                return [hash[need], i]
            hash[nums[i]] = i


