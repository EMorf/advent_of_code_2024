import pathlib
path_to_folder: pathlib.Path = pathlib.Path(__file__).resolve().parent

# Duplicate elements are covered by the safe function
def monotonic(vals: list[int]):
    return vals == sorted(vals) or vals == sorted(vals, reverse=True)

def safe(vals: list[int]):
    for i in range(0, len(vals) - 1):
        a = abs(vals[i] - vals[i + 1])
        if a > 3 or a < 1:
            return False
    return True

c = 0
with open(pathlib.Path(path_to_folder / "./data.txt"), "r") as file:
    for line in file:
        line = line.split()
        line = [int(x) for x in line]
        for id in range(len(line)):
            cand = [x for i, x in enumerate(line) if i != id]
            if monotonic(cand) and safe(cand):
                c += 1
                break
        
print(c)