from collections import deque, defaultdict

class Twitter(object):

    def __init__(self):
        self.feeds = defaultdict(deque)
        #
        # { userId: { (timestamp, userId, tweetId), (timestamp, userId, tweetId), ... },
        #   userId: { (timestamp, userId, tweetId), (timestamp, userId, tweetId), ... }
        # }
        #
        self.followers = defaultdict(set)
        self.timestamp = 0


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.timestamp += 1
        tweet = (self.timestamp, userId, tweetId)
        self.feeds[userId].appendleft(tweet)
        for follower in self.followers[userId]:
            self.feeds[follower].appendleft(tweet)


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        return [self.feeds[userId][i][2] for i in \
                range(0, min(10, len(self.feeds[userId])))]


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.followers[followeeId]:
            self.followers[followeeId].add(followerId)
            tweets = [tweet for tweet in self.feeds[followerId]]
            # also add tweets from followeeId
            for tweet in self.feeds[followeeId]:
                if tweet[1] == followeeId:
                    tweets.append(tweet)
            # sort tweets by timestamp in descending order
            self.feeds[followerId] = deque(
                    sorted(tweets, key = lambda x: x[0],
                        reverse = True))


    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
            # remove followeeId's tweets from followerId's feed
            self.feeds[followerId] = deque(
                    tweet for tweet in self.feeds[followerId] \
                            if tweet[1] != followeeId)


vectors = [
        'Twitter', None, None, None,
        'postTweet', 1, 5, None,
        'getNewsFeed', 1, None, [5],
        'follow', 1, 2, None,
        'postTweet', 2, 6, None,
        'getNewsFeed', 1, None, [6,5],
        'unfollow', 1, 2, None,
        'getNewsFeed', 1, None, [5],
        'Twitter', None, None, None,
        'postTweet', 1, 1, None,
        'getNewsFeed', 1, None, [1],
        'follow', 2, 1, None,
        'getNewsFeed', 2, None, [1],
        'unfollow', 2, 1, None,
        'getNewsFeed', 2, None, [],
        'Twitter', None, None, None,
        'postTweet', [1, 2], [4, 5], None,
        'unfollow', 1, 2, None,
        'getNewsFeed', 1, None, [4],
        'Twitter', None, None, None,
        'postTweet', 2, 5, None,
        'follow', [1,1], [1,2], None,
        'getNewsFeed', 1, None, [5],
        'Twitter', None, None, None,
        'postTweet', [2,1,1,2,2,1,2,2,1,1], [5,3,101,13,10,2,94,505,333,22], None,
        'getNewsFeed', 2, None, [505,94,10,13,5],
        'follow', 2, 1, None,
        'getNewsFeed', 2, None, [22,333,505,94,2,10,13,101,3,5],
        'Twitter', None, None, None,
        'postTweet', [1,1,1,1,1,1,1,1,1,1,1], [5,3,101,13,10,2,94,505,333,22,11], None,
        'getNewsFeed', 1, None, [11,22,333,505,94,2,10,13,101,3],
        'Twitter', None, None, None,
        'postTweet', [1,2,1,2,2,1,1,2,1,2,1,1,2,1,2,1,2,1,2,2,1,2], [5,3,101,13,10,2,94,505,333,22,11,205,203,201,213,200,202,204,208,233,222,211], None,
        'getNewsFeed', 1, None, [222,204,200,201,205,11,333,94,2,101],
        'follow', 1, 2, None,
        'getNewsFeed', 1, None, [211,222,233,208,204,202,200,213,201,203],
        'unfollow', 1, 2, None,
        'getNewsFeed', 1, None, [222,204,200,201,205,11,333,94,2,101]
        ]

tw = None
for i in range(0, len(vectors), 4):
    action = vectors[i]
    param1 = vectors[i + 1]
    param2 = vectors[i + 2]
    expected = vectors[i + 3]
    returned = None

    if tw is not None and action == 'Twitter':
        print('')
    if type(param1) == list and type(param2) == type(param2):
        for p1, p2 in zip(param1, param2):
            print(f'{action}: param1 = {p1}, param2 = {p2}, expected = {expected}')
    else:
        print(f'{action}: param1 = {param1}, param2 = {param2}, expected = {expected}')

    if action == 'Twitter':
        tw = Twitter()
    elif action == 'postTweet':
        assert type(param1) == type(param2)
        if type(param1) == int:
            param1 = [param1]
            param2 = [param2]
        for p1, p2 in zip(param1, param2):
            tw.postTweet(p1, p2)
    elif action == 'getNewsFeed':
        returned = tw.getNewsFeed(param1)
    elif action == 'follow':
        assert type(param1) == type(param2)
        if type(param1) == int:
            param1 = [param1]
            param2 = [param2]
        for p1, p2 in zip(param1, param2):
            tw.follow(p1, p2)
    elif action == 'unfollow':
        tw.unfollow(param1, param2)
    assert expected == returned, f'expected {expected}, returned {returned}!'
