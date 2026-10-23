class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use binary serch
        # start with beg and end
        # if the two numbers at beg and end is greater than target, we need a smaller number so decrease end pointer
        # if the two numbers at beg and end is less than target, we need a greater number so incerase start ppointer
        s = 0
        e = len(numbers) - 1

        # cannot be equal
        while s < e:
            summation = numbers[s] + numbers[e]
            if summation == target:
                return [s + 1, e + 1]
            elif summation > target:
                e -= 1
            else:
                s += 1



        return -1