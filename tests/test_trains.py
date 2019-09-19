from trains.trains import Trains
from trains.exceptions import RouteNotPossibleException

import unittest


class TestTrains(unittest.TestCase):
    
    def setUp(self):
        self.trains = Trains("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7") 

    def test_get_sum_distance(self):
        self.assertEqual(self.trains.get_sum_distance('A', 'B', 'C'), 9)
        self.assertEqual(self.trains.get_sum_distance('A', 'D'), 5)
        self.assertEqual(self.trains.get_sum_distance('A', 'D', 'C'), 13)
        self.assertEqual(self.trains.get_sum_distance('A', 'E', 'B', 'C', 'D'), 22)

    def test_get_sum_distance_no_such_route(self):
        self.assertEqual(self.trains.get_sum_distance('A', 'E', 'D'), "NO SUCH ROUTE")

    def test_count_paths_with_max_routes(self):
        self.assertEqual(self.trains.count_paths_with_max_routes('C', 'C', 3), 2)

    def test_count_paths_with_exact_routes(self):
        self.assertEqual(self.trains.count_paths_with_exact_routes('A', 'C', 4), 3)

    def test_shortest_route_distance(self):
        self.assertEqual(self.trains.shortest_route_distance('A', 'C'), 9)
        self.assertEqual(self.trains.shortest_route_distance('B', 'B'), 9)

    def test_shortest_route_distance_route_not_possible_exception(self):
        self.assertRaises(RouteNotPossibleException, self.trains.shortest_route_distance, 'B', 'F')

    def test_difference_route_by_distance(self):
        self.assertEqual(self.trains.difference_route_by_distance('C', 'C', 30), 7)


if __name__ == "__main__":
    unittest.main()
