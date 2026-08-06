class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res_list = []
        res = []

        # Sort the array to avoid duplicate combinations
        candidates.sort()

        def combinationSumCore(idx, add, res):
            # Base conditions
            if add == target:
                res_list.append(res.copy())
                return

            if idx >= len(candidates) or add > target:
                return

            # Include the element in the res. and go for next with updated additions
            res.append(candidates[idx])
            combinationSumCore(idx + 1, add + candidates[idx], res)
            res.pop()

            # Skip same candidates.
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            # Go for next element without updated additions.
            combinationSumCore(idx + 1, add, res)

        combinationSumCore(0, 0, res)
        return res_list