class Leaderboard:

    def __init__(self):
        self.hashmap = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.hashmap[playerId] = self.hashmap.get(playerId, 0) + score

    def top(self, K: int) -> int:
        heap = []
        for score in self.hashmap.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        del self.hashmap[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)