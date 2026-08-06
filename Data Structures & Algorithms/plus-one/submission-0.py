class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits) - 1
        carry = 0
        total = 0
        res_list = []

        for i in range(size, -1, -1):
            if i == len(digits) - 1:
                total = carry + digits[i] + 1
            else:
                total = carry + digits[i]

            carry = total // 10
            res_list.append(total % 10)

        print(total)
        if total >= 10:
            res_list.append(total // 10)

        print(res_list)
        tmp_list = []
        for num in reversed(res_list):
            tmp_list.append(num)

        return tmp_list