class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        q=deque()
        q.append(beginWord)
        level=0
        wordlist=set(wordList)
        visited=set()
        visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                word=q.popleft()

                if word==endWord:
                    return level+1
                
                for i in range(len(word)):
                    for j in range(26):
                        ch=chr((ord('a') + j))
                        new=word[:i]+ch+word[i+1:]

                        if new in wordlist and new not in visited:
                            visited.add(new)
                            q.append(new)
            level+=1
        return 0