class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            # Check if the v is at its right pos
            if i == (v - 1):
                continue

            # v is not at right position
            # Check if v and num at right pos are equal
            # If they are equal, then return nums[i]
            # Else, swap.
            if v == nums[nums[i] - 1]:
                return v

            print(i, nums)
            tmp = v
            print(tmp, nums[i], nums[v - 1])

            nums[i] = nums[v - 1]
            print(tmp, nums[i], nums[v - 1])

            nums[v - 1] = tmp
            print(tmp, nums[i], nums[nums[i] - 1])
            print(i, nums)

        return -1
        