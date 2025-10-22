from setuptools import setup
from pathlib import Path
import re


def read_version():
    p = Path(__file__).parent / "ismain" / "__init__.py"
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]", text, re.M)
    return m.group(1) if m else "0.0.0"


def read_readme():
    p = Path(__file__).parent / "README.md"
    return p.read_text(encoding="utf-8") if p.exists() else ""


setup(
    name="ismain",
    version=read_version(),
    long_description=read_readme(),
    long_description_content_type="text/markdown",
)
