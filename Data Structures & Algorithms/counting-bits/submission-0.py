class Solution:
    def countBits(self, n: int) -> List[int]:
        res_list = []

        for num in range(0, (n + 1)):
            res = 0
            while num != 0:
                num = num & (num - 1)
                res += 1
            
            res_list.append(res)

        return res_list