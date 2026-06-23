class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            i = len(self.dic[key]) - 1
            while i >= 0:
                if timestamp >= self.dic[key][i][0]:
                    return self.dic[key][i][1]
                i -= 1
        return ""
        
