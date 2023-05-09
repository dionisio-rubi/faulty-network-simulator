import concurrent.futures
import heapq
import time
from Node import Node
from WeightedGraph import WeightedGraph


start_time = time.monotonic()

graph = WeightedGraph()

def main():
    #Create nodes
    node_a = Node("A", 0.15)
    node_b = Node("B", 0.2)
    node_c = Node("C", 0.05)
    node_d = Node("D", 0.0875)
    node_e = Node("E", 0.1)

    # Add some nodes
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)
    graph.add_node(node_e)

    # Add some edges
    graph.add_edge(node_a, node_b, 5, 0.1)
    graph.add_edge(node_a, node_c, 3, 0.2)
    graph.add_edge(node_b, node_c, 1, 0.05)
    graph.add_edge(node_b, node_d, 2, 0.1)
    graph.add_edge(node_c, node_d, 4, 0.3)
    graph.add_edge(node_d, node_e, 6, 0.2)

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     future = executor.submit(run_timer, 1)

    shortest_paths = dijkstra(graph, node_a)
    for node_id, distance in shortest_paths.items():
        print(f'Node A -> Node {node_id}: {distance:.2f}')


def print_elapsed_time():
    elapsed_time = time.monotonic() - start_time
    print(f"Elapsed time: {elapsed_time:.1f} seconds")


def run_timer(interval):
    while True:
        flag = graph.simulate_node_failure(time.monotonic() - start_time)
        if flag:
            return
        time.sleep(interval)


def dijkstra(graph: WeightedGraph, source: Node):
    nodes = graph.get_nodes()
    distances = {}  # key: node_id, value: distance from source
    for node_id in nodes.keys():
        distances[node_id] = float('inf')
    distances[source.get_id()] = 0
    heap = [(distances[source.get_id()], source)]
    heapq.heapify(heap)

    while len(heap) > 0:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > distances[curr_node.get_id()]:
            continue
        # For each neighbor of the current node
        for neighbor, link in (graph.get_neighbors(curr_node.get_id())).items():
            # Calculate the distance to the neighbor through the current node
            dist = curr_dist + link.cost

            # If the distance to the neighbor is less than the current known distance,
            # update the distance and add the neighbor to the priority queue
            if dist < distances[neighbor.get_id()]:
                distances[neighbor.get_id()] = dist
                heapq.heappush(heap, (dist, neighbor))
    return distances

# WORKING CODE
# def dijkstra(graph: WeightedGraph, source: Node):
#     nodes = graph.get_nodes()
#     distances = {}  # key: node_id, value: distance from source
#     for node_id in nodes.keys():
#         distances[node_id] = float('inf')
#     distances[source.get_id()] = 0
#     heap = [(distances[source.get_id()], source)]
#     heapq.heapify(heap)
#
#     while len(heap) > 0:
#         curr_dist, curr_node = heapq.heappop(heap)
#         if curr_dist > distances[curr_node.get_id()]:
#             continue
#         # For each neighbor of the current node
#         for neighbor, link in (graph.get_neighbors(curr_node.get_id())).items():
#             # Calculate the distance to the neighbor through the current node
#             dist = curr_dist + link.cost
#
#             # If the distance to the neighbor is less than the current known distance,
#             # update the distance and add the neighbor to the priority queue
#             if dist < distances[neighbor.get_id()]:
#                 distances[neighbor.get_id()] = dist
#                 heapq.heappush(heap, (dist, neighbor))
#     return distances

if __name__ == '__main__':
    with open('file.txt', 'w') as f:
        f.truncate(0)
    main()
