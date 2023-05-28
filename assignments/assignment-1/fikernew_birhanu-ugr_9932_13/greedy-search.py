from random import shuffle
import time
from graph import Graph, load_romania_graph

romania: Graph = load_romania_graph()

def greedy_search(graph: Graph, start: str, goal: str) -> bool:
    visited = set([start])

    curr_city = start
    unvisited_neighbours = [(neighbour, weight) for neighbour, weight in graph.get_neighbours(curr_city)]
    path = [start]

    while unvisited_neighbours:
        for city, weight in unvisited_neighbours:
            if city == goal:
                print(path + [city])
                return True
        
        curr_city = min(unvisited_neighbours, key=lambda x: x[1])[0]
        visited.add(curr_city)
        path.append(curr_city)

        neighbours = graph.get_neighbours(curr_city)
        unvisited_neighbours = [(neighbour, weight) for neighbour, weight in neighbours if neighbour not in visited]

    print(path)
    return False

    
# A.
# Benchmark test:
romanian_cities = [city for city in romania.get_nodes()]
shuffle(romanian_cities)
random_cities = romanian_cities[:10]

for city1 in random_cities:
    for city2 in random_cities:
        if city1 is not city2:

            start_time = time.time()
            
            found: bool = greedy_search(romania, city1, city2)

            end_time = time.time()

            elapsed_time = end_time - start_time

            print(f"Finding path between {city1} -> {city2} [{'successfull' if found else 'unsuccessful'}]. Elapsed time:", elapsed_time)
