class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict.keys():
            self.dict[key] = [(value, timestamp)]
        else:
            self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        key_lst = self.dict.get(key, [])
        result = ""
        l = 0
        r = len(key_lst) - 1

        while l <= r:
            idx = (l + r) // 2
            if key_lst[idx][1] <= timestamp:
                l = idx + 1
                result = key_lst[idx][0]
            else:
                r = idx - 1
        
        return result
        
