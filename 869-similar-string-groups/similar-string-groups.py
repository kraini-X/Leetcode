class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1,s2):
            diff=[]
            n=len(s1)
            for i in range(n):
                if s1[i]!=s2[i]:
                    diff.append(i)
            if len(diff)==0:
                return True
            if len(diff)==2:
                i,j=diff
                return s1[i]==s2[j] and s1[j]==s2[i]
            return False
        
        parent=[i for i in range(len(strs)) ]
        rank=[0]*len(strs)
		
        def find(i):
            if i==parent[i]:
                return i
            parent[i]=find(parent[i])
            return parent[i]
        
        def union(x,y):
            xp=find(x)
            yp=find(y)
            if xp==yp:
                return            
            if rank[xp]>rank[yp]:
                parent[yp]=xp
            elif rank[xp]<rank[yp]:
                parent[xp]=yp
            else:
                parent[yp]=xp
                rank[xp]+=1
        n=len(strs)
        for i in range(n):
            for j in range(i+1,n):
                if isSimilar(strs[i],strs[j]):
                    union(i,j)
        groups=set()
        for i in range(n):
            groups.add(find(i))
        return len(groups)
        