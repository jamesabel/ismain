import subprocess
import os
import sys

from ismain import is_main


def test_is_main():

    # not as "main"
    is_main_return = is_main()
    print(f"is_main_return={is_main_return}")
    assert not is_main_return

    # run this script as "main"
    cmd = [os.path.join("venv", "Scripts", "python.exe"), os.path.join("test_is_main", "test_is_main.py")]
    p = subprocess.run(cmd)
    is_main_return = bool(p.returncode)
    print(f"is_main_return={is_main_return}")
    assert is_main_return


if __name__ == "__main__":
    sys.exit(is_main())
