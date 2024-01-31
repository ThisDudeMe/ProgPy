# Tuples in Python
# ----------------
# Tuples are immutable sequences, meaning once defined, their values cannot be changed.
# They are used to store a collection of items, which can be of different types.
# Example of creating and using a tuple:

my_tuple = (1, 2, "Hello", 3.14)
print("Tuple:", my_tuple)
print("First Element:", my_tuple[0])  # Accessing the first element

# Sets in Python
# --------------
# Sets are collections of unique elements. They automatically remove duplicates.
# They are mutable, but the elements contained must be immutable and hashable.
# Example of creating and using a set:

my_set = {1, 2, 3, 4, 2, 3}
print("Set:", my_set)  # Duplicates (2, 3) are removed automatically
my_set.add(5)         # Adding an element to the set
print("Set after adding 5:", my_set)

# Counter from collections
# ------------------------
# Counter is a subclass of dict for counting hashable objects.
# It's a collection where elements are stored as keys and their counts are stored as values.
# Example of creating and using a Counter:

from collections import Counter
word_count = Counter("mississippi")
print("Word Count:", word_count)
print("Count for 's':", word_count['s'])  # Count of how many times 's' appears

# Deque from collections
# ----------------------
# Deque (Double-Ended Queue) supports adding and removing elements from either end.
# It's more efficient than list for push/pop operations on both ends.
# Example of creating and using a deque:

from collections import deque
my_deque = deque([1, 2, 3])
my_deque.appendleft(0)  # Add 0 to the left side of the deque
my_deque.append(4)      # Add 4 to the right side of the deque
print("Deque:", my_deque)
print("Popping from right:", my_deque.pop())       # Pops 4
print("Popping from left:", my_deque.popleft())    # Pops 0
print("Deque after pops:", my_deque)