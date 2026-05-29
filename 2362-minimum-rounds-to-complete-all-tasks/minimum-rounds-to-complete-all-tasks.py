class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        rounds=0
        freq=Counter(tasks)
        for val in freq.values():
            if val==3:
                rounds+=1
            elif val==2:
                rounds+=1
            elif val>3:
                if val%3==0:
                    rounds+=val//3
                elif val%3==2:
                    rounds+=val//3+1
                elif val%3==1:
                    rounds+=val//3+1
            else:
                return -1
        return rounds