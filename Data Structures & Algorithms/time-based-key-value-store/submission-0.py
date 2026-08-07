class TimeMap:

    def __init__(self):
        # key -> list of [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        # Timestamps are strictly increasing,
        # so simply append.
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1
        result = ""

        # Find the rightmost timestamp <= timestamp
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result 
