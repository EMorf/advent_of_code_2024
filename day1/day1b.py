import pathlib
from collections import defaultdict
from heapq import heapify, heappop


path_to_folder: pathlib.Path = pathlib.Path(__file__).resolve().parent

left : defaultdict[int,int] = defaultdict(int)
right : defaultdict[int,int] = defaultdict(int)
with open(pathlib.Path(path_to_folder / "./data.txt"), "r") as file:

    for line in file:
        line = line.split() # type: ignore
        left[int(line[0])] += 1
        right[int(line[1])] += 1

similarity_score = 0
for element in left:
    similarity_score += right[element] * left[element] * element

print(similarity_score)
