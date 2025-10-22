[![PyPI version](https://img.shields.io/pypi/v/ismain.svg)](https://pypi.org/project/ismain/)  <!-- PyPI current version -->
[![PyPI downloads](https://img.shields.io/pypi/dm/ismain)](https://pypi.org/project/ismain/)  <!-- PyPI monthly downloads -->
[![Codecov](https://codecov.io/gh/jamesabel/ismain/branch/main/graph/badge.svg)](https://codecov.io/gh/jamesabel/ismain)
[![License](https://img.shields.io/github/license/jamesabel/ismain)](https://github.com/OWNER/REPO/blob/master/LICENSE)  <!-- License -->
[![Dependabot status](https://img.shields.io/badge/dependabot-up%20to%20date-brightgreen)](https://github.com/jamesabel/ismain/security/dependabot)  <!-- Dependabot indicator (manual badge) -->

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
