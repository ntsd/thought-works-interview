from trains.trains import Trains

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
