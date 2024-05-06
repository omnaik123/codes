#Implement Dijkstras Minimal spanning tree Algorithm.
import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Priority queue to store vertices to be visited next
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we have already found a better path, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph representation (dictionary of dictionaries)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print("Vertex", vertex, ":", distance)
