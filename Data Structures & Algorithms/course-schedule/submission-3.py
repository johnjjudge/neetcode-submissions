class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if prerequisites == [] :
            return True

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for courseAndPreReq in prerequisites:
            course = courseAndPreReq[0]
            preReq = courseAndPreReq[1]
            preMap[course].append(preReq)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            


