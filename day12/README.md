## Amazing Elegant Solution
[By Reddit user marchelzo](https://www.reddit.com/r/adventofcode/comments/3wh73d/day_12_solutions/cxw7oz1?utm_source=share&utm_medium=web2x&context=3)

```
from json import loads

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

print(n(loads(input())))
```

## My super kludge-y approach
