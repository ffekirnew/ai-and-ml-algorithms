class Graph:
    def __init__(self) -> None:
        self.graph: dict(dict(int)) = {} # to contain key value pairs of ( node : (neighbours : weight ) )

    def get_nodes(self) -> list[str]:
        """Get all nodes on the graph.

        Returns:
            list[str]: A list of all nodes in the graph.
        """
        return list(self.graph.keys())
    
    def add_node(self, node: str) -> None:
        """Add a new node to the graph.

        Args:
            node (str): Representation of the new node to be added.
        """
        # check if the node already exists in the graph
        if node not in self.graph:
            self.graph[node] = {} # to contain key value pairs of ( neighbours : weight )
    
    def insert_edge(self, node1: str, node2: str, weight: int) -> None:
        """Insert an edge between two nodes into the graph.

        Args:
            node1 (str): Representation of node 1.
            node2 (str): Representation of node 2.
            weight (int): Representation of the weight of the path between the two nodes.
        """
        # add both nodes to the graph
        self.add_node(node1)
        self.add_node(node2)

        # make each nodes the neighbours of eachother by adding them to the graph with the given weight
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight
    
    def delete_node(self, node: str) -> None:
        """Delete a node in the graph.

        Args:
            node (str): Representation of the node to be deleted.
        """
        # check if the node to be deleted exists on the graph
        if node in self.graph:

            # if so, delete all references of the node from all neighbours
            for neighbour in self.graph[node]:
                del self.graph[neighbour][node]
            
            # finally delete the node
            del self.graph[node]
    
    def delete_edge(self, node1: str, node2: str) -> None:
        """Delete an edge between two nodes in the graph.

        Args:
            node1 (str): Representation of node 1.
            node2 (str): Representation of node 2.
        """
        # check if both nodes are on the graph
        if node1 in self.graph and node2 in self.graph:

            # check if there is an edge between the nodes.
            if node2 in self.graph[node1]:
                del self.graph[node1][node2]
                del self.graph[node2][node1]
    
    def get_neighbours(self, node: str) -> dict:
        if node in self.graph:
            return list(self.graph[node].items())


def load_romania_graph() -> Graph:
    romania = Graph()

    # add the nodes to the graph
    romania.add_node("Oradea")
    romania.add_node("Zerind")
    romania.add_node("Arad")
    romania.add_node("Timisoara")
    romania.add_node("Lugoj")
    romania.add_node("Mehadia")
    romania.add_node("Drobeta")
    romania.add_node("Sibiu")
    romania.add_node("Rimnicu Vilcea")
    romania.add_node("Craiova")
    romania.add_node("Fagaras")
    romania.add_node("Pitesti") 
    romania.add_node("Bucharest") 
    romania.add_node("Giurgiu") 
    romania.add_node("Neamt") 
    romania.add_node("Iasi") 
    romania.add_node("Vaslui") 
    romania.add_node("Urziceni") 
    romania.add_node("Hirsova") 
    romania.add_node("Eforie")

    # insert the edges between the different nodes
    romania.insert_edge("Oradea", "Zerind", 71)
    romania.insert_edge("Oradea", "Sibiu", 151)
    romania.insert_edge("Zerind", "Arad", 75)
    romania.insert_edge("Arad", "Sibiu", 140)
    romania.insert_edge("Arad", "Timisoara", 118)
    romania.insert_edge("Timisoara", "Lugoj", 111)
    romania.insert_edge("Lugoj", "Mehadia", 70)
    romania.insert_edge("Mehadia", "Drobeta", 75)
    romania.insert_edge("Drobeta", "Craiova", 120)
    romania.insert_edge("Sibiu", "Rimnicu Vilcea", 80)
    romania.insert_edge("Rimnicu Vilcea", "Craiova", 146)
    romania.insert_edge("Sibiu", "Fagaras", 99)
    romania.insert_edge("Fagaras", "Bucharest", 211)
    romania.insert_edge("Rimnicu Vilcea", "Pitesti", 97)
    romania.insert_edge("Pitesti", "Bucharest", 101)
    romania.insert_edge("Bucharest", "Giurgiu", 90)
    romania.insert_edge("Iasi", "Neamt", 87)
    romania.insert_edge("Iasi", "Vaslui", 92)
    romania.insert_edge("Vaslui", "Urziceni", 142)
    romania.insert_edge("Urziceni", "Bucharest", 85)
    romania.insert_edge("Urziceni", "Hirsova", 98)
    romania.insert_edge("Hirsova", "Eforie", 86)

    return romania
