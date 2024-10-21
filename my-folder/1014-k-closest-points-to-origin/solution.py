class Solution:
    def distance(self, p):
        return p[0]**2 + p[1] **2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance : point
        min_heap = []

        for x,y in points:
            dist = x**2 + y**2
            min_heap.append((dist, x, y))

        heapq.heapify(min_heap)

        result = []

        for i in range(k):
            a,b,c = heapq.heappop(min_heap)
            result.append((b,c))

        return result
