class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict(Counter(tasks))
        heap = [-v for v in freq.values()]
        heapq.heapify(heap)
        queue = deque()
        result = 0

        while heap or queue:
            result += 1
            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                if count != 0:
                    queue.append((count, result + n))
            if queue:
                if queue[0][1] == result:
                    heapq.heappush(heap, -queue.popleft()[0])

        return result