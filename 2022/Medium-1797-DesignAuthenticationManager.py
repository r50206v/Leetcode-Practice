from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.hashmap = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hashmap[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.hashmap.get(tokenId):
            if self.hashmap[tokenId] > currentTime:
                self.hashmap[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for k, v in self.hashmap.items():
            if v > currentTime:
                ans += 1
        return ans


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)