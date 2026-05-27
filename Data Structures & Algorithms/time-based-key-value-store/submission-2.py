class TimeMap:

    def __init__(self):
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        else:
            i = len(self.timeMap[key]) - 1
            while i >= 0:
                if self.timeMap[key][i][0] <= timestamp:
                    return self.timeMap[key][i][1]
                else:
                    i -= 1
            return ""



        
