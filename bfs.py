# from collections import deque
#
# adj = []
# mark = []
# parent = []
# dist = []
# for i in range(1000):
#     mark.append(False)
#     parent.append(-1)
#     dist.append(9999)
#
#
# class Vertex:
#     def __init__(self, index, name, child):
#         self.index = index
#         self.name = name
#         self.child = child
#         self.distance = -1
#
#
# vertex_data = {
#     'Veridian City': ['Route 2', 'Route 22', 'Route 1'],
#     'Route 2': ["Diglett's Cave", "Viridian Forest",
#                 "Pewter City"],
#     'Pewter City': ["Route 3"],
#     'Route 3': ["Mt. Moon"],
#     "Mt. Moon": ["Route 4"],
#     "Route 4": ["Cerulean City"],
#     "Cerulean City": ["Route 9", "Route 5", "Route 24"],
#     "Route 9": ["Rock Tunnel"]
# }
#
#
# def bfs(n, s):
#     for i in range(n):
#         mark[i] = False
#         dist[i] = 9999
#         parent[i] = -1
#
#     dist[s] = 0
#
#     bag = deque()
#     bag.append((-1, s))
#     while bag:
#         p, v = bag.popleft()
#         if not mark[v]:
#             mark[v] = True
#             parent[v] = p
#             if p != -1:
#                 dist[v] = dist[p] + 1
#             for w in adj[v]:
#                 bag.append((v, w))
#
#
# def main():
#     n, m = map(int, input().split())
#     for _ in range(m):
#         a, b = map(int, input().split())
#         adj[a].append(b)
#
#     bfs(n, 0)
#
#     for i in range(n):
#         print(parent[i], end=' ')
#
#
# if __name__ == "__main__":
#     main()
from collections import deque


class Vertex:
    def __init__(self, name, child):
        self.name = name
        self.child = child
        self.distance = -1


vertex_data = {
    'Veridian City': ['Route 2', 'Route 22', 'Route 1'],
    'Route 2': ["Diglett's Cave", "Viridian Forest",
                "Pewter City"],
    'Pewter City': ["Route 3"],
    'Route 3': ["Mt. Moon"],
    "Mt. Moon": ["Route 4"],
    "Route 4": ["Cerulean City"],
    "Cerulean City": ["Route 9", "Route 5", "Route 24"],
    "Route 9": ["Rock Tunnel"],
    "Route 22": ["Pokemon League"],
    "Pokemon League": ["Route 23"],
    "Route 23": ["Victory Road"],
    "Route 1": ["Pallet Town"],
    "Pallet Town": ["Route 21"],
    "Route 21": ["Cinnabar Island", "Pokemon Mansion"],
    "Pokemon Mansion": ["Cinnabar Island"],
    "Cinnabar Island": ["Route 20"],
    "Route 20": ["Seafoam Islands"], "Seafoam Islands": ["Route 19"],
    "Route 19": ["Fuchsia City"],
    "Fuchsia City": ["Safari Zone", "Route 15", "Route 18"],
    "Safari Zone": [], "Route 18": []
}

# Initialize data structures
adj = {}
for key, value in vertex_data.items():
    adj[key] = Vertex(key, value)

mark = {key: False for key in adj}
parent = {key: -1 for key in adj}
dist = {key: 9999 for key in adj}


def bfs(start, end):
    queue = deque()
    queue.append(start)
    dist[start] = 0
    mark[start] = True

    while queue:
        current = queue.popleft()
        print("Visiting:", current)
        if current == end:
            print("Reached end vertex:", end)
            # Construct path from start to end
            path = []
            while current != -1:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path from start to end:", path)
            return path
        for neighbor in adj[current].child:
            print("Checking neighbor:", neighbor)
            if not mark[neighbor]:
                mark[neighbor] = True
                parent[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    print("End vertex", end, "not found!")
    return None


# Starting BFS from 'Veridian City' to find 'Cerulean City'
start_vertex = 'Veridian City'
end_vertex = 'Cerulean City'
bfs(start_vertex, end_vertex)
