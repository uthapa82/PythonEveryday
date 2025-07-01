Managing collisions with linear probing. 
-1 for empty slots

-2 for deleted slots

Key Methods:
hash(x): Computes the hash index using modulo — x % capacity.

search(x): Linearly probes until:

It finds x → return True

It hits an empty slot (-1) → return False

It loops back to start → return False

insert(x):

Checks if the hash table is full or if x already exists

Finds a slot (-1 or -2) and inserts

Increments size

remove(x):

Probes for x, if found → mark as deleted (-2)

If not found → return False