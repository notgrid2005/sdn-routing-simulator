# 🌐 SDN Routing Simulator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A Software-Defined Networking (SDN) routing simulator with static (Dijkstra) and adaptive (traffic-aware) routing algorithms.

## Features
- Network topology builder
- Dijkstra shortest path routing
- Adaptive routing with traffic load awareness
- Flow table management
- SDN controller simulation

## Quick Start
```bash
python main.py
```

## Project Structure
```
sdn-routing-simulator/
├── simulator/
│   ├── __init__.py
│   ├── topology.py    # Network graph builder
│   ├── routing.py     # Dijkstra + Adaptive algorithms
│   └── controller.py  # SDN Controller logic
├── main.py
└── README.md
```
