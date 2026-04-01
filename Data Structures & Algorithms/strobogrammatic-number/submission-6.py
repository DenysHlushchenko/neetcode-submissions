class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        rotated = ''

        for n in reversed(num):
            if n in hashmap:
                rotated += hashmap[n]
            else:
                return False
        return int(num) == int(rotated)