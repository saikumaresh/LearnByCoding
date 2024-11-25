class Graph:
    def __init__(self, edges):
        """
        Initialize the graph with edges.
        Convert the edge list into a dictionary for easy lookup.
        """
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        """
        Find all paths from 'start' to 'end' using recursion.
        Avoid revisiting nodes in the current path to prevent cycles.
        """
        path = path + [start]  # Update the current path

        # If start equals end, we've found a path
        if start == end:
            return [path]

        # If start node is not in the graph, return no paths
        if start not in self.graph_dict:
            return []

        # Explore all neighbors of the current node
            paths = []
            for node in self.graph_dict[start]:
                if node not in path:  # Avoid revisiting nodes
                    new_paths = self.get_paths(node, end, path)
                    for p in new_paths:
                        paths.append(p)

            return paths

    def get_shortest_path(self, start, end, path=[]):
        """
        Find the shortest path from 'start' to 'end' using recursion.
        Avoid revisiting nodes in the current path to prevent cycles.
        """
        path = path + [start]  # Update the current path

        # If start equals end, we've found a path
        if start == end:
            return path

        # If start node is not in the graph, return no path
        if start not in self.graph_dict:
            return None

        # Explore all neighbors of the current node
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:  # Avoid revisiting nodes
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == '__main__':

    # Test case 1: Example graph with direct and indirect paths
    routes1 = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    graph1 = Graph(routes1)

    # Test case 1 outputs
    print("\nTest Case 1:")
    print("All paths from Mumbai to New York:", graph1.get_paths("Mumbai", "New York"))
    print("Shortest path from Mumbai to New York:", graph1.get_shortest_path("Mumbai", "New York"))
    print("All paths from Dubai to New York:", graph1.get_paths("Dubai", "New York"))
    print("Shortest path from Dubai to New York:", graph1.get_shortest_path("Dubai", "New York"))

    # Test case 2: Graph with multiple paths and cycles
    routes2 = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "C"),  # Cycle in the graph
        ("E", "F"),
    ]

    graph2 = Graph(routes2)

    # Test case 2 outputs
    print("\nTest Case 2:")
    print("All paths from A to F:", graph2.get_paths("A", "F"))
    print("Shortest path from A to F:", graph2.get_shortest_path("A", "F"))
    print("All paths from C to E:", graph2.get_paths("C", "E"))
    print("Shortest path from C to E:", graph2.get_shortest_path("C", "E"))

    # Test case 3: Disconnected graph
    routes3 = [
        ("1", "2"),
        ("2", "3"),
        ("4", "5"),
    ]

    graph3 = Graph(routes3)

    # Test case 3 outputs
    print("\nTest Case 3:")
    print("All paths from 1 to 3:", graph3.get_paths("1", "3"))
    print("Shortest path from 1 to 3:", graph3.get_shortest_path("1", "3"))
    print("All paths from 1 to 5:", graph3.get_paths("1", "5"))  # No path
    print("Shortest path from 1 to 5:", graph3.get_shortest_path("1", "5"))  # No path
    
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))