class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        odd_cnt, even_cnt = 0, len(s)
        for val in freq.values():
            if val % 2 == 1:
                odd_cnt = max(odd_cnt, val)
            else:
                even_cnt = min(even_cnt, val)
        return odd_cnt - even_cnt

