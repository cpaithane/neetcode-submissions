class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # First find pile with max_bananas
        max_ban = 0
        for i in range(0, len(piles)):
            max_ban = max(max_ban, piles[i])

        k = 1
        while k < max_ban:
            total = 0
            for i, v in enumerate(piles):
                total += (v // k) + (1 if (v % k != 0) else 0)
                if total > h:
                    break
            
            if total <= h:
                break
            k = k * 2

        e = k
        k = max(1, k // 2)
        while k <= e:
            total = 0
            for i, v in enumerate(piles):
                total += (v // k) + (1 if (v % k != 0) else 0)
                if total > h:
                    break
            if total <= h:
                return k
            k += 1

        return min(k, max_ban)
