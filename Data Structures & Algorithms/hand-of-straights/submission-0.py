
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Check if total cards can be divided equally
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        # Process cards in sorted order
        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                # Build consecutive groups
                for i in range(groupSize):
                    if count[card + i] < freq:
                        return False

                    count[card + i] -= freq

        return True
