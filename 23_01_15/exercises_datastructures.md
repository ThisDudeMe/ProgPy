### Exercises on Sets

1. **Basic:** Create a set containing numbers from 1 to 10. Then add a new number to the set and remove a number from the set.
2. **Intermediate:** Given two sets, find their union, intersection, difference, and symmetric difference. Look up what these terms mean.
3. **Advanced:** Write a function that takes a list of words and returns the number of distinct words that appear more than once.

### Exercises on Tuples

1. **Basic:** Create a tuple with different data types (integer, float, string) and print each value with its type.
2. **Intermediate:** Write a Python program to convert a list of tuples into a dictionary.
3. **Advanced:** Implement a function that takes a list of tuples (each tuple consists of two integers) and returns the tuple with the largest product.

### Exercises on Counter

1. **Basic:** Use Counter to count the occurrences of each character in a given string.
2. **Intermediate:** Given a list of names, use Counter to find the name that appears the most.
3. **Advanced:** Write a function using Counter that takes a string and returns the first non-repeating character in it.

### Exercises on Deque

1. **Basic:** Implement a queue using deque and perform enqueue and dequeue operations.
2. **Intermediate:** Write a function that uses a deque to find the first unique character in a sequence of characters.

Sure, let's go through the solutions for each of the exercises on Sets, Tuples, Counter, and deque.

### Solutions for Sets Exercises

1. **Basic:**

   ```python
   # Create a set and perform add and remove operations
   my_set = set(range(1, 11))
   my_set.add(11)
   my_set.remove(2)
   print(my_set)
   ```

2. **Intermediate:**

   ```python
   # Operations on two sets
   set1 = {1, 2, 3, 4, 5}
   set2 = {4, 5, 6, 7, 8}

   union = set1 | set2
   intersection = set1 & set2
   difference = set1 - set2
   symmetric_difference = set1 ^ set2

   print("Union:", union)
   print("Intersection:", intersection)
   print("Difference:", difference)
   print("Symmetric Difference:", symmetric_difference)
   ```

3. **Advanced:**

   ```python
   # Function to count words appearing more than once
   def count_repeated_words(word_list):
       from collections import Counter
       word_count = Counter(word_list)
       return sum(1 for word, count in word_count.items() if count > 1)

   words = ["apple", "banana", "apple", "orange", "banana", "grape"]
   print(count_repeated_words(words))
   ```

### Solutions for Tuples Exercises

1. **Basic:**

   ```python
   # Tuple with different data types
   my_tuple = (1, 3.14, 'Python')
   for item in my_tuple:
       print(item, type(item))
   ```

2. **Intermediate:**

   ```python
   # Convert list of tuples to a dictionary
   list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
   dict_from_tuples = dict(list_of_tuples)
   print(dict_from_tuples)
   ```

3. **Advanced:**

   ```python
   # Function to find the tuple with the largest product
   def max_product(tuples_list):
       return max(tuples_list, key=lambda pair: pair[0] * pair[1])

   tuples_list = [(1, 2), (2, 3), (4, 5), (6, 7)]
   print(max_product(tuples_list))
   ```

### Solutions for Counter Exercises

1. **Basic:**

   ```python
   # Counting characters in a string
   from collections import Counter
   char_count = Counter("mississippi")
   print(char_count)
   ```

2. **Intermediate:**

   ```python
   # Find the most common name
   from collections import Counter
   names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]
   common_name = Counter(names).most_common(1)[0][0]
   print(common_name)
   ```

3. **Advanced:**

   ```python
   # First non-repeating character
   def first_non_repeating_char(str):
       char_count = Counter(str)
       for char in str:
           if char_count[char] == 1:
               return char
       return None

   print(first_non_repeating_char("aabbccdeeffg"))
   ```

### Solutions for Deque Exercises

1. **Intermediate:**

   ```python
   # Queue implementation using deque
   queue = deque()
   queue.append('item1')  # Enqueue
   queue.append('item2')
   print("Queue after enqueues:", queue)
   queue.popleft()  # Dequeue
   print("Queue after dequeue:", queue)
   ```

2. **Advanced:**

   ```python
   # First unique character in a stream
   def first_unique_char(stream):
       d = deque()
       repeats = set()
       for char in stream:
           if char not in repeats:
               if char in d:
                   d.remove(char)
                   repeats.add(char)
               else:
                   d.append(char)
           if d:
               print("First unique character:", d[0])
           else:
               print("No unique character.")

   first_unique_char("aabcdbef")
   ```

