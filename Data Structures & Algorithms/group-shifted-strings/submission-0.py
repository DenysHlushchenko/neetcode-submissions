class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def get_key(s: str) -> str:
            if len(s) == 1:
                return '#'
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(chr(diff + ord('a')))
            return ''.join(key)
        
        groups = defaultdict(list)
        for string in strings:
            key = get_key(string)
            groups[key].append(string)
        return list(groups.values())

# Time O(n*k)
# Space O(1)