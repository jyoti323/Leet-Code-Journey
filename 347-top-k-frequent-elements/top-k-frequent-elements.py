class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}

    ##count frequency
        for num in nums:
            count[num]=count.get(num,0)+1

            ##sorted 
            ##it take time colplexity(nlogn)

        sorted_count=sorted(count,key=count.get,reverse=True)

        return sorted_count[:k]



        