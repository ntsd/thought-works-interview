from trains.graph import Graph
from trains.exceptions import NoSuchRouteException, RouteNotPossibleException

import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_route('A', 'B', 5)
        self.graph.add_route('B', 'C', 4)
        self.graph.add_route('C', 'D', 8)
        self.graph.add_route('D', 'C', 8)
        self.graph.add_route('D', 'E', 6)
        self.graph.add_route('A', 'D', 5)
        self.graph.add_route('C', 'E', 2)
        self.graph.add_route('E', 'B', 3)
        self.graph.add_route('A', 'E', 7)

    def test_add_route(self):
        self.graph.add_route('C', 'D', 7)
        self.assertEqual(self.graph.get_distance('C', 'D'), 7)

    def test_get_distance(self):
        self.assertEqual(self.graph.get_distance('A', 'B'), 5)
        self.assertEqual(self.graph.get_distance('B', 'C'), 4)

    def test_get_distance_no_such_route_exception(self):
        self.assertRaises(NoSuchRouteException, self.graph.get_distance, 'F', 'A')
        self.assertRaises(NoSuchRouteException, self.graph.get_distance, 'A', 'F')

    def test_get_neighbors(self):
        self.assertEqual(list(self.graph.get_neighbors('A')), ['B', 'D', 'E'])
        self.assertEqual(list(self.graph.get_neighbors('C')), ['D', 'E'])

    def test_get_all_routes_by_depth(self):
        self.assertEqual(
            list(self.graph.get_all_routes_by_depth('C', 'C', max_depth=3)),
            [['C', 'E', 'B', 'C'], ['C', 'D', 'C']]
        )

    def test_get_all_routes_by_distance(self):
        self.assertEqual(
            list(self.graph.get_all_routes_by_distance('C', 'C', max_distance=30)),
            [['C', 'E', 'B', 'C'],
            ['C', 'E', 'B', 'C', 'E', 'B', 'C'],
            ['C', 'E', 'B', 'C', 'E', 'B', 'C', 'E', 'B', 'C'],
            ['C', 'E', 'B', 'C', 'D', 'C'],
            ['C', 'D', 'C'],
            ['C', 'D', 'E', 'B', 'C'],
            ['C', 'D', 'C', 'E', 'B', 'C']]
        )

    def test_get_shortest_distance(self):
        self.assertEqual(self.graph.get_shortest_distance('A', 'C'), 9)
        self.assertEqual(self.graph.get_shortest_distance('B', 'B'), 9)

    def test_get_shortest_distance_route_not_possible_exception(self):
        self.assertRaises(RouteNotPossibleException, self.graph.get_shortest_distance, 'A', 'F')


if __name__ == "__main__":
    unittest.main()
