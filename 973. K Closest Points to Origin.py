import heapq


def kClosest(points, k):
    full_data = []
    for x, y in points:
        distance = x ** 2 + y ** 2
        full_data.append([distance, x, y])
    heapq.heapify(full_data)
    res = []
    while k > 0:
        distance, x, y = heapq.heappop(full_data)
        res.append([x,y])
        k -= 1
    return res




