class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_of_squares(num):
            res = 0

            while num != 0:
                digit = num % 10
                digit = digit ** 2
                res += digit

                num = num // 10

            return res

        visited = set()

        while n not in visited:
            visited.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True

        return False

        slow = n
        fast = sum_of_squares(n)
        while slow != fast:
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)
            slow = sum_of_squares(slow)

        if fast == 1:
            return True
        else:
            return False