import subprocess
import os
import sys

from ismain import is_main, __version__, __author__


def test_is_main():

    # not as "main"
    is_main_return = is_main()
    print(f"is_main_return={is_main_return}")
    assert not is_main_return

    assert __version__ is not None
    assert __author__ is not None

    # run this script as "main" if not in CI
    if os.getenv("CI"):
        print("Skipping subprocess test in CI environment")
        return
    cmd = [os.path.join("venv", "Scripts", "python.exe"), os.path.join("test_is_main", "test_is_main.py")]
    p = subprocess.run(cmd)
    is_main_return = bool(p.returncode)
    print(f"is_main_return={is_main_return}")
    assert is_main_return


if __name__ == "__main__":
    sys.exit(is_main())
