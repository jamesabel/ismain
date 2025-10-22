[![PyPI version](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)  <!-- PyPI current version -->
[![PyPI downloads](https://img.shields.io/pypi/dm/PACKAGE)](https://pypi.org/project/PACKAGE/)  <!-- PyPI monthly downloads -->
[![Codecov](https://codecov.io/gh/OWNER/REPO/branch/BRANCH/graph/badge.svg)](https://codecov.io/gh/OWNER/REPO)  <!-- Codecov coverage badge -->
[![License](https://img.shields.io/github/license/OWNER/REPO)](https://github.com/OWNER/REPO/blob/BRANCH/LICENSE)  <!-- License -->
[![Dependabot status](https://img.shields.io/badge/dependabot-up%20to%20date-brightgreen)](https://github.com/OWNER/REPO/security/dependabot)  <!-- Dependabot indicator (manual badge) -->

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
