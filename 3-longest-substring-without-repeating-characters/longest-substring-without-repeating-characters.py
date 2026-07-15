class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        n=len(s)
        l=0
        length=0
        for r in range(l,n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            length=max(length,r-l+1)
        return length

        