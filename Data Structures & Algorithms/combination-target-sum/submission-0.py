class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res_list = []
        res = []

        def combinationSumCore(res, idx, add, target):
            if add == target:
                res_list.append(res.copy())
                return

            if idx >= len(nums) or add > target:
                return

            res.append(nums[idx])
            combinationSumCore(res, idx, add + nums[idx], target)
            res.pop()
            combinationSumCore(res, idx + 1, add, target)

        combinationSumCore(res, 0, 0, target)
        return res_list