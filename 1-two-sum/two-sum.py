class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##using hash map

        seen={}

        for i in range(len(nums)):
            num=nums[i]
            compliment=target-num

            if compliment in seen:
                return[seen[compliment],i]

            seen[num]=i
