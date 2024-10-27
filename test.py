from main import create_pr


def test_valid_diff_creates_pr():
    test_diff = "diff --git a/test.py b/test.py\nindex 1234567890..abcdef1234 (modified)\n--- a/test.py\n+++ b/test.py\n@@ -1,1 +1,2 @@\n+test"
    test_repo_name = "test-repo"
    test_branch_name = "test-branch"
    assert create_pr(test_diff, test_repo_name, test_branch_name) is not None
