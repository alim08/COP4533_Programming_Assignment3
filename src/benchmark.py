import time
import os
import matplotlib.pyplot as plt
from hvlcs import HVLCS_Solver

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # get root
    sizes = [25, 50, 100, 200, 400, 600, 800, 1000, 1500, 2000]
    times = []

    for i in range(1, 11):
        solver = HVLCS_Solver()
        solver.parse_input(os.path.join(project_root, f"tests/file_{i}.in"))  # make path to test file

        start = time.perf_counter()
        solver.solve()
        solver.reconstruct()
        end = time.perf_counter()

        times.append(end - start)

    plt.plot(sizes, times, marker='o')
    plt.title("HVLCS Runtime vs String Length")
    plt.xlabel("String Length (N)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)

    plt.savefig(os.path.join(project_root, "runtime_graph.png"))  # save graph
    print("Graph saved as runtime_graph.png")

if __name__ == "__main__":
    main()