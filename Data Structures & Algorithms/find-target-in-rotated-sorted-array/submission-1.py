class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        res = -1

        while s <= e:
            m = s + ((e - s) // 2)

            if nums[m] == target:
                res = m
                break

            # From s to m, elements are in right order
            if nums[s] <= nums[m]:
                # Check if t is falling in between
                if nums[s] <= target and target <= nums[m]:
                    e = m
                else:
                    s = m + 1
            else:
                # Check if t is falling in between
                if nums[m] <= target and target <= nums[e]:
                    s = m
                else:
                    e = m - 1
        
        return res
        