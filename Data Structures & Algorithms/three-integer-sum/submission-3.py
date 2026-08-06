class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Sort the array first
        nums.sort()

        for i in range(0, len(nums)):

            # As array is sorted, no possibility of having negative num.
            if nums[i] > 0:
                break

            # If prev num is same as that of cur, then the pair is already
            # considered
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            e = len(nums) - 1

            while j < e:
                t = (nums[i] + nums[j]) * (-1)

                if t == nums[e]:
                    tmp_res = []
                    tmp_res.append(nums[i])
                    tmp_res.append(nums[j])
                    tmp_res.append(nums[e])

                    res.append(tmp_res)
                    
                    j += 1
                    e -= 1
                    while nums[j] == nums[j-1] and j < e:
                        j += 1
                    

                elif t < nums[e]:
                    e -= 1
                
                else:
                    j += 1

        return res