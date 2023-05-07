from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # リストの長さの取得し、nに入れる。
        n = len(obstacles)
        answer = [1] * n

        list1 = []

        # インデックス番号と中身を別々に取り出す。
        for i, height in enumerate(obstacles):
            idx = bisect.bisect_right(list1, height)

            if idx == len(list1):
                list1.append(height)
            else:
                list1[idx] = height
            answer[i] = idx + 1

        return answer
