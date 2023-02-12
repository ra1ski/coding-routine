# Sets
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

# Arrays
Static arrays - fixed in size

Dynamic - copy and build an array in a new location. Sometimes append is O(n) if underneath it creates only n blocks in memory.
Now it has to loop the array and copy then into the new location

# Pros & cons
Arrays:
- Fast llokup
- fast push/pop
- ordered

- slow inserts
- slow deletes
- fixed size if using static arrays