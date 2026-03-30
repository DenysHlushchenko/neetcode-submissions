class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalidNums = {2, 3, 4, 5, 7}
        original = n
        isInvalid = False

        rotated = 0
        while n > 0:
            right_num = n % 10
            if right_num in invalidNums:
                return False
            elif right_num == 6:
                rotated = rotated * 10 + 9
            elif right_num == 9:
                rotated = rotated * 10 + 6
            else:
                rotated = rotated * 10 + right_num
            n //= 10
        return original != rotated