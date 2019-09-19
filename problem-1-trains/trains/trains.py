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

    def count_paths_with_max_routes(start_node, end_node, max_routes):
        pass


if __name__ == "__main__":
    trains = Trains("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
    print(trains.get_sum_distance('A', 'B', 'C'))
    print(trains.get_sum_distance('A', 'D'))
    print(trains.get_sum_distance('A', 'D', 'C'))
    print(trains.get_sum_distance('A', 'E', 'B', 'C', 'D'))
    print(trains.get_sum_distance('A', 'E', 'D'))
