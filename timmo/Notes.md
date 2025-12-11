# TimMo's notes

## Day 1

### Part 2

Roughly speaking, we can detect the number of 0s hit by counting the multiples of 100
we've passed with the initial 'raw' result (before applying mod 100).
When rotating right, this can be found using floor division with 100.

When rotating left, we can use floor division with -100
to get the absolute value of the result directly (ie a positive number).
But we will always under-count by 1, as this doesn't include crossing 0 itself
(since we always start in the positive range 0-99).
The exception to this is when we start _on_ 0,
as we will have already counted hitting this zero in the previous rotation.

We can anticipate this under-counting and adjust our zeros count in advance,
and then let the code fall through as normal:

```python
case "L":
    # anticipate under-counting (unless starting on 0) and compensate
    if dial != 0:
        zeros += 1
    dial = dial - distance
    if dial <= 0:
        zeros += dial // -100
```

Alternatively, when we know we're rotating left (towards negative numbers),
we can adjust the starting point to the equivalent negative value,
to make the negative case symmetrical with the positive,
such that passing a _negative_ multiple of 100 is equivalent to hitting 0
(and staying in the range -99 to 0 means we haven't).

Since the dial will always end on a value <= 0, we can remove this condition
when incrementing the zeros count.

```python
case "L":
    # anticipate under-counting (unless starting on 0) and compensate
    if dial != 0:
        dial -= 100
    dial = dial - distance
    zeros += dial // -100
```

We can also exploit the behaviour of the modulo (`%`) operator with negative values,
which means that `dial %= -100` is equivalent to the first two lines in the block, ie:

- `0 %= -100 == 0`
- `1 %= -100 == 1 - 100 == -99`
- `99 %= -100 == 99 - 100 == -1`

to give:

```python
case "L":
    dial %= -100
    dial = dial - distance
    zeros += dial // -100
```

This gives a pleasing symmetry to the two cases, after the initial adjustment to the negative case:

```python
for direction, distance in rotations:
    match direction:
        case "L":
            dial %= -100
            dial = dial - distance
            zeros += dial // -100
        case "R":
            dial = dial + distance
            zeros += dial // 100
        case _:
            raise ValueError(f"Unknown direction: '{direction}'")
    dial %= 100
```

### Taking it too far

...actually, we can bring the final `dial %= 100` inside the `R` case,
as the modulo operation in the `L` case will override whatever we do there anyway:

```python
for direction, distance in rotations:
    match direction:
        case "L":
            dial %= -100
            dial = dial - distance
            zeros += dial // -100
        case "R":
            dial %= 100
            dial = dial + distance
            zeros += dial // 100
        case _:
            raise ValueError(f"Unknown direction: '{direction}'")
```

We can then see a complete symmetry, which we can use to collapse the whole thing down:

```python
for direction, distance in rotations:
    match direction:
        case "L":
            sign = -1
        case "R":
            sign = 1
        case _:
            raise ValueError(f"Unknown direction: '{direction}'")
        
    dial %= sign * 100
    dial = dial + sign * distance
    zeros += dial // (sign * 100)
```

And dispensing with error-checking and other niceties:

```python
for direction, distance in rotations:
    sign = -1 if direction == "L" else 1        
    dial %= sign * 100
    dial = dial + sign * distance
    zeros += dial // (sign * 100)
```

## Day 3

### Part 1

The maximum two-digit number can be found by first identifying the highest battery
(ie maximising the tens digit),
and then finding the highest digit to the right of this.
There is a special case when the highest battery is the right-most battery,
in which case we need to find the second-highest battery to use at the tens instead,
and have the units as the highest battery (ie the right-most one we just found).

### Part 2

Off-by-one errors abound!

To generalise from the two-digit case: when selecting each digit in turn,
we choose the highest one available while making sure we leave enough digits
to fill up subsequent positions; ie, we don't search too far to the right.
So when constructing 12-digit numbers from an array of 100,
for the first digit we don't look in the final 11, ie we search within 1st to 89th.
For the second digit we search to the right of wherever we found the first one up to the 90th
(leaving 10 for future digits), and so on.
