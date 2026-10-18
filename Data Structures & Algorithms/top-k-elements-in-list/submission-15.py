class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        f=[[]for i in range(len(nums)+1)]#[[],[],[],[],[],[]]
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1 #s={1:1;2:2;3:3}
        for n,c in s.items():
            f[c].append(n)
        res=[]
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res
        