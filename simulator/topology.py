"""Network topology builder for SDN simulation."""

class Node:
    def __init__(self, name, node_type="switch"):
        self.name = name
        self.type = node_type
        self.links = {}

    def add_link(self, neighbor, weight=1):
        self.links[neighbor.name] = weight

    def __repr__(self):
        return f"Node({self.name})"


class Topology:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, node_type="switch"):
        node = Node(name, node_type)
        self.nodes[name] = node
        return node

    def add_link(self, n1, n2, weight=1):
        self.nodes[n1].add_link(self.nodes[n2], weight)
        self.nodes[n2].add_link(self.nodes[n1], weight)

    def get_neighbors(self, name):
        return self.nodes[name].links

    def get_graph(self):
        return {n: node.links for n, node in self.nodes.items()}

    def __str__(self):
        lines = []
        for name, node in self.nodes.items():
            links = ", ".join(f"{k}(w={v})" for k, v in node.links.items())
            lines.append(f"  {name} -> [{links}]")
        return "Topology:\n" + "\n".join(lines)
