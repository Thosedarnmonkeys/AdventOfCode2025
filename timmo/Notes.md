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

## Day 4

I think the only complication here really is the admin of checking all the right cells,
so I wrote myself a `Grid` class — my much-loved data structure from last year!
Though I decided it might be cheating to just copy last year's, so I've started again.
I may refactor in order to reuse in future puzzles, but we'll see...

## Day 5

### Part 1

I just brute-forced this, but could have made it more efficient by sorting the ranges
and then used some kind of binary search to get to a/the relevant range more quickly,
or (especially) to detect if there was no suitable range.
Though this might be quite fiddly if the ranges aren't consolidated.

### Part 2

This was fairly straightforward — sort the ranges by their start
and then work through them and combine any that overlap.
I was stuck for ages because I hadn't imagined that a range could be entirely contained
within another, and so was always keeping the end of the second range when combining them.

## Day 6

I had an annoying issue where my IDE was automatically stripping trailing whitespace
from the input, so I had to add that back as part of the input loading process.

### Part 1

I wasn't sure if I'd have to do something sophisticated like identifying the columns
which were spaces all the way down.
Happily, you could just split on spaces, though this gives extraneous empty strings
from where there were multiple spaces together, so you had to ignore these,
but simple enough.

### Part 2

I decided to transpose and reverse the whole input — effectively rotating it 90°.
This gave a list of strings like:
```
[
    '3829 ',
    ' 156*',
    '     ',
    '  35 ',
    '2454*',
    '     ',
    '  39 ',
    '  73 ',
    '2194+',
    ...
]
```

It was then quite straightforward to collate the problems by working down the list
accumulating integers as we go and checking the final character each time.
When this character was a symbol (`+` or `*`) instead of a space,
we save the accumulated list together with the symbol as a single problem.
These were then calculated in a separate pass subsequently.

## Day 7

### Part 1

My initial solution for this effectively recreated the annotated version of the map
given in the question; starting with each row as it was given in the input,
then working along it and updating it based on the state of the previous row,
and counting splits as they occurred.

Since strings are immutable and thus an individual character in a string
can't simply be updated,
I processed the input so each row was a list of \[single-character\] strings
rather than having each row as one string,
so that an individual position in the grid could be updated easily.

I later re-worked this after finding a better approach for part 2,
which I could adapt back to part 1 as well (see below).

### Part 2

My initial thought was that I'd need an algorithm following each possible beam path
and spawning off new execution branches to follow with each split.
I then realised we don't need to end up with a copy of each specific path,
but rather it suffices to count how many different beams would have reached a given position
(potentially having re-merged) and carry that total forward, including through future splits.

So I changed the representation I work with from the ASCII art version of the diagram
to a list of integers,
with each representing how many different beams have reached that position.
When processing a row, we initialise every position to 0,
and then can increment this when tracing beams down from the row above.
This also naturally handles when two splits end up 'on top of' each other,
or a split puts a beam into the same path as one coming from above.

To get the final answer, we simply sum the numbers in the last row.

### Part 1 (revisited)

Having found this approach, I copied it back to part 1 with two major changes:
1. We keep track of the number of splits we have processed
2. Since we don't care about the number of beams,
   we record beam 'state' as just `True`/`False`
   indicating whether or not a beam is present at that position.

## Day 8

### Part 1

There are 500,500 possible pairs of boxes, but I couldn't see any straightforward way
of solving this without brute-forcing it (I'm sure there are ways to optimise the search
in a more sophisticated solution).

I was worried that holding onto a copy of all the possible pairs with their distances
would explode my memory, so I'd considered using some kind of priority queue
with a size limit to only ever keep the shortest 1000 distances found so far.
But none of the queue data structures in the standard library looked quite right for this*,
and in any case I thought a more complex class might slow down execution.


So instead I structured my algorithm to find all the distances
for a given box and then combine that list with the current 1000 shortest distances
and then prune it back down to the 1000 shortest,
before moving on to the next box.

After finding the 1000 shortest distances,
I discard the distance data and just work with the box IDs
(these were just the index of the order in which their coordinates appear in the list).

For connecting the boxes into circuits I maintain a list of circuits, with
each being a `set` of the box IDs it contains, stored in a `dict` against a circuit ID.
A separate 'state' `dict` maps each box ID to the circuit ID it currently belongs to
(basically a pointer).
When merging two circuits, simply update the first circuit (set)
with the values from the second, remove the second from the circuits `dict`
and update the state of all the boxes in the second circuit
to now reference the first circuit ID.

### Part 2

It was very easy to adapt the approaches from part 1 for part 2.
Now we have no choice but to store the distances between all possible pairs,
but this didn't seem to be an issue memory-wise
(well, I didn't measure it but nothing ground to a halt
and the programme still ran very quickly).

The algorithm for connecting circuits is the same,
just that we check the number of circuits after each iteration
to see whether they've all been merged into one yet, at which point we return.
