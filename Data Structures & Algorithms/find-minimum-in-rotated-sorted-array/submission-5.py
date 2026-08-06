class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        res = nums[0]

        while s <= e:
            mid = (s + ((e - s) // 2))

            # Array between s and e is not rotated.
            # Then nums[s] is the minimum.
            if nums[s] < nums[e]:
                res = min(res, nums[s])
                break

            res = min(res, nums[mid])
            if nums[s] <= nums[mid]:
                s = mid + 1
            else:
                e = mid - 1

        return res
        