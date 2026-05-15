class HitCounter:

    # Initializes the object of the hit counter system.
    def __init__(self):
        self.hits = collections.deque()


    # Records a hit that happened at timestamp (in seconds). 
    # Several hits may happen at the same timestamp.
    def hit(self, timestamp : int) -> None:
        self.hits.append(timestamp)

    # Returns the number of hits in the past 
    # 5 minutes from timestamp (i.e., the past 300 seconds).
    def getHits(self, timestamp:int) -> int:
        while self.hits:
            difference = timestamp - self.hits[0]
            if difference >= 300:
                self.hits.popleft()
            else:
                break

        return len(self.hits)
