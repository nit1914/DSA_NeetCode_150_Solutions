from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        # Convert list to set for fast searching
        wordSet = set(wordList)

        # If endWord is not present, transformation is impossible
        if endWord not in wordSet:
            return 0

        # Queue stores: (current_word, number_of_words)
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            # We reached the destination
            if word == endWord:
                return steps

            # Change each character one by one
            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + ch + word[i + 1:]

                    # If new word is valid and not visited
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))

                        # Remove to prevent visiting again
                        wordSet.remove(newWord)

        # No transformation possible
        return 0