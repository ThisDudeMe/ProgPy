## Basic Exercises

1. **Countdown**
    - Write a class Countdown that takes number n and prints all numbers from n to zero when iterated upon.

2. **Create a Simple Iterator**

   - Write a class `SquareIterator` that takes a number `n` and iterates from 1 to `n`, returning the square of each number during each iteration.

3. **Using Built-in Iterators**

   - Use the `iter()` and `next()` functions to manually iterate over a list of your choice. Handle the `StopIteration` exception gracefully.


### Intermediate Exercises

4. **Custom Range Iterator**

   - Create a custom iterator `CustomRange` that behaves like the built-in range function.

5. **Iterate Over Two Lists Concurrently**

   - Write an iterator using `zip()` that takes two lists of equal length and iterates over them concurrently, returning tuples containing elements from both lists.

6. **Lazy Evaluation of Infinite Series**
    - Implement a generator `partial_sums` that lazily evaluates the partial sums of an infinite series. For example, given the series of natural numbers (1, 2, 3, ...), it should yield 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4), and so on.



### Advanced Exercises

7. **Cycling Iterator**

   - Using `itertools.cycle()`, create an iterator that endlessly cycles through a given list. For example, cycling through `[1, 2, 3]` would produce `1, 2, 3, 1, 2, 3, ...` indefinitely.

8. **Chained Iteration**

   - Create a generator function `chain_iterables` that takes multiple iterables (like lists, sets, etc.) and iterates through them one after the other.

9. **Windowed Iterator**
   - Write a generator `windowed_seq` that takes an iterable and a window size `n` and yields tuples of length `n` sliding over the iterable. For example, `windowed_seq('ABCDE', 3)` would yield `('A', 'B', 'C')`, then `('B', 'C', 'D')`, and so on.


## Solutions
### 1.
See demonstration.

### 2. Create a Simple Iterator (SquareIterator)

```python
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            result = self.i ** 2
            self.i += 1
            return result
        else:
            raise StopIteration

# Example Usage
for square in SquareIterator(5):
    print(square)
```

### 3. Using Built-in Iterators

```python
my_list = [10, 20, 30]
my_iter = iter(my_list)

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
```

### 4. Custom Range Iterator

```python
class CustomRange:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current <= self.end) or (self.step < 0 and self.current >= self.end):
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration

# Example Usage
for i in CustomRange(5, 15, 2):
    print(i)
```

### 5. Iterate Over Two Lists Concurrently

```python
class ParallelIterator:
    def __init__(self, list1, list2):
        # Ensure both lists are of the same length
        if len(list1) != len(list2):
            raise ValueError("Lists must be of the same length")
        self.list1 = list1
        self.list2 = list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list1):
            result = (self.list1[self.index], self.list2[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

# Example Usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num, char in ParallelIterator(list1, list2):
    print(num, char)
```

### 6. Lazy Evaluation of Infinite Series (partial_sums)

```python
def partial_sums():
    total, n = 0, 1
    while True:
        total += n
        yield total
        n += 1

# Example Usage
sums = partial_sums()
for _ in range(5):
    print(next(sums))
```


### 7. Cycling Iterator

```python
class CyclingIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.lst:  # Check if the list is empty
            raise StopIteration

        value = self.lst[self.index]
        self.index = (self.index + 1) % len(self.lst)  # Cycle the index
        return value

# Example Usage
cycler = CyclingIterator([1, 2, 3])
for i in range(10):
    print(next(cycler))

```

### 8. Chained Iteration (chain_iterables)

```python
def chain_iterables(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# Example Usage
for item in chain_iterables([1, 2], ['a', 'b']):
    print(item)
```

### 9. Windowed Iterator (windowed_seq)

```python
def windowed_seq(iterable, n):
    it = iter(iterable)
    win = []
    for item in it:
        win.append(item)
        if len(win) == n:
            yield tuple(win)
            win.pop(0)

# Example Usage
for window in windowed_seq('ABCDE', 3):
    print(window)
```
