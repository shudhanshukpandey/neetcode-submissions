class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        feq = Counter(tasks)
        heap_q = [-val for val in feq.values()]
        heapq.heapify(heap_q)
        
        dq = deque()
        time = 0
        
        while heap_q or dq:
            time += 1
            if not heap_q:
                time = dq[0][1]
            else:
                cnt = 1 + heapq.heappop(heap_q)
                if cnt:
                    dq.append([cnt, time + n])
            
            if dq and dq[0][1] == time:
                heapq.heappush(heap_q, dq.popleft()[0])
                
        return time