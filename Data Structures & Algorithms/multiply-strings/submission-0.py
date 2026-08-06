class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tmp_list = []

        def do_mult(digit, num1):
            res = 0
            carry = 0
            local_mult = 0
            mult = 1
            for n in range(len(num1) - 1, -1, -1):
                local_mult = carry + (digit * int(num1[n]))
                carry = local_mult // 10
                local_mult = local_mult % 10
                res += local_mult * mult
                mult = mult * 10

            res = res + carry * mult
            return res

        mult = 1
        for i in range(len(num2) - 1, -1, -1):
            digit = int(num2[i])
            local_mult = do_mult(digit, num1) * mult
            tmp_list.append(local_mult)
            mult = mult * 10

        print("tmp_list = ", tmp_list)

        total = 0
        for tmp in tmp_list:
            total += tmp

        print("total = ", total)

        if total == 0:
            return "0"

        res = ""
        while total != 0:
            digit = total % 10
            total = total // 10
            res = str(digit) + res

        return res