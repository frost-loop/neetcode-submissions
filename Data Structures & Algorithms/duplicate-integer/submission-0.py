class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for k in nums:
            if k in d:
                d[k]+=1
                if d[k]==2:
                    return True
            else:
                d[k]=1
        return False
        