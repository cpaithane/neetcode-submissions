from heapq import heapify, heappush, heappop 

class Twitter:

    def __init__(self):
        self.follower_dict = {}
        self.tweets_dict = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets_dict.get(userId, [])
        tweets.append((self.count, tweetId))
        self.tweets_dict[userId] = tweets
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res_tweets = []
        res_tweets.extend(self.tweets_dict.get(userId, []))
        followees = self.follower_dict.get(userId, [])
        for f in followees:
            if f != userId:
                res_tweets.extend(self.tweets_dict[f])

        heap = []
        heapify(heap)

        for count, tweet in res_tweets:
            heappush(heap, (-1 * count, tweet))

        res_list = []
        while len(heap) > 0 and len(res_list) < 10:
            count, tweet = heappop(heap)
            res_list.append(tweet)

        return res_list

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.follower_dict.get(followerId, [])
        if followeeId not in followees:
            followees.append(followeeId)
            self.follower_dict[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.follower_dict.get(followerId, [])
        if followeeId in followees:
            followees.remove(followeeId)
        self.follower_dict[followerId] = followees
