class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == [] :
            return [i for i in range(numCourses)]

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        
        courseStack = []
        inCourseStack = set()
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                if crs not in inCourseStack:
                    inCourseStack.add(crs)
                    courseStack.append(crs)
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            if crs not in inCourseStack:
                inCourseStack.add(crs)
                courseStack.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return courseStack
