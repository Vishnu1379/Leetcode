class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        c=sum(nums)
        d=""
        for i in nums:
            d+=str(i)
        a=0
        for i in d:
            a+=int(i)
        return (abs(a-c))
        
        