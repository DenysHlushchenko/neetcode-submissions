class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = defaultdict(int)

        for i, char in enumerate(keyboard):
            hashmap[char] = i
        
        prev_pos = -1
        res = 0

        for i in range(len(word)):
            cur_pos = hashmap[word[i]]
            if prev_pos == -1:
                res += cur_pos
            else:
                res += abs(prev_pos - cur_pos)
            prev_pos = cur_pos
        return res


# keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
#              i
#                                                   j

# prev_idx = 1

# res = 2 + 1