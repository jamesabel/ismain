
# Installation

`pip install ismain`

# Usage

```
from ismain import is_main

#
# Same as:
# 
#     if "__name__" == __main__:
# 
# ... but more readable.
#
if is_main():
    print("Hello from main.")
```
