from Graph import Graph

def main():
    graph = Graph()
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    graph.add_edge(4, 2)

    # Set the order for BFS print
    order = "right"

    print("BFS:")
    graph.bfs(1, order)
    print("\nDFS:")
    graph.dfs(1)
    print("\nIs Bipartite:", graph.is_bipartite())
    print("Cycles:", graph.find_cycles())


if __name__ == "__main__":
    main();
