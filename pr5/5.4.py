from collections.abc import Hashable

lst = [1, 'a', [2, 2], (1, 2), {'x': 1}]
s = {i for i in lst if isinstance(i, Hashable)}
print(s)