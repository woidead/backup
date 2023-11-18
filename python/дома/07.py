from itertools import count
from os import remove


nums = [1,2,3,3]

#s = {x for x in nums if nums.count(x) > 1}
for x in nums:
    if nums.count(x) == 2:
        print(x)
        break