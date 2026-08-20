class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # closest_point = {}
        heap = []
        heapq.heapify(heap)
        for point in points:
            closest_point = []

            min_dist = round(((point[0]-0)**2 + (point[1]-0)**2)**.5,2)

            # closest_point[min_dist] =closest_point.get(min_dist,[])+[point]
            closest_point = [min_dist, point]
            heapq.heappush(heap, closest_point)

        # sorted_val = dict(sorted(closest_point.items(), key = lambda x: x[0]))
        # print(heap)
        return_data = []
        while k:

            # return_data = [list(i[1]) for i in heap][:k]
            return_data.append(heapq.heappop(heap)[1])
            k-=1
        return return_data

        # 18, 26, 20
        