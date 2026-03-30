class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        res = 0

        for n in arr:
            if n + 1 in nums:
                res += 1
        return res
        
# Time O(n)
# Space O(1)