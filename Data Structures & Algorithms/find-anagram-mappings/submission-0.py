class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums2):
            hashmap[n] = i

        mapping = [0] * len(nums1)
        for i, n in enumerate(nums1):
            mapping[i] = hashmap.get(n)
        return mapping