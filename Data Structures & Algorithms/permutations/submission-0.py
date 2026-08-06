class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        res = []
        visited = [False] * len(nums)

        def permuteCore(res, visited):
            if len(nums) == len(res):
                res_list.append(res.copy())
                return

            for i in range(0, len(nums)):
                if visited[i] == True:
                    continue

                visited[i] = True
                res.append(nums[i])
                permuteCore(res, visited)
                res.pop()
                visited[i] = False

        permuteCore(res, visited)
        return res_list