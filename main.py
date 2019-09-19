from trains.trains import Trains

if __name__ == "__main__":
    inputs = open("input.txt", "r")
    for line in inputs.readlines():
        trains = Trains(line)
        print(trains.get_sum_distance('A', 'B', 'C'))
        print(trains.get_sum_distance('A', 'D'))
        print(trains.get_sum_distance('A', 'D', 'C'))
        print(trains.get_sum_distance('A', 'E', 'B', 'C', 'D'))
        print(trains.get_sum_distance('A', 'E', 'D'))
        print(trains.count_paths_with_max_routes('C', 'C', 3))
        print(trains.count_paths_with_exact_routes('A', 'C', 4))
        print(trains.shortest_route_distance('A', 'C'))
        print(trains.shortest_route_distance('B', 'B'))
        print(trains.difference_route_by_max_distance('C', 'C', 30))
