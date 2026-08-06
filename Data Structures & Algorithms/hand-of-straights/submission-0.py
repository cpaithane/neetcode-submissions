class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        nr_groups = len(hand) // groupSize
        hand.sort()
        groups = {}
        for i in range(0, nr_groups):
            groups[i] = []

        def get_suitable_group(num):
            group = -1
            for i in range(0, nr_groups):
                nums = groups[i]

                if len(nums) == groupSize:
                    continue

                if len(nums) == 0 or num - nums[len(nums) - 1] == 1:
                    group = i
                    nums.append(num)
                    break

            return group

        for num in hand:
            # Check suitable group for num
            group = get_suitable_group(num)
            if group == -1:
                return False

        return True