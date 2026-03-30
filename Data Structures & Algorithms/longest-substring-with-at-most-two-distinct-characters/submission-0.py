class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        longest = -1
        l, r = 0, 0

        while r < len(s):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1

            while len(freq) > 2:
                left_char = s[l]
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    del freq[left_char]
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest
        

# s = "eceba"
#      l
#      r

# hashmap = {
    # e: 1
# }