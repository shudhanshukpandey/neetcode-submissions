class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


    """
    class Twitter:

    def __init__(self):
        self._tweetfeed = {}
        self._followfeed = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if not self._tweetfeed.get(userId):
            counter = -1
            heap_tweet = [(counter, tweetId)]

            heapq.heapify(heap_tweet)

            self._tweetfeed[userId] = heap_tweet

            return
        root_counter = self._tweedfeed.get(userId)[0][0]
        heapq.heappush(self._tweedfeed.get(userId),(root_counter-1, tweetId))
            return




        

    def getNewsFeed(self, userId: int) -> List[int]:
        


        

    def follow(self, followerId: int, followeeId: int) -> None:

        if folloeeId not in self._followfeed:
            self._followfeed[followeeId] = {followerId}
            return 
        self._followfeed[followeeId].add(followerId)
        return
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self._followfeed.get(followeeId).remove(followerId)
        return
        

    
    """