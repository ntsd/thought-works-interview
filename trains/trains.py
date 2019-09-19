from trains.graph import Graph
from trains.exceptions import NoSuchRouteException


class Trains:

    def __init__(self, text):
        self.graph = Graph()
        self.add_routes_from_text(text)

    def add_routes_from_text(self, text):
        for route_text in text.replace(' ','').split(','):
            self.graph.add_route(route_text[0], route_text[1], int(route_text[2]))    

    def get_sum_distance(self, *routes):
        try:
            return sum(self.graph.get_distance(routes[i], routes[i + 1]) for i in range(len(routes) - 1))
        except NoSuchRouteException as e:
            return e.message

    def count_paths_with_max_routes(self, start_node, end_node, max_routes):
        return len(list(self.graph.get_all_routes_in_depth(start_node, end_node, max_routes)))

    def count_paths_with_exact_routes(self, start_node, end_node, exact_routes):
        count = 0
        for route in self.graph.get_all_routes_in_depth(start_node, end_node, exact_routes):
            if len(route) == exact_routes + 1:
                count += 1
        return count

    def shortest_route_distance(self, start_node, end_node):
        return self.graph.get_shortest_distance(start_node, end_node)

    def difference_route_in_distance(self, start_node, end_node, distance):
        return len(list(self.graph.get_all_routes_in_distance(start_node, end_node, distance)))

if __name__ == "__main__":
    trains = Trains("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
    print(trains.get_sum_distance('A', 'B', 'C'))
    print(trains.get_sum_distance('A', 'D'))
    print(trains.get_sum_distance('A', 'D', 'C'))
    print(trains.get_sum_distance('A', 'E', 'B', 'C', 'D'))
    print(trains.get_sum_distance('A', 'E', 'D'))
    print(trains.count_paths_with_max_routes('C', 'C', 3))
    print(trains.count_paths_with_exact_routes('A', 'C', 4))
    print(trains.shortest_route_distance('A', 'C'))
    print(trains.shortest_route_distance('B', 'B'))
    print(trains.difference_route_in_distance('C', 'C', 30))