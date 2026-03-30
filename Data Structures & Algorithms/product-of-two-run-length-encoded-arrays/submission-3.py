class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        prodNums = []
        i, j = 0, 0
        
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product_val = val1 * val2
            product_freq = min(freq1, freq2)

            encoded1[i][1] -= product_freq
            encoded2[j][1] -= product_freq

            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            
            if not prodNums or prodNums[-1][0] != product_val:
                prodNums.append([product_val, product_freq])
            else:
                prodNums[-1][1] += product_freq
        return prodNums

# encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]

# [2, 0]
# [3, 2]

# product_freq = 1

# product_encoded = [[2, 3], [6, 1]]