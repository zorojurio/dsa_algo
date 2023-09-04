from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        points.sort(key=lambda x: x[1])
        print(points)
        i = 0
        for j in range(1, len(points)):
            if points[j][0] <= points[i][1] <= points[j][1]:
                print(points[i])
            else:
                count += 1
                i = j
        return count


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
sol = Solution()
print(sol.findMinArrowShots(points))
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
sol = Solution()
print(sol.findMinArrowShots(points))
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
sol = Solution()
print(sol.findMinArrowShots(points))
