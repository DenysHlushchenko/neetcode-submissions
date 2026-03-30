class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = defaultdict(int)

        for i, char in enumerate(keyboard):
            hashmap[char] = i
        
        prev_pos = hashmap[word[0]]
        res = prev_pos

        for i in range(1, len(word)):
            cur_pos = hashmap[word[i]]
            res += abs(prev_pos - cur_pos)
            prev_pos = cur_pos
        return res

# Time O(n)
# Space O(1)