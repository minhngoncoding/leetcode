class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)

        taken = set()
        
        print(pre)

        def dfs(course):
            if not pre[course]:
                return True 
            
            # Return False when cycle
            if course in taken: # This course already check beforehand
                return False

            taken.add(course)

            for c in pre[course]:
                if not dfs(c):
                    return False

            pre[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


