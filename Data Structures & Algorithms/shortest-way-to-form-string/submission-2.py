class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t_idx, cnt = 0, 0

        while t_idx < len(target):
            start_t_idx = t_idx
            for s_idx in range(len(source)):
                if t_idx < len(target) and source[s_idx] == target[t_idx]:
                    t_idx += 1
            
            if start_t_idx == t_idx:
                return -1
            cnt += 1
        return cnt
            

        

# # Example 1:
# source = "abc", target = "acdbc"


# # Example 2:
# cnt = 0
# source = "xyz"
# #         i

# target = "xzyxz"
# #         j

