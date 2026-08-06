class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res_list = []
        res = []

        #
        # Simple steps to remember for backtracking problems.
        #
        def combinationSumCore(res, idx, add, target):
            # Define base conditions to break recursion
            # Valid condition
            if add == target:
                res_list.append(res.copy())
                return

            # Define base conditions to break recursion
            # Invalid condition
            if idx >= len(nums) or add > target:
                return

            # Try choosing the element
            res.append(nums[idx])
            # Try to solve the problem
            combinationSumCore(res, idx, add + nums[idx], target)
            # If problem is not solved, remove the element from result
            res.pop()
            # Go for next element to choose
            combinationSumCore(res, idx + 1, add, target)

        combinationSumCore(res, 0, 0, target)
        return res_list