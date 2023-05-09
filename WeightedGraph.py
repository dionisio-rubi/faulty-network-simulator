from Node import *
import random


class WeightedGraph:
    counter = 0

    def __init__(self):
        self.nodes = {}  # key: node_id, value: Node object
        self.adjacency_matrix = {}  # key: node_id, value: list of neighbors

    def add_node(self, node: Node) -> None:
        self.nodes[node.get_id()] = node

    def remove_node(self, node_id: str) -> None:
        node = self.nodes[node_id]
        for neighbor in node.get_neighbors().keys():
            neighbor_id = neighbor.get_id()
            self.nodes[neighbor_id].remove_neighbor(node)
        del self.nodes[node_id]

    def add_edge(self, node1, node2, weight, link_failure_probability):
        node1 = self.nodes[node1.get_id()]
        node2 = self.nodes[node2.get_id()]
        link = Link(weight, link_failure_probability)
        node1.add_neighbor(node2, link)
        node2.add_neighbor(node1, link)

    def remove_edge(self, node1_id, node2_id):
        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]
        node1.remove_neighbor(node2_id)
        node2.remove_neighbor(node1_id)

    def get_nodes(self) -> dict:
        return self.nodes

    def get_node(self, node_id):
        return self.nodes[node_id]

    def simulate_node_failure(self, time) -> int:
        """
        Simulates a node failure for every node in the graph.
        Generates a random failure threshold for each node and compares it to the node's failure probability.
        If the node's failure probability is greater than the failure threshold, the node is removed from the graph.
        """
        with open('file.txt', 'a') as file:
            node_removed = 0  # int representing if a node was removed, not removed, or no nodes in graph
            # Write to file
            # file.write(f'{time:.1f}s :Simulating node failure...\n')
            print(f'{time:.1f}s : Node failure sim{"." * (WeightedGraph.counter + 1)}')
            to_remove = []
            if len(self.nodes) == 0:
                print("No nodes in graph")
                node_removed = -1
            for node_id, node in self.nodes.items():
                failure_threshold = random.random()
                if failure_threshold <= node.node_failure_probability:
                    # Write to file
                    # file.write(f'Node {node_id} failed\n')
                    print(f'Node {node_id} failed - Failure Probability= {node.node_failure_probability:.2f} >= Failure Threshold= {failure_threshold:.2f}')
                    to_remove.append(node_id)
                    node_removed = 1
            for node_id in to_remove:
                self.remove_node(node_id)

        WeightedGraph.counter = (WeightedGraph.counter + 1) % 3
        return node_removed

    def simulate_link_failure(self):
        """
        Simulates a link failure for every link in the graph.
        Generates a random failure threshold for each link and compares it to the link's failure probability.
        If the link's failure probability is greater than the failure threshold, the link is removed from the graph.
        """
        print("Simulating link failure...")
        temp = self.nodes.copy()

    def __str__(self):
        for node in self.nodes.values():
            print(node)
            for neighbor in node.neighbors:
                print(f'    {neighbor} - {node.neighbors[neighbor]}')
