# Input: s = "loveleetcode"
# Output: 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for k in s:
            d[k]=d.get(k,0)+1
        count=0
        res=[]
        for k,v in d.items():
            if v==1:
                res.append( s.find(k))
        if res:
            return min(res)
        return -1


if __name__=="__main__":
    s='aabb'
    index = Solution().firstUniqChar(s)
    print(f"res:{index}")
