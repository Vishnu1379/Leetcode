class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l,u,bound=0,1,(0,1)
        setused={s[0]}
        while u<len(s):
            if s[u] in setused:
                setused.remove(s[l])
                l+=1 
            else:
                setused.add(s[u])
                u+=1 
            if u-l>bound[1]-bound[0]:
                bound=(l,u)
        return bound[1]-bound[0]
        