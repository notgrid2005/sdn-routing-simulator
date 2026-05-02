#!/usr/bin/env python3
"""Demo: SDN Routing Simulator with static and adaptive routing."""
from simulator.controller import SDNController


def main():
    controller = SDNController()

    # Build a network topology
    links = [
        ("S1", "S2", 1), ("S1", "S3", 4), ("S2", "S3", 2),
        ("S2", "S4", 5), ("S3", "S4", 1), ("S3", "S5", 3),
        ("S4", "S5", 2), ("S4", "S6", 3), ("S5", "S6", 1),
    ]
    controller.build_topology(links)

    print("=" * 50)
    print("SDN Routing Simulator")
    print("=" * 50)
    print(controller.topology)

    # Static routing
    print("\n--- Static Routing ---")
    controller.set_mode("static")
    path, cost = controller.install_path("S1", "S6")
    print(f"S1 -> S6: {' -> '.join(path)} (cost: {cost})")

    path, cost = controller.install_path("S1", "S5")
    print(f"S1 -> S5: {' -> '.join(path)} (cost: {cost})")

    # Adaptive routing (considers traffic load)
    print("\n--- Adaptive Routing (with traffic awareness) ---")
    controller.set_mode("adaptive")
    path, cost = controller.install_path("S2", "S6")
    print(f"S2 -> S6: {' -> '.join(path)} (cost: {cost:.1f})")

    path, cost = controller.install_path("S1", "S6")
    print(f"S1 -> S6: {' -> '.join(path)} (cost: {cost:.1f})")

    print("\n" + "=" * 50)
    controller.show_status()


if __name__ == "__main__":
    main()
