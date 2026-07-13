class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import defaultdict,deque
        visited=defaultdict(bool)

        visited[startGene]=True
        q = deque([startGene])
        choices=["A","C","G","T"]
        level=0
        while q:
            for _ in range(len(q)):
                gene=q.popleft()

                if gene==endGene:
                    return level
                
                for i in range(len(gene)):
                    for ch in choices:
                        newGene=gene[0:i]+ch+gene[i+1:]
                        if newGene in bank and not visited[newGene]:
                            visited[newGene]=True
                            q.append(newGene)
            level+=1
        return -1

        