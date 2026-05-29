class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        seeds = list(zip(plantTime, growTime))
        seeds.sort(key=lambda x: -x[1])   

        prevPlant=0
        maxDays=0

        for pt,gt in seeds:
            days=prevPlant+pt+gt
            maxDays=max(days,maxDays)
            prevPlant+=pt
        return maxDays
        