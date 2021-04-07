## Amazing Elegant Solution
Using recursion [by reddit user marchelzo](https://www.reddit.com/r/adventofcode/comments/3wh73d/day_12_solutions/cxw7oz1?utm_source=share&utm_medium=web2x&context=3)

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

## My super kludge-y redact-y approach

Find all the `:"red`'s.  Identify the dictionary `{}` its in and remove it.  Then apply solution from part 1.

i.e.

1. grep for the term `:"red`, you know that comes from a dictionary as opposed to a list
2. from there look backwards to find the first *unmatched* `{`
    - For example: `abc { {defg} :"red"...}` is contained in the dictionary opened by the leftmost `{` not the first `{` encountered when working backwards.
    - So I kept a bracket count as I went!  +1 for `{`, -1 for `}`.
    - Once I hit a `{` whenre the bracket count was 0 then that was the opening bracket
3. find the closing bracket `}` after the `:"red` using a similar approach
4. now you have the indexes of the brackets `{}` that contain the red.  I just replaced text betwen those positions with `X`'s 
    - This created a cool redacted-esque vibe
