from trains.graph import Graph
from trains.exceptions import NoSuchRouteException

import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_route('A', 'B', 5)
        self.graph.add_route('B', 'C', 15)

    def test_add_node(self):
        self.graph.add_route('C', 'D', 7)
        self.assertEqual(self.graph.get_distance('C', 'D'), 7)

    def test_get_distance(self):
        self.assertEqual(self.graph.get_distance('A', 'B'), 5)
        self.assertEqual(self.graph.get_distance('B', 'C'), 15)

    def test_no_such_route_exception(self):
        self.assertRaises(NoSuchRouteException, self.graph.get_distance, 'A', 'C')


if __name__ == "__main__":
    unittest.main()
