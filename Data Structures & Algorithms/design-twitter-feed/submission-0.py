class Twitter:

    def __init__(self):
        self.followingGraph = collections.defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweet_user, tweet_id = self.tweets[i]
            if tweet_user == userId or tweet_user in self.followingGraph[userId]:
                result.append(tweet_id)
            if len(result) >= 10:
                break
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingGraph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followingGraph and followeeId in self.followingGraph[followerId]:
            self.followingGraph[followerId].remove(followeeId)
