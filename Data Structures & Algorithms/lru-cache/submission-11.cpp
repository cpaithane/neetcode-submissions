class LRUCache {
private:
    int capacity;
    list<int> lru;
    unordered_map<int, pair<int, list<int>::iterator>> kv;

    void make_recent(int key) {
        lru.erase(kv[key].second);
        lru.push_front(key);
        kv[key].second = lru.begin();
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;    
    }

    int get(int key) {
        if (kv.find(key) == kv.end()) {
            return -1;
        }

        make_recent(key);
        return kv[key].first;
    }
    
    void put(int key, int value) {
        if (kv.find(key) != kv.end()) {
            kv[key].first = value;
            make_recent(key);
            return;
        }

        if (kv.size() >= this->capacity) {
            int ev_key = lru.back();
            kv.erase(ev_key);
            lru.pop_back();
        }

        lru.push_front(key);
        kv[key].first = value;
        kv[key].second = lru.begin();
    }
};
