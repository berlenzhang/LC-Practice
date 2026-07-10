class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            alphabet = [0] * 26
            for char in i:
                alphabet[ord(char) - ord('a')] += 1
            hashmap[tuple(alphabet)].append(i)
        
        return list(hashmap.values())