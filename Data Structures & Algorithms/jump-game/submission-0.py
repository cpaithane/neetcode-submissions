class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Recursive solution
        def recurse(i):
            if i == len(nums) - 1:
                return True

            end = min(i + nums[i], len(nums) - 1)

            for j in range(i + 1, end + 1):
                if recurse(j) == True:
                    return True

            return False

        return recurse(0)