from collections import defaultdict
from typing import Dict

arr = ["a", "a", "b", "c", "c", "c"]

counter: Dict[str, int] = defaultdict(int)
for e in arr:
    counter[e] += 1

sorted_dict = sorted(counter.items(), key=lambda x: x[1])
print(dict(counter))
print(dict(sorted_dict))
