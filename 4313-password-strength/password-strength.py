class Solution:
    def passwordStrength(self, password: str) -> int:
        score=0
        for ch in set(password):
            if 97<=ord(ch)<=122:
                score+=1
            elif 65<=ord(ch)<=90:
                score+=2
            elif 48<=ord(ch)<=57:
                score+=3
            else:
                score+=5
        return score


        