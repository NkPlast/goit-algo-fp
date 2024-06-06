import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Тому що граф незважений

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Вузли можна розглянути більше одного разу, тому ми перевіряємо
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Тільки тоді розглядаємо цей новий шлях, якщо він коротший
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

# Тестування алгоритму
graph = Graph(6)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(0, 3, 2)
graph.add_edge(1, 3, 3)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(2, 5, 6)
graph.add_edge(4, 5, 1)

start_vertex = 0
distances = graph.dijkstra(start_vertex)
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex}: Шлях = {distance}")
