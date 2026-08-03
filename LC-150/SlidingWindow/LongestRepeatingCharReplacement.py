class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        maxlen = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            if (r - l + 1) > k + max(hashmap.values()):
                hashmap[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)

        return maxlen