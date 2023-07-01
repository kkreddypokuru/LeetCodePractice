class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        start=0
        end=len(s)
        endt=len(t)
        sd={}
        td={}
        if end==endt:
            while start<end:
                sd[s[start]] = sd.get(s[start],0)+1
                td[t[start]] = td.get(t[start],0)+1
                start = start +1
            if sd==td:
                return "true"
            return "false"

        return "false"


s="rat"
t="cat"
sol = Solution()
res=sol.isAnagram(s, t)
print(res)