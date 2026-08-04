class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import deque
        n=len(routes)
        BusMap=defaultdict(list)

        for bus, route in enumerate(routes):

            for stops in route:
                BusMap[stops].append(bus)
        
        
        visitedBus=set()
        
        q=deque()

        for buses in BusMap[source]:
            q.append(buses)
            visitedBus.add(buses)
        level=1
        if source==target:
            return 0
        while q:
            for _ in range(len(q)):
                idx=q.popleft()

                for stops in routes[idx]:
                    if stops==target:
                        return level

                    for buses in BusMap[stops]:
                        if buses not in visitedBus:
                            visitedBus.add(buses)
                            q.append(buses)
            level+=1
        return -1