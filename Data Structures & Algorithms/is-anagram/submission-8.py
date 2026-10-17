class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x,y={},{}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in x:
                x[i]=x[i]+1
            else:
                x[i]=1
        for i in t:
            if i in y:
                y[i]+=1
            else:
                y[i]=1
        return x==y