from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def bfs(self, queue):
        if not queue:
            return

        new_queue = deque()
        while queue:
            node = queue.popleft()
            print(node, end=' ')

            if node in self.adj_list:
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_queue.append(neighbor)

        self.bfs(new_queue)

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

print("Breadth-First Traversal:")
visited = set()
graph.bfs(deque([0]))
