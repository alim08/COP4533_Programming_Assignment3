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

    def solve(self):
        m = len(self.A)
        n = len(self.B)
        
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.A[i-1] == self.B[j-1]:
                    char_val = self.values.get(self.A[i-1], 0)
                    self.dp[i][j] = self.dp[i-1][j-1] + char_val
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])
                    
        return self.dp[m][n]

    def reconstruct(self):  # fixed indentation bug
        i = len(self.A)
        j = len(self.B)
        subsequence = []
        
        while i > 0 and j > 0:
            if self.A[i-1] == self.B[j-1]:
                subsequence.append(self.A[i-1])
                i -= 1
                j -= 1
            elif self.dp[i-1][j] > self.dp[i][j-1]:
                i -= 1
            else:
                j -= 1
                
        # The sequence is built backwards, so reverse it
        return "".join(reversed(subsequence))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/hvlcs.py <input_file>")
        sys.exit(1)
        
    solver = HVLCS_Solver()
    solver.parse_input(sys.argv[1])
    
    max_val = solver.solve()
    optimal_seq = solver.reconstruct()
    
    print(max_val)
    print(optimal_seq)