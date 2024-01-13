from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node, order='left'):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft() if order == 'left' else queue.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(sorted(self.graph[node]))

    def dfs(self, start_node):
        visited = set()

        def dfs_util(node):
            nonlocal visited
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                for neighbor in sorted(self.graph[node]):
                    dfs_util(neighbor)

        dfs_util(start_node)

    def is_bipartite(self):
        cycles = self.find_cycles();
        
        for cycle in cycles:
            if (len(cycle) - 1) % 2 == 1:
                return False
            
        return True

    def find_cycles(self):
        visited = set()
        cycles = []

        def dfs_cycle(node, parent, current_path):
            nonlocal visited, cycles

            visited.add(node)
            current_path.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_cycle(neighbor, node, current_path)
                elif neighbor != parent and neighbor in current_path:
                    cycle = current_path[current_path.index(neighbor):] + [neighbor]
                    cycles.append(cycle)

            current_path.pop()

        for node in self.graph:
            if node not in visited:
                dfs_cycle(node, None, [])

        return cycles