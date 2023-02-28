from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


s = Solution()
numsList = [[5], [2, 5], [-1, 0, 4, 7, 10]]
target = [-5, 0, 0]
for idx, val in enumerate(numsList):
    res = s.search(val, target[idx])
    print(res)
