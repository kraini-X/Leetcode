class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        q=deque()
        q.append(beginWord)
        level=1
        wordlist=set(wordList)
        visited=set()
        visited.add(beginWord)

        while q:
            for _ in range(len(q)):
                word=q.popleft()

                if word==endWord:
                    return level
                
                for i in range(len(word)):
                    for j in range(97,123):
                        newWord=word[0:i]+chr(j)+word[i+1:]
                        if newWord in wordlist and newWord not in visited:
                            visited.add(newWord)
                            q.append(newWord)
            level+=1
        return 0


        