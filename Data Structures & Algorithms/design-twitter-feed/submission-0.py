class Twitter:

    def __init__(self):
        self.t = 0
        self.tweets = defaultdict(list)    # userID : [(time, tweet)] pairs
        self.follows = defaultdict(set) # follower : set(followees)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.tweets[userId].append((self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        users = self.follows[userId] | {userId} # set of all tweets of followees + user

        for uid in users:
            for t_tweet in self.tweets[uid]:
                heapq.heappush(minHeap, t_tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        return [tweetId for _, tweetId in sorted(minHeap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
