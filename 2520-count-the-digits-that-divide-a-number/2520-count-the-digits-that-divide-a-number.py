class Solution:
    def countDigits(self, num: int) -> int:
        d=str(num)
        c=0
        for i in d:
            if int(d)%int(i)==0:
                c+=1
        return c