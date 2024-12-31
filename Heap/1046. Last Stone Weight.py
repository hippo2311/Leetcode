import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_larg = heapq.heappop(stones)

            if largest != next_larg:
                heapq.heappush(stones, largest - next_larg)
        return -stones[0] if stones else 0
# Time O(n log n)
# Space O(n)