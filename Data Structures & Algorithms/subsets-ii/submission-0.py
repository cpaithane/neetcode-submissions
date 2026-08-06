class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        res = []

        nums.sort()

        def recurse(idx, res):
            if idx == len(nums):
                res_list.append(res.copy())
                return

            res.append(nums[idx])
            recurse(idx + 1, res)
            res.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            recurse(idx + 1, res)

        recurse(0, res)
        return res_list