from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []

        # User sees their own tweets + tweets of people they follow
        users = self.following[userId] | {userId}

        # Put the latest tweet of each user into heap
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        # Get 10 most recent tweets
        while heap and len(result) < 10:
            time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add the next older tweet from the same user
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)