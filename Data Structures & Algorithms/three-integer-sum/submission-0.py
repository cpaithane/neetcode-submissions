class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Sort the array first
        nums.sort()
        print("Sorted array")
        print(nums)
        for i in range(0, len(nums)):
            j = i + 1
            e = len(nums) - 1

            while j < e:
                t = (nums[i] + nums[j]) * (-1)

                if t == nums[e]:
                    tmp_res = []
                    tmp_res.append(nums[i])
                    tmp_res.append(nums[j])
                    tmp_res.append(nums[e])

                    if tmp_res not in res:
                        print("Adding triples to the res")
                        print(i, j, e)
                        print(nums[i], nums[j], nums[e])
                        res.append(tmp_res)
                    
                    j += 1

                elif t < nums[e]:
                    e -= 1
                
                else:
                    j += 1

        return res