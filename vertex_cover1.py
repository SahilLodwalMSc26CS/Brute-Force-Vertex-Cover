import networkx as nx
import matplotlib.pyplot as plt
import time
import csv
import random
import os

#----------------------------------------------#
RESULT_FILE = "results.txt"
IMAGE_FILE = "vertex_cover_graphs.png"
CSV_file = "P1_Results.csv"
VERTICES = 10
EDGE_COUNTS = [10, 15, 20, 25, 30, 35, 40, 45]

#Used GenAI for bitmasking for subset making
#----------------------------------------------#

def generate_connected_edges(num_vertices, target_edge_count):
    nodes = list(range(num_vertices))
    random.shuffle(nodes)

    connected_edges = []
    for i in range(1, num_vertices):
        u = nodes[i]
        v = random.choice(nodes[:i])
        connected_edges.append((min(u, v), max(u, v)))

    all_possible = []
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            edge = (u, v)
            if edge not in connected_edges:
                all_possible.append(edge)

    remaining_needed = target_edge_count - len(connected_edges)
    if remaining_needed > 0 and len(all_possible) >= remaining_needed:
        extra_edges = random.sample(all_possible, remaining_needed)
        connected_edges.extend(extra_edges)

    return connected_edges
#----------------------------------------------------#

def create_edge_files():
    edges = []
    for u in range(VERTICES):
        for v in range(u + 1, VERTICES):
            edges.append((u, v))

    if len(edges) < VERTICES:
        raise ValueError("Not enough vertices to generate all possible edges.")
        
    for n in EDGE_COUNTS:
        filename = f"edges_{n}.txt"
        if not os.path.exists(filename):
            random_edges = generate_connected_edges(VERTICES, n)
            if len(random_edges) > n:
                for i in range(len(random_edges) - n):
                    random_edges.pop()
            with open(filename, "w") as file:
                for u, v in random_edges:
                    file.write(f"{u} {v}\n")
            print(f"{filename} created.")
        else:
            print(f"{filename} already exists. Keeping it unchanged.")
#----------------------------------------------------#

def read_edges(filename):
    edges = []
    with open(filename, "r") as file:
        for line in file:
            u, v = map(int, line.split())
            edges.append((u, v))
    return edges
#----------------------------------------------------#

# Brute force Vertex Cover
def brute_force_vertex_cover(G):
    vertices = list(G.nodes())
    edges = list(G.edges())

    for mask in range(1 << len(vertices)):
        cover = []
        for i in range(len(vertices)):
            if (mask >> i) & 1:
                cover.append(vertices[i])
        if all(u in cover or v in cover for u, v in edges):
            return cover
#----------------------------------------------------#

def draw_graph(G, cover, axis, edge_count):
    position = nx.spring_layout(G, seed=1)
    colors = [
        "red" if vertex in cover else "lightgreen"
        for vertex in G.nodes()
    ]

    nx.draw(
        G,
        position,
        ax=axis,
        with_labels=True,
        node_color=colors,
        node_size=500,
        edge_color="gray",
        font_weight="bold"
    )

    axis.set_title(
        f"Edges: {edge_count} | VC Size: {len(cover)}"
    )
#----------------------------------------------------#

def calculate_complexity_ops(v_count, e_count):
    """
    Computes total structural operations based on O(2^V * V * E)
    """
    subsets = 1 << v_count # Equivalent to 2^V
    total_operations = subsets * v_count * e_count
    return total_operations
#----------------------------------------------------#

# Save results
def save_results(results):
    with open(RESULT_FILE, "w") as file:
        file.write("BRUTE FORCE VERTEX COVER RESULTS\n")
        file.write("================================\n\n")
        file.write("Base Complexity Formula: O(2^|V| * |V| * |E|)\n")
        file.write(f"Total Static Vertices (V): {VERTICES}\n\n")

        for edges, size, time_ms, cover, ops in results:
            file.write(f"Edges (E): {edges}\n")
            file.write(f"Vertices (V): {VERTICES}\n")
            file.write(f"VC Size: {size}\n")
            file.write(f"Theoretical Complexity Equation: O(2^{VERTICES} * {VERTICES} * {edges})\n")
            file.write(f"Calculated Worst-Case Operations: {ops:,}\n")
            file.write(f"Running Time: {time_ms:.6f} ms\n")
            file.write(f"Vertex Cover: {cover}\n")
            file.write("--------------------------------\n\n")

# Save results to CSV
def save_csv(results):

    with open(CSV_file, "w", newline="") as file:
        writer = csv.writer(file)

        # Headings for P1 - BF
        writer.writerow(["","Practical 1 - Vertex Cover BFA",""])
        writer.writerow(["(n,m)", "Size", "Time"])

        for edges, size, time_ms, cover, ops in results:
            writer.writerow([
                (VERTICES,edges),
                size,
                time_ms
            ])
#----------------------------------------------------#

def main():
    create_edge_files()
    figure, axes = plt.subplots(2, 4, figsize=(16, 9))
    axes = axes.flatten()
    results = []
    for i, edge_count in enumerate(EDGE_COUNTS):
        filename = f"edges_{edge_count}.txt"


        edges = read_edges(filename)
        graph = nx.Graph()
        graph.add_nodes_from(range(VERTICES))
        graph.add_edges_from(edges)


        start = time.perf_counter()
        cover = brute_force_vertex_cover(graph)
        time_ms = (time.perf_counter() - start) * 1000


        ops = calculate_complexity_ops(VERTICES, edge_count)

        print(
            f"Edges: {edge_count} | "
            f"VC Size: {len(cover)} | "
            f"Ops: {ops:,} | "
            f"Time: {time_ms:.6f} ms | "
            f"Cover: {sorted(cover)}"
        )

        results.append(
            (edge_count, len(cover), time_ms, sorted(cover), ops)
        )

        draw_graph(
            graph,
            cover,
            axes[i],
            edge_count
        )

    figure.suptitle(
        "Brute Force Vertex Cover\nRed Nodes = Vertex Cover",
        fontsize=16
    )

    plt.tight_layout()
    plt.savefig(
        IMAGE_FILE,
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

    save_results(results)
    save_csv(results)

    print("\nSaved:")
    print(IMAGE_FILE)
    print(RESULT_FILE)
    print(CSV_file)
#----------------------------------------------------#

main()
