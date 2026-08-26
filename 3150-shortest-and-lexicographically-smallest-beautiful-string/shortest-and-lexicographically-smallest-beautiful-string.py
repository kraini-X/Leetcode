class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        ones=0
        n=len(s)
        minSize=float('inf')
        ans=""
        for r in range(n):
            if s[r]=="1":
                ones+=1
            
            while ones>k:
                
                if s[l]=="1":
                    ones-=1
                l+=1

            while ones==k:
                
                curr=s[l:r+1]
                curr_size=r-l+1

                if curr_size<minSize:
                    minSize=curr_size
                    ans=curr
                elif curr_size==minSize:
                    ans=min(ans,curr)
                
                if s[l]=="1":
                    ones-=1
                l+=1

        return ans

        