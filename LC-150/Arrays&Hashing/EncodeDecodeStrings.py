class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += str(len(i)) + "#" + i
        return string

    def decode(self, s: str) -> List[str]:
        result = []

        pointer = 0
        while pointer < len(s):
            length = ""
            while s[pointer] != "#":
                length += s[pointer]
                pointer += 1
            
            length_num = int(length)
            result.append(s[pointer + 1:pointer + length_num + 1])
            pointer = pointer + length_num + 1
        
        return result