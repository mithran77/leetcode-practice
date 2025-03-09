# 355. Design Twitter

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
# and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
# Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.


# from heapq import heappop, heappush
# from abc import ABC, abstractmethod
# import time

# # Singly linked list

# class IUser(ABC):
#     @abstractmethod
#     def get_followed_users(self):
#         pass

#     @abstractmethod
#     def get_tweets_head(self):
#         pass

#     @abstractmethod
#     def follow(self, user_id):
#         pass

#     @abstractmethod
#     def unfollow(self, user_id):
#         pass

# class IPostable(ABC):
#     @abstractmethod
#     def post(self, tweet_id):
#         pass

# class ITweet(ABC):
#     @abstractmethod
#     def get_created_at(self):
#         pass

# class Tweet(ITweet):
#     def __init__(self, tweet_id): # O(1)
#         self.id = tweet_id
#         self._created_at = time.time()
#         self.next = None

#     def get_created_at(self):  # O(1)
#         return self._created_at

# class SLLUser(IUser, IPostable):
#     def __init__(self, user_id): # O(1)
#         self.id = user_id
#         self.following = set([user_id])
#         self.tweets_head = None

#     def get_followed_users(self): # O(1)
#         return self.following

#     def get_tweets_head(self):
#         return self.tweets_head

#     def follow(self, user_id): # O(1)
#         if self.id == user_id:
#             raise ValueError("User should not follow itself")
#         self.following.add(user_id)

#     def unfollow(self, user_id): # O(1)
#         if self.id == user_id:
#             raise ValueError("User cannot unfollow itself")
#         self.following.discard(user_id)

#     def post(self, tweet_id): # O(1)
#         tweet = Tweet(tweet_id)
#         tweet.next = self.tweets_head
#         self.tweets_head = tweet

# class Twitter:

#     # Singleton to be used here
#     def __init__(self): # O(1)
#         self.user_map = {} # userId -> user Object
#         self.feed_size = 10

#     def postTweet(self, user_id, tweet_id): # O(1)
#         if user_id not in self.user_map:
#             self.user_map[user_id] = SLLUser(user_id) # O(1)
#         self.user_map[user_id].post(tweet_id) # O(1)

#     def getNewsFeed(self, user_id): # O(n log n)
#         feed = []
#         if user_id not in self.user_map: # early return
#             return feed

#         users = self.user_map[user_id].get_followed_users()
#         max_heap = []

#         # Add only the tweet head of each followed user(n) to the heap
#         for user in users: # O(n log n)
#             tweet = self.user_map[user].get_tweets_head()
#             if tweet:
#                 heappush(max_heap, (-tweet.get_created_at(), tweet))  # O(log n)

#         # Fetch up to 10 tweets from the heap
#         # merge n sorted Lists
#         while max_heap and len(feed) < self.feed_size: # O(10 log n)
#             _, tweet = heappop(max_heap)  # O(log n)
#             feed.append(tweet.id)
#             if tweet.next:
#                 heappush(max_heap, (-tweet.next.get_created_at(), tweet.next))  # O(log n)

#         return feed

#     def follow(self, follower_id, followee_id): # O(1)
#         if follower_id not in self.user_map:
#             self.user_map[follower_id] = SLLUser(follower_id) # O(1)
#         if followee_id not in self.user_map:
#             self.user_map[followee_id] = SLLUser(followee_id) # O(1)
#         self.user_map[follower_id].follow(followee_id) # O(1)

#     def unfollow(self, follower_id, followee_id): # O(1)
#         if follower_id in self.user_map:
#             self.user_map[follower_id].unfollow(followee_id) # O(1)


from collections import defaultdict, deque
from typing import List
import heapq

# class Twitter:
#     def __init__(self):
#         self.tweets = defaultdict(deque)  # userId -> user's tweets
#         self.followees = defaultdict(set)  # userId -> user's followees
#         self.globalOrder = 0  # Global timestamp for tweet order

#     class Tweet:
#         def __init__(self, tweet_id, order):
#             self.id = tweet_id
#             self.order = order

#     class Feed:
#         def __init__(self, tweets):
#             self.iterator = iter(tweets)
#             self.curr = next(self.iterator, None)

#         def advance(self):
#             self.curr = next(self.iterator, None)
#             return self.curr is not None

#     def postTweet(self, userId, tweetId):
#         self.tweets[userId].appendleft(self.Tweet(tweetId, self.globalOrder))
#         self.globalOrder += 1

#     def getNewsFeed(self, userId):
#         max_heap = []

#         # Add user's own tweets to the feed
#         if self.tweets[userId]:
#             heapq.heappush(max_heap, (-self.tweets[userId][0].order, self.Feed(self.tweets[userId])))

#         # Add followees' tweets to the feed
#         for followeeId in self.followees[userId]:
#             if self.tweets[followeeId]:
#                 heapq.heappush(max_heap, (-self.tweets[followeeId][0].order, self.Feed(self.tweets[followeeId])))

#         feeds = []
#         while max_heap and len(feeds) < 10:
#             _, feed = heapq.heappop(max_heap)
#             feeds.append(feed.curr.id)
#             if feed.advance():
#                 heapq.heappush(max_heap, (-feed.curr.order, feed))

#         return feeds

#     def follow(self, followerId, followeeId):
#         if followerId != followeeId:
#             self.followees[followerId].add(followeeId)

#     def unfollow(self, followerId, followeeId):
#         self.followees[followerId].discard(followeeId)

# # Example Usage
# twitter = Twitter()
# twitter.postTweet(1, 101)
# twitter.postTweet(1, 102)
# twitter.follow(1, 2)
# twitter.postTweet(2, 201)
# twitter.postTweet(2, 202)
# print(twitter.getNewsFeed(1))  # Most recent tweets from user 1 and 2
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))  # Only user 1's tweets


FEED_SIZE = 10

class Tweet: # SLL
    def __init__(self, id, ts, next=None):
        self.id = id
        self.timestamp = ts
        self.next = next

class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # <uid: [follow_id]>
        self.tweets = defaultdict(lambda: None) # <uid: Tweet>
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        head = self.tweets[userId]
        self.tweets[userId] = Tweet(tweetId, self.timestamp, head)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        tweet_heap = []
        # Add tweets sorted by timestamp to max heap
        followers = list(self.following[userId]) + [userId]
        for follower in followers:
            head = self.tweets[follower]
            if head is not None:
                heapq.heappush(tweet_heap, (-head.timestamp, head))

        # Generate feed
        while tweet_heap and len(feed) < FEED_SIZE:
            _, tweet = heapq.heappop(tweet_heap)
            feed.append(tweet.id)
            tweet = tweet.next
            if tweet is not None:
                heapq.heappush(tweet_heap, (-tweet.timestamp, tweet))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
