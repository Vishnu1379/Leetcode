class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        counter=collections.Counter(s)
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1