import pathlib
from collections import deque
from heapq import heapify, heappush, heappop


path_to_folder: pathlib.Path = pathlib.Path(__file__).resolve().parent

# Split data into two lists, corresponding to the left and right column, with relevant names
left: list[int] = []
right: list[int] = []
with open(pathlib.Path(path_to_folder / "./data.txt"), "r") as file:

    for line in file:
        line = line.split()  # type: ignore
        left.append(int(line[0]))
        right.append(int(line[1]))

# Sanity check
assert len(left) == len(right)

# Convert to a heap, as it has an optimal removal time complexity
heapify(left)
heapify(right)
distance: int = 0


while left:
    min_left = heappop(left)
    min_right = heappop(right)
    distance += abs(min_left - min_right)

print(distance)
