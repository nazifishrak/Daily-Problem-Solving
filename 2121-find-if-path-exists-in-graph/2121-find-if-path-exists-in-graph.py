class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        # Create the graph
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Set to keep track of visited nodes
        visited = set()
        
        # Define the recursive DFS function
        def dfs(node):
            # If we've reached the destination, we're done
            if node == destination:
                return True
            
            # Mark the current node as visited
            visited.add(node)
            
            # Check all neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            # If we get here, this path didn't work
            return False
        
        # Start the DFS from the source
        return dfs(source)