class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop=[]

        for start,end in logs:
            pop.append([start,1])
            pop.append([end,-1])
        
        pop.sort(key=lambda x:(x[0],x[1]))
        population=0
        year=0
        mx=0
        for yr,p in pop:
            population+=p
            if population>mx:
                mx=population
                year=yr
        return year
            

        