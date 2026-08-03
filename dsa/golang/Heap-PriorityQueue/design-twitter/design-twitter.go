/*
    355. Design Twitter

    Design a simplified version of Twitter where users
    can post tweets, follow/unfollow another user,
    and is able to see the 10 most recent tweets in the
    user's news feed.

    Implement the Twitter class:

    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new
    tweet with ID tweetId by the user userId. Each call to
    this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10
    most recent tweet IDs in the user's news feed.
    Each item in the news feed must be posted by users who
    the user followed or by the user themself. Tweets must
    be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user
    with ID followerId started following the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user
    with ID followerId started unfollowing the user with ID followeeId.

    Example 1:

    Input
    ["Twitter", "postTweet", "getNewsFeed", "follow",
    "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Output
    [null, null, [5], null, null, [6, 5], null, [5]]

    Explanation
    Twitter twitter = new Twitter();
    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1);  // User 1's news feed should
    return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);    // User 1 follows user 2.
    twitter.postTweet(2, 6); // User 2 posts a new tweet
    (id = 6).
    twitter.getNewsFeed(1);  // User 1's news feed should
    return a list with 2 tweet ids -> [6, 5]. Tweet id 6
    should precede tweet id 5 because it is posted after
    tweet id 5.
    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
    twitter.getNewsFeed(1);  // User 1's news feed should
    return a list with 1 tweet id -> [5], since user 1 is
    no longer following user 2.

    Constraints:

    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 104
    All the tweets have unique IDs.
    At most 3 * 104 calls will be made to postTweet,
    getNewsFeed, follow, and unfollow.
    A user cannot follow himself.
*/

import "container/heap"

type Tweet struct {
    id int
    time int
}

type Twitter struct {
    tweets map[int][]Tweet
    follows map[int][]int
    time int
}

func Constructor() Twitter {
    t := Twitter{
        tweets: map[int][]Tweet{}, // <uId : [Tweet]>
        follows: map[int][]int{}, // <uId : [followerId]>
        time: 0,
    }

    return t
}


func (t *Twitter) PostTweet(userId int, tweetId int)  {
    t.time++
    t.tweets[userId] = append(t.tweets[userId], Tweet{tweetId, t.time})
}


func (t *Twitter) GetNewsFeed(userId int) []int {
    maxHeap := &TweetHeap{}
    *maxHeap = append(*maxHeap, t.tweets[userId]...)
    for _, f := range t.follows[userId] {
        *maxHeap = append(*maxHeap, t.tweets[f]...)
    }
    heap.Init(maxHeap)

    res := []int{}
    for maxHeap.Len() > 0 && len(res) < 10  {
        res = append(res, heap.Pop(maxHeap).(Tweet).id)
    }

    return res

}


func (t *Twitter) Follow(followerId int, followeeId int)  {
    if !slices.Contains(t.follows[followerId], followeeId) {
        t.follows[followerId] = append(t.follows[followerId], followeeId)
    }
}


func (t *Twitter) Unfollow(followerId int, followeeId int)  {
    t.follows[followerId] = slices.DeleteFunc(
        t.follows[followerId], func(v int) bool { return v == followeeId })
}


/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */

 // TweetHeap is a max-heap of Tweets.
type TweetHeap []Tweet

func (h TweetHeap) Len() int           { return len(h) }
func (h TweetHeap) Less(i, j int) bool { return h[i].time > h[j].time }
func (h TweetHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *TweetHeap) Push(x interface{}) {
    *h = append(*h, x.(Tweet))
}

func (h *TweetHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}


// SLL

import "container/heap"

type Tweet struct {
    id int
    time int
    next *Tweet
}

type Twitter struct {
    tweets map[int]*Tweet
    follows map[int][]int
    time int
}

func Constructor() Twitter {
    t := Twitter{
        tweets: map[int]*Tweet{}, // <uId : [Tweet]>
        follows: map[int][]int{}, // <uId : [followerId]>
        time: 0,
    }

    return t
}


func (t *Twitter) PostTweet(userId int, tweetId int)  {
    t.time++
    head := t.tweets[userId]
    t.tweets[userId] = &Tweet{
        id: tweetId,
        time: t.time,
        next: head,
    }
}


func (t *Twitter) GetNewsFeed(userId int) []int {
    maxHeap := &TweetHeap{}

    if head := t.tweets[userId]; head != nil {
        *maxHeap = append(*maxHeap, *head)
    }
    for _, f := range t.follows[userId] {
        if head := t.tweets[f]; head != nil {
            *maxHeap = append(*maxHeap, *head)
        }
    }
    heap.Init(maxHeap)

    feed := []int{}
    for maxHeap.Len() > 0 && len(feed) < 10  {
        tw := heap.Pop(maxHeap).(Tweet)
        feed = append(feed, tw.id)
        if tw.next != nil {
            heap.Push(maxHeap, *tw.next)
        }
    }

    return feed

}


func (t *Twitter) Follow(followerId int, followeeId int)  {
    if !slices.Contains(t.follows[followerId], followeeId) {
        t.follows[followerId] = append(t.follows[followerId], followeeId)
    }
}


func (t *Twitter) Unfollow(followerId int, followeeId int)  {
    t.follows[followerId] = slices.DeleteFunc(
        t.follows[followerId], func(v int) bool { return v == followeeId })
}


/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */

 // TweetHeap is a max-heap of Tweets.
type TweetHeap []Tweet

func (h TweetHeap) Len() int           { return len(h) }
func (h TweetHeap) Less(i, j int) bool { return h[i].time > h[j].time }
func (h TweetHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *TweetHeap) Push(x interface{}) {
    *h = append(*h, x.(Tweet))
}

func (h *TweetHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}
