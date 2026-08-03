class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        hashmap = {}

        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
            hashmap[s[r]] = r
            length = max(length, r - l + 1)
        return length
