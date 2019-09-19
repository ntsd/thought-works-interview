from trains.graph import Graph
from trains.exceptions import NoSuchRouteException


class Trains:
    """
    Trains Class is created to solve The Trains problem.

    Args:
        text (str): row string of input of graph

    Attributes:
        graph (Graph): graph is algorithm class to solve Trains problem
    """

    def __init__(self, text):
        self.graph = Graph()
        self.add_routes_from_text(text)

    def add_routes_from_text(self, text):
        """Replace and split a raw string of Trains problem input and add a route to graph."""
        for route_text in text.replace(' ','').split(','):
            self.graph.add_route(route_text[0], route_text[1], int(route_text[2]))    

    def get_sum_distance(self, *routes):
        """Return sum of the distance of all node in the direction from first to last."""
        try:
            return sum(self.graph.get_distance(routes[i], routes[i + 1]) for i in range(len(routes) - 1))
        except NoSuchRouteException as e:
            return e.message

    def count_paths_with_max_routes(self, start_node, end_node, max_routes):
        """Return number of all paths start with start_node and end with end_node with max_routes."""
        return len(list(self.graph.get_all_routes_by_max_depth(start_node, end_node, max_routes)))

    def count_paths_with_exact_routes(self, start_node, end_node, exact_routes):
        """Return number of all paths start with start_node and end with end_node with exact_routes."""
        count = 0
        for route in self.graph.get_all_routes_by_max_depth(start_node, end_node, exact_routes):
            if len(route) == exact_routes + 1:
                count += 1
        return count

    def shortest_route_distance(self, start_node, end_node):
        """Return the shortest distance from start_node to end_node."""
        return self.graph.get_shortest_distance(start_node, end_node)

    def difference_route_by_max_distance(self, start_node, end_node, distance):
        """Return number of all paths start with start_node and end with end_node in distance."""
        return len(list(self.graph.get_all_routes_by_max_distance(start_node, end_node, distance)))


if __name__ == "__main__":
    help(Trains)
