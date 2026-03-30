class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = 0
        unique = set(arr)
        for x in arr:
            if x + 1 in unique:
                count += 1
        
        return count