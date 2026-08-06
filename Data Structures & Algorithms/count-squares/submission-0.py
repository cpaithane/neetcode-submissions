class CountSquares:

    def __init__(self):
        self.pts_count = {}
        self.pts = []

    def add(self, point: List[int]) -> None:
        count = self.pts_count.get((point[0], point[1]), 0)
        self.pts_count[(point[0], point[1])] = count + 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        qx = point[0]
        qy = point[1]
        res = 0

        for p in self.pts:
            x = p[0]
            y = p[1]

            # Check diagonal. Difference between diagonal and query point
            # must be equal. Or x and y coordinates must not match with query
            # point.
            if (abs(qx - x) != abs(qy - y)) or x == qx or y == qy:
                continue
            
            # Diagonal is found. Let's check for two adjacent points.
            # As there can be multiple entries for the same point, let's multiply
            res += self.pts_count.get((qx, y), 0) * self.pts_count.get((x, qy), 0)

        return res