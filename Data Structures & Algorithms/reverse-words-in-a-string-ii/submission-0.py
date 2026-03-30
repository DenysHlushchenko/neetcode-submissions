class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        n = len(s)
        l, r = 0, 0

        def reverse_word(left, right):
            while left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1

        while r < n:
            while r < n and s[r] != ' ':
                r += 1
            reverse_word(l, r - 1)
            r += 1
            l = r
        

# s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# #                 l
# #                                                             r

# l = 3
# [0:l]

# ["l","u","e"," ","s","k","y"," ","i","s"," ","b","t","h","e"]
# #                             l
# #                                             r

