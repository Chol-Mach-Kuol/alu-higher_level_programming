# Python - Everything is Object

This project explores how Python handles objects, identity, mutability, and references.

## Key Concepts

- Every value in Python is an object with an identity (`id()`), type (`type()`), and value
- `==` checks value equality; `is` checks identity (same object in memory)
- **Immutable types**: int, float, str, tuple, frozenset, bytes
- **Mutable types**: list, dict, set, bytearray
- CPython caches small integers (-5 to 256) and the empty tuple as singletons
- Variables are references; assignment binds a name to an object
- Mutable objects passed to functions can be modified in place
