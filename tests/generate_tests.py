import random
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
tests_dir = os.path.join(project_root, "tests")  # fixed nested test file

def generate_file(filename, length):
    alphabet = ['a', 'b', 'c', 'd', 'e']   #intialize alphabet
    values = {char: random.randint(1, 10) for char in alphabet}  # assign random number

    string_a = "".join(random.choices(alphabet, k=length))
    string_b = "".join(random.choices(alphabet, k=length))

    os.makedirs(os.path.dirname(filename), exist_ok=True)  # make directory
    with open(filename, 'w') as f:
        f.write(f"{len(alphabet)}\n")  # num of characters in alphabet
        for char, val in values.items():  # each char and value
            f.write(f"{char} {val}\n")

        f.write(f"{string_a}\n")
        f.write(f"{string_b}\n")

if __name__ == "__main__":
    sizes = [25, 50, 100, 200, 400, 600, 800, 1000, 1500, 2000]  # tests size
    for i, size in enumerate(sizes):
        filepath = os.path.join(tests_dir, f"file_{i + 1}.in")
        generate_file(filepath, size)
    print("Generated 10 nontrivial test files in tests/")