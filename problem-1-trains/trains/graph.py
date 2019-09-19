from trains.exceptions import NoSuchRouteException, RouteNotPossibleException

import bisect
import heapq
from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.routes = defaultdict(dict)

    def add_route(self, node_from, node_to, distance):
        self.routes[node_from][node_to] = distance

    def get_distance(self, node_from, node_to):
        try:
            return self.routes[node_from][node_to]
        except KeyError:
            raise NoSuchRouteException("NO SUCH ROUTE")
    
    def get_childs(self, node):
        return self.routes[node].keys()

    def get_all_routes_in_depth(self, start, end=None, max_depth=0):
        """DFS"""
        stack = [(start, [start], 1)]
        while stack:
            (current, path, depth) = stack.pop()
            for neighbour in self.get_childs(current):
                if neighbour == end or depth >= max_depth:
                    yield path + [neighbour]
                else:
                    stack.append((neighbour, path + [neighbour], depth + 1))
    
    def get_all_routes_in_distance(self, start, max_distance=0): # bug
        """DFS"""
        stack = [(start, [start], 0)]
        while stack:
            (current, path, distance) = stack.pop()
            for neighbour in self.get_childs(current):
                if distance >= max_distance:
                    yield path + [neighbour]
                else:
                    stack.append((neighbour, path + [neighbour], distance + self.get_distance(current, neighbour)))

    def get_shortest_distance(self, start, end):
        """Dijkstra algorithm"""
        shortest_paths = {start: (None, 0)}
        visited = set()
        current_node = start

        while current_node != end or len(visited) == 0:
            visited.add(current_node)
            destinations = self.get_childs(current_node)
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = weight_to_current_node + self.get_distance(current_node, next_node)
                if next_node not in shortest_paths or next_node == start: # check next_node == start for start and end is the same node
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if weight < current_shortest_weight:
                        shortest_paths[next_node] = (current_node, weight)
                
            next_destinations = {}
            for node in shortest_paths:
                if node not in visited:
                    next_destinations[node] = shortest_paths[node]
                
            if not next_destinations: # break when no route
                break
            
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        try:
            return shortest_paths[end][1]
        except KeyError:
            raise RouteNotPossibleException("NO SUCH ROUTE")


if __name__ == "__main__":
    graph = Graph()
    graph.add_route('A', 'B', 5)
    graph.add_route('B', 'C', 4)
    graph.add_route('C', 'D', 8)
    graph.add_route('D', 'C', 8)
    graph.add_route('D', 'E', 6)
    graph.add_route('A', 'D', 5)
    graph.add_route('C', 'E', 2)
    graph.add_route('E', 'B', 3)
    graph.add_route('A', 'E', 7)
    print(list(graph.get_all_routes_in_depth('C', 'C', max_depth=3)))
    print(list(graph.get_all_routes_in_depth('A', max_depth=4)))
    print(graph.get_shortest_distance('A', 'C'))
    print(graph.get_shortest_distance('B', 'B'))
    print(list(graph.get_all_routes_in_distance('C', max_distance=30)))
