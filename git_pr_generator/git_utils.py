import subprocess
from typing import Tuple

def run_git_command(command: str) -> str:
    """Run a git command and return its output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            check=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git command failed: {e.stderr}")

def get_current_branch() -> str:
    """Get the name of the current git branch."""
    return run_git_command("git branch --show-current")

def get_repo_name() -> str:
    """Get the name of the git repository."""
    return run_git_command("basename `git rev-parse --show-toplevel`")

def get_diff(current_branch: str, compare_branch: str) -> str:
    """Get the git diff between two branches."""
    return run_git_command(f"git diff {current_branch}..{compare_branch}")