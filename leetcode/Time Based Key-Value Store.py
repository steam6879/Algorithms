from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.m[key]

        if not values:
            return ''

        pl, pr = 0, len(values) - 1

        while pl <= pr:
            pc = pl + (pr - pl) // 2
            if values[pc][0] == timestamp:
                return values[pc][1]

            elif values[pc][0] < timestamp:
                pl = pc + 1
            else:
                pr = pc - 1

        if pr >= 0:
            return values[pr][1]
        else:
            return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)