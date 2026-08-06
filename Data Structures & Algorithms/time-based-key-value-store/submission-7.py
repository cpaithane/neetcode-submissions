class TimeMap:
    kv_dict = {}
    def __init__(self):
        # Dictionary of str -> {(TS1, val1), (TS2, val2)}
        self.kv_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val_list = self.kv_dict.get(key, [])
        val_list.append((timestamp, value))
        self.kv_dict[key] = val_list

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.kv_dict.get(key, [])
        
        # Do a binary search
        l = 0
        r = len(val_list) - 1
        res = ""

        while l <= r:
            m = (l + ((r - l) // 2))
            print(l, m, r, val_list)
            if val_list[m][0] <= timestamp:
                res = val_list[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
