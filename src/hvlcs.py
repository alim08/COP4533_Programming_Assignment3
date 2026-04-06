import sys

class HVLCS_Solver:
    def __init__(self):
        self.values = {}
        self.A = ""
        self.B = ""

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
        if not lines:
            return
            
        K = int(lines[0])
        
        for i in range(1, K + 1):
            char, val = lines[i].split()
            self.values[char] = int(val)
            
        self.A = lines[K + 1]
        self.B = lines[K + 2]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/hvlcs.py <input_file>")
        sys.exit(1)
        
    solver = HVLCS_Solver()
    solver.parse_input(sys.argv[1])
    print(f"Loaded strings A (len {len(solver.A)}) and B (len {len(solver.B)})")