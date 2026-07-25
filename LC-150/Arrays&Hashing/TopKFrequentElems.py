class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        counts = [[] for i in range(len(nums) + 1)]

        for key, value in hashmap.items():
            counts[value].append(key)
        
        result = []
        for i in counts[::-1]:
            for num in i:
                result.append(num)
                if len(result) == k:
                    return result
        
        return False