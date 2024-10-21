# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjlist = defaultdict(list)

        
        dist = [float("inf")] * (n)

        dist[src ] = 0

        if k >= n -1:
            k = n-2
        
        for i in range(k + 1):
            cur = dist[:]

            for u,v,w in flights:
                cur[v] = min(cur[v],dist[u] + w)
        
            # print(cur,"hi")
            dist = cur[:]
        if dist[dst] == float("inf"):
            return -1
        return dist[dst]