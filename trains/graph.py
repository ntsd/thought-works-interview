from trains.exceptions import NoSuchRouteException, RouteNotPossibleException

import bisect
import heapq
from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.routes = defaultdict(dict)

    def add_route(self, node_from, node_to, distance):
        """Add route to graph"""
        self.routes[node_from][node_to] = distance

    def get_distance(self, node_from, node_to):
        """Get distance of route"""
        try:
            return self.routes[node_from][node_to]
        except KeyError:
            raise NoSuchRouteException("NO SUCH ROUTE")
    
    def get_childs(self, node):
        """Get childs of node"""
        return self.routes[node].keys()

    def get_all_routes_in_depth(self, start, end, max_depth):
        """Get all routes by Depth First Search stop when depth is more than max depth."""
        stack = [(start, [start], 1)]
        while stack:
            (current, path, depth) = stack.pop()
            for neighbour in self.get_childs(current):
                if neighbour == end:
                    yield path + [neighbour]
                if depth < max_depth:
                    stack.append((neighbour, path + [neighbour], depth + 1))
    
    def get_all_routes_in_distance(self, start, end, max_distance):
        """Get all routes by Depth First Search stop when distance is more than max distance."""
        stack = [(start, [start], 0)]
        while stack:
            (current, path, distance) = stack.pop()
            for neighbour in self.get_childs(current):
                next_distance = distance + self.get_distance(current, neighbour)
                if next_distance < max_distance:
                    if neighbour == end:
                        yield path + [neighbour]
                    stack.append((neighbour, path + [neighbour], next_distance))

    def get_shortest_distance(self, start, end):
        """Find shortest distance from start to end by Dijkstra Algorithm."""
        shortest_paths = {start: (None, 0)}
        visited = set()
        current_node = start

        while current_node != end or len(visited) == 0:
            visited.add(current_node)
            destinations = self.get_childs(current_node)
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = weight_to_current_node + self.get_distance(current_node, next_node)
                if next_node not in shortest_paths or next_node == start: # next_node == start for start and end is the same node
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if weight < current_shortest_weight:
                        shortest_paths[next_node] = (current_node, weight)
                
            next_destinations = {}
            for node in shortest_paths:
                if node not in visited:
                    next_destinations[node] = shortest_paths[node]
                
            if not next_destinations:
                break
            
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        try:
            return shortest_paths[end][1]
        except KeyError:
            raise RouteNotPossibleException()


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
    print(list(graph.get_all_routes_in_depth('A', 'C', max_depth=4)))
    print(graph.get_shortest_distance('A', 'C'))
    print(graph.get_shortest_distance('B', 'B'))
    print(list(graph.get_all_routes_in_distance('C', 'C', max_distance=30)))
