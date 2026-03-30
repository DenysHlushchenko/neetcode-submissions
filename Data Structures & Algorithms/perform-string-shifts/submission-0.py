class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        res = s
        n = len(s)

        for direction, amount in shift:
            # left shift
            if direction == 0:
                start, end = res[amount:], res[0:amount]
                res = start + end
            else:
                # right shift
                start, end = res[n-amount:], res[0:n-amount]
                res = start + end
        return res


    
        

# s = "abc", shift = [[0,1],[1,2]]


# bca, shift = 2