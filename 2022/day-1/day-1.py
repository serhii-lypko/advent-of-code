import os
from functools import reduce
import heapq

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "day-1.txt")

with open(file_path, "r") as file:
    res_heap = []
    curr_group_sum = 0

    line = file.readline()

    while line:
        if line.strip() == "":
            heapq.heappush(res_heap, curr_group_sum)
            curr_group_sum = 0
        else:
            number = int(line)
            curr_group_sum += number

        line = file.readline()

    heapq.heappush(res_heap, curr_group_sum)

    largest = heapq.nlargest(3, res_heap)
    res = sum(largest)

    print(res)
