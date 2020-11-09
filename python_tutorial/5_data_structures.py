# Remove item by index from list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]

# Tuples
t = 12345, 54321, 'hello!'
t[0] # 12345
t # (12345, 54321, 'hello!')

# Tuples are immutable, lists are mutable
x, y, z = t # sequence inpacking


# Sets
# A set is an unordered collection with no duplicate elements

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

a # unique letters in a
{'a', 'r', 'b', 'c', 'd'}

a - b # letters in a but not in b
{'r', 'd', 'b'}

a | b # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

a & b # letters in both a and b
{'a', 'c'}

a ^ b # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}


# Dictionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items(): # Iterating through key and value
    print(k, v)

# or
for i, v in enumerate(knights):
    print(i, v)