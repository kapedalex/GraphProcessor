# GraphProcessor

This project implements a program that processes an annotated metagraph and computes the attributes of its elements based on specified rules. The program takes input from a file that describes the metagraph's structure and the rules for attribute computation, then produces an output file listing the computed attributes for both vertices and edges.

## Features
- Input Handling: Reads the number of vertices and edges, their connections, and the rules for attribute computation from a structured text file.
- Attribute Computation: Supports various rules for attribute calculations:
- Direct assignment of attribute values.
- Reference copying from other vertices or edges.
- Functional calculations using minimum or multiplication of attributes from specified elements.
- Output Generation: Writes the computed attributes of vertices and edges to an output file in a readable format.
## Requirements
- Python 3.11

# Usage
Run the program via ```python main.py```

# Input file format

The first line contains two integers: the number of vertices (NV) and the number of edges (NE).
Followed by an empty line.
Next, list NE pairs of integers representing edges.
Followed by another empty line.
Finally, provide NV + NE rules for computing attributes

Example input:

```
8 8

1 2
2 4
3 4
4 5
6 5
5 7
7 6
7 8

0.1
2
0.2
min e 2 e 3
min e 4 e 5
0.5
0.3
e 8
v 1
* v 2 e 1
v 3
v 4
* v 6 e 7
v 5
v 7
v 7
```


