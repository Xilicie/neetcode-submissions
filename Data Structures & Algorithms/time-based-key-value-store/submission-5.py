class TimeMap:

    def __init__(self):
        self.store: dict(str, list(tuple(int, str))) = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.store[key]) - 1

        if not self.store[key] or self.store[key][0][0] > timestamp: 
            return ""

        index = right

        while left <= right: 
            mid = left + (right - left) // 2
            cur_timestamp = self.store[key][mid]

            if cur_timestamp[0] < timestamp:
                index = mid
                left = mid + 1

            elif cur_timestamp[0] > timestamp:
                right = mid - 1

            elif cur_timestamp[0] == timestamp:
                return cur_timestamp[1]

        return self.store[key][index][1]

