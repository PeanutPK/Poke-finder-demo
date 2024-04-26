from collections import deque
from data.city_relation import city_relation as vertex_data


class Vertex:
    def __init__(self, name, child):
        self.name = name
        self.child = child
        self.distance = -1


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
                print("Marking neighbor:", neighbor)
                mark[neighbor] = True
                parent[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    print("End vertex", end, "not found!")
    return None


if __name__ == '__main__':
    # Starting BFS from 'Viridian City' to all Geodude capture area by walking
    start_vertex = 'Viridian City'
    capture_area = {"Mt. Moon": None, "Rock Tunnel": None, "Victory Road": None}
    end_vertex = 'Mt. Moon'
    for area_name in capture_area.keys():
        end_vertex = area_name
        value = bfs(start_vertex, end_vertex)
        capture_area[area_name] = value
