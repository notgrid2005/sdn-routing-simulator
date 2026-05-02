"""SDN Controller that manages routing and flow installation."""
from .topology import Topology
from .routing import dijkstra, adaptive_route, FlowTable


class SDNController:
    def __init__(self):
        self.topology = Topology()
        self.flow_table = FlowTable()
        self.traffic = {}
        self.mode = "static"

    def build_topology(self, links):
        nodes = set()
        for n1, n2, w in links:
            nodes.add(n1)
            nodes.add(n2)
        for n in nodes:
            self.topology.add_node(n)
        for n1, n2, w in links:
            self.topology.add_link(n1, n2, w)

    def set_mode(self, mode):
        self.mode = mode

    def compute_path(self, src, dst):
        graph = self.topology.get_graph()
        if self.mode == "adaptive":
            path, cost = adaptive_route(graph, src, dst, self.traffic)
        else:
            path, cost = dijkstra(graph, src, dst)
        return path, cost

    def install_path(self, src, dst):
        path, cost = self.compute_path(src, dst)
        for i in range(len(path) - 1):
            self.flow_table.install_rule(path[i], dst, f"fwd:{path[i+1]}")
            link = tuple(sorted([path[i], path[i+1]]))
            self.traffic[link] = self.traffic.get(link, 0) + 1
        return path, cost

    def show_status(self):
        print(self.topology)
        print(self.flow_table)
        print(f"Traffic: {self.traffic}")
