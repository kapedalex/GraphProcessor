from typing import List, Optional


class GraphProcessor:
    def __init__(self, NV: int, NE: int, edges: list[tuple[int, int]], rules: list[str]):
        """
        Initializes the class with the number of vertices (NV), edges (NE), a list of edges,
        and rules.
        """
        self.NV = NV
        self.NE = NE
        self.edges = edges
        self.rules = rules
        self.attributes: List[Optional[float]] = [None] * (NV + NE)

    @staticmethod
    def read_input(filename: str) -> tuple[int, int, list[tuple[int]], list[str]]:
        """
        Reads input data from a file.
        Returns the number of vertices (NV), number of edges (NE), a list of edges, and a list of rules.
        """
        with open(filename, 'r') as f:
            NV, NE = map(int, f.readline().strip().split())
            f.readline()

            edges = [tuple(map(int, f.readline().strip().split())) for _ in range(NE)]
            f.readline()

            rules = [f.readline().strip() for _ in range(NV + NE)]

        return NV, NE, edges, rules

    def compute_attribute(self, i: int) -> float:
        """
        Lazily computes attributes for a vertex or edge with index i.
        """
        if self.attributes[i] is not None:
            return self.attributes[i]

        rule = self.rules[i].split()

        if len(rule) == 1:
            self.attributes[i] = float(rule[0])
        elif len(rule) == 2:
            ref_type, ref_index = rule[0], int(rule[1]) - 1
            if ref_type == 'v':
                self.attributes[i] = self.compute_attribute(ref_index)
            elif ref_type == 'e':
                self.attributes[i] = self.compute_attribute(self.NV + ref_index)
        elif len(rule) == 5:
            func, ref1_type, ref1_index, ref2_type, ref2_index = (
                rule[0], rule[1], int(rule[2]) - 1, rule[3], int(rule[4]) - 1
            )

            val1 = self.compute_attribute(ref1_index if ref1_type == 'v' else self.NV + ref1_index)
            val2 = self.compute_attribute(ref2_index if ref2_type == 'v' else self.NV + ref2_index)

            if func == 'min':
                self.attributes[i] = min(val1, val2)
            elif func == '*':
                self.attributes[i] = val1 * val2

        return self.attributes[i]

    def process_rules(self) -> list[float]:
        """
        Processes rules and computes all attributes of vertices and edges.
        Returns a list of computed attributes.
        """
        for i in range(self.NV + self.NE):
            self.compute_attribute(i)
        return self.attributes

    @staticmethod
    def write_output(filename: str, NV: int, NE: int, attributes: list) -> None:
        """
        Writes the attributes of vertices and edges to a file.
        """
        with open(filename, 'w') as f:
            for i in range(NV):
                f.write(f'{attributes[i]:.2f}\n')

            for i in range(NV, NV + NE):
                f.write(f'{attributes[i]:.2f}\n')
