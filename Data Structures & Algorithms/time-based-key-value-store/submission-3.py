class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        i = len(self.store[key]) - 1
        while i >= 0:
            if self.store[key][i][0] <= timestamp:
                return self.store[key][i][1]
            i -=1
        return ""

        
