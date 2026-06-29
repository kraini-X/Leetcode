class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        n=len(patterns)
        for p in patterns:
            if p in word:
                count+=1
        return count
            


        