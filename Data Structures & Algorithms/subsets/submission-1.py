class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        sub_res = []

        def backtrack(i):
            if i >= len(nums):
                res_list.append(sub_res.copy())
                return

            sub_res.append(nums[i])
            backtrack(i + 1)
            sub_res.pop()
            backtrack(i + 1)

        backtrack(0)
        return res_list