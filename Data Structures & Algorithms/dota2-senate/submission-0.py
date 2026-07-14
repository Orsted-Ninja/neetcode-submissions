class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d=deque(),deque()
        n=len(senate)
        for i,v in enumerate(senate):
            if v=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r1=r.popleft()
            d1=d.popleft()
            if r1<d1:
                r.append(r1+n)
            else:
                d.append(d1+n)
        return 'Radiant' if r else  'Dire'
        
        