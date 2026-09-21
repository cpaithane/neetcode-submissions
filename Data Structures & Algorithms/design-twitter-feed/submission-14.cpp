class Twitter {
private:
    int count;
    unordered_map<int, vector<pair<int, int>>> tweets;
    unordered_map<int, unordered_set<int>> followers;

public:
    Twitter() {
        count = 0;    
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({this->count, tweetId});
        this->count++;
    }
    
    vector<int> getNewsFeed(int userId) {
        auto &news = tweets[userId];
        auto &followers_id = followers[userId];
        priority_queue<pair<int, int>> heap;
        vector<int> res_list;

        for (auto &p : news) {
            heap.push(p);
        }

        if (followers.find(userId) != followers.end()) {
            for (int f : followers[userId]) {
                for (auto &p : tweets[f]) {
                    heap.push(p);
                }
            }
        }

        while (!heap.empty() && res_list.size() < 10) {
            auto &[count, tweetId] = heap.top();
            res_list.push_back(tweetId);
            heap.pop();
        }

        return res_list;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }
        followers[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followers.find(followerId) != followers.end()) {
            followers[followerId].erase(followeeId);
        }
    }
};
