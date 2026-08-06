class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv_dict = {}
        self.lru_list = []

    def get(self, key: int) -> int:
        if key in self.lru_list:
            self.lru_list.remove(key)
            self.lru_list.insert(0, key)
            return self.kv_dict.get(key, -1)

        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lru_list:
            self.lru_list.remove(key)
        
        self.lru_list.insert(0, key)
        self.kv_dict[key] = value

        if len(self.kv_dict) > self.capacity:
            print("put:", self.lru_list)
            evict_key = self.lru_list[len(self.lru_list) - 1]
            print("evict_key", evict_key)
            self.lru_list.remove(evict_key)
            del self.kv_dict[evict_key]
        