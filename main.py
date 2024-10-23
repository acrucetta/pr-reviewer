"""
Find the .git in the current working directory.
Ask the user for the branch they want to compare
and the branch they're merging to.

Evaluate all the changes and write a PR explaining:
1. What to review first
2. Any tests if applicable
3. Archiectural diagram of the changes

Optional:
- Improvements on the code: security, speed, etc...
"""

import os
import sys
import subprocess

def main(curr_branch : str, compare_branch : str):
    diffs = subprocess.run(f"git diff {curr_branch}..{compare_branch}", shell=True, capture_output=True)
    print(diffs)
    return ""

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0],args[1])

