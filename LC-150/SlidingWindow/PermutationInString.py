class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_key = [0] * 26
        s2_key = [0] * 26

        for i in range(len(s1)):
            s1_key[ord(s1[i]) - ord('a')] += 1
            s2_key[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_key[i] == s2_key[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2_key[idx] += 1
            if s2_key[idx] == s1_key[idx]:
                matches += 1
            elif s2_key[idx] - 1 == s1_key[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            s2_key[idx] -= 1
            if s2_key[idx] == s1_key[idx]:
                matches += 1
            elif s2_key[idx] + 1== s1_key[idx]:
                matches -= 1
            
            l += 1

        return matches == 26