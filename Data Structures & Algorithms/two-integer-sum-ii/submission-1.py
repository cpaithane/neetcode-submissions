class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 1
        e = len(numbers)

        tmp_sum = 0

        while s < e:
            tmp_sum = numbers[s-1] + numbers[e-1]
            
            if tmp_sum == target:
                res = []
                res.append(s)
                res.append(e)
                return res

            elif tmp_sum < target:
                s += 1

            else:
                e -= 1
        
        return []
        