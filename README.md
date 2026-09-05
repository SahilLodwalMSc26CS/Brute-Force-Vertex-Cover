# Brute Force Vertex Cover

This project implements the **Brute Force Vertex Cover Algorithm** using Python and NetworkX.

## About the Project

The program finds a minimum Vertex Cover of a graph using a brute force approach.

A **Vertex Cover** is a set of vertices such that every edge in the graph has at least one endpoint in the selected set.

The program:

* Generates connected graphs with different numbers of edges.
* Reads graph edges from `.txt` files.
* Finds the Vertex Cover using brute force.
* Measures the running time.
* Calculates a theoretical worst-case operation count.
* Draws the graphs and highlights the Vertex Cover.
* Saves the results in `.txt` and `.csv` files.

## Input

The program uses graphs containing:

* **10 vertices**
* **10, 15, 20, 25, 30, 35, 40 and 45 edges**

The edge files are stored as:

```text
edges_10.txt
edges_15.txt
edges_20.txt
...
edges_45.txt
```

Each line represents an edge:

```text
0 1
0 2
1 3
```

## Algorithm

The brute force algorithm checks different subsets of vertices.

For every subset, it checks whether every edge has at least one endpoint in the subset.

The first valid subset found is returned as the Vertex Cover.

## Time Complexity

For a graph with `|V|` vertices and `|E|` edges:

```text
O(2^|V| × |V| × |E|)
```

There are `2^|V|` possible subsets of vertices.

For each subset:

* Creating/checking the subset can involve `|V|` vertices.
* Checking whether all edges are covered takes `|E|` operations.

Therefore:

```text
O(2^|V| × |V| × |E|)
```

## Output

The program produces:

### `results.txt`

Contains:

* Number of vertices
* Number of edges
* Vertex Cover size
* Theoretical complexity
* Calculated worst-case operations
* Running time
* Vertex Cover vertices

### `P1_Results.csv`

Contains the experimental results in CSV format:

```text
(n,m), Size, Time
```

### `vertex_cover_graphs.png`

Contains the generated graphs.

* **Red nodes** = Vertex Cover
* **Green nodes** = Other vertices

## Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Brute-Force-Vertex-Cover.git
```

Go to the project directory:

```bash
cd Brute-Force-Vertex-Cover
```

Run the program:

```bash
python vertex_cover.py
```

## Technologies Used

* Python
* NetworkX
* Matplotlib
* CSV
* Brute Force Algorithm

## Academic Work

This project was developed as part of a practical/assignment on algorithm design and analysis, specifically studying the computational complexity of the Vertex Cover problem.

