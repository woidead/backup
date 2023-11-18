class Solution(object):
    def maximumWealth(self, accounts):
        v =[]
        for s in accounts:
                x = sum(s)
                v.append(x)
        a = max(v)
        return a