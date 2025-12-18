#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#323. Number of Connected Components in an Undirected Graph

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):

            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        seen=set()
        ans =0

        for val in range(n):
            if val not in seen:
                seen.add(val)
                ans +=1
                dfs(val)
        return ans



        
