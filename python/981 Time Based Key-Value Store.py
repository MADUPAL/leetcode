class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        if not values:
            return ""
        
        l, r = 0, len(values)-1
        result = ""
        while l <= r:
            m = (l+r)//2

            if values[m][1] <= timestamp:
                l = m+1
                result = values[m][0]
            elif values[m][1] > timestamp:
                r = m-1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)