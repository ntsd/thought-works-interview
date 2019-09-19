### Trains Problem

algorithms that are used to solve this problem with graph structure.

##### 1. Depth-first Search (DFS)
   
   DFS to get all paths by depth or distance because DFS use lower memory than Breadth-first search (BFS) and it just gets all paths until the depth is more than maximum depth or distance is more than maximum distance so BFS is unnecessary for this problem.

   I created get_all_routes_in_depth and get_all_routes_in_distance because of this problem not require to store both distance and depth for it so I separate it for saving resource.

##### 2. Dijkstra's
    
    Dijkstra for shortest distance because Dijkstra will pick node from closest distance first difference to BFS or DFS that will pick node base on root or children nodes.

    Response only distance when finding the destination because this problem only needs to find the shortest distance, not a full path.

#### Requirements:
- Python3 (version >= 3.6)

Run these command on this directory

#### Run example

```
python3 main.py
```

#### Run test all

```
python3 -m unittest discover
```

#### Run test specific

```
python3 -m unittest tests.test_graph
python3 -m unittest tests.test_trains
```
