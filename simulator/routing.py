"""Routing algorithms: Dijkstra (static) and adaptive load-based."""
import heapq
from collections import defaultdict


def dijkstra(graph, source, dest):
    dist = {n: float("inf") for n in graph}
    dist[source] = 0
    prev = {n: None for n in graph}
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == dest:
            break
        for v, w in graph[u].items():
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
    path = []
    node = dest
    while node:
        path.append(node)
        node = prev[node]
    return list(reversed(path)), dist[dest]


def adaptive_route(graph, source, dest, traffic):
    """Route considering current traffic load on links."""
    adjusted = {}
    for n in graph:
        adjusted[n] = {}
        for nb, w in graph[n].items():
            link = tuple(sorted([n, nb]))
            load = traffic.get(link, 0)
            adjusted[n][nb] = w * (1 + load * 0.5)
    return dijkstra(adjusted, source, dest)


class FlowTable:
    def __init__(self):
        self.rules = defaultdict(list)

    def install_rule(self, switch, match, action):
        self.rules[switch].append({"match": match, "action": action})

    def lookup(self, switch, packet_dest):
        for rule in self.rules[switch]:
            if rule["match"] == packet_dest:
                return rule["action"]
        return None

    def __str__(self):
        lines = ["Flow Table:"]
        for sw, rules in self.rules.items():
            lines.append(f"  {sw}:")
            for r in rules:
                lines.append(f"    match={r['match']} -> {r['action']}")
        return "\n".join(lines)
