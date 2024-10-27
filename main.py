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
import anthropic


SYSTEM_PROMPT = """
You are tasked with creating a pull request based on a git diff, following best practices and effectively communicating the changes to your team. This is crucial for maintaining a smooth code review process and ensuring that your teammates understand the purpose and impact of your changes.

You will be provided with the following information:
<git_diff>
{{GIT_DIFF}}
</git_diff>

<repo_name>{{REPO_NAME}}</repo_name>

<branch_name>{{BRANCH_NAME}}</branch_name>

Follow these steps to create an effective pull request:

1. Analyze the git diff:
   - Identify the files that have been changed
   - Determine the nature of the changes (e.g., bug fix, feature addition, refactoring)
   - Note any significant additions, deletions, or modifications

2. Create a concise yet descriptive pull request title:
   - Start with a prefix that indicates the type of change (e.g., [FIX], [FEATURE], [REFACTOR])
   - Briefly summarize the main purpose of the changes
   - Keep the title under 72 characters if possible

3. Write a comprehensive pull request description:
   - Provide a high-level overview of the changes
   - Explain the motivation behind the changes
   - List the specific modifications made
   - Mention any potential impact on other parts of the codebase
   - Include any necessary setup or testing instructions

4. Follow these best practices for pull requests:
   - Keep the changes focused and atomic (i.e., address one concern per pull request)
   - Ensure the code follows the project's style guide and conventions
   - Include relevant unit tests or update existing tests if necessary
   - Mention any related issues or pull requests
   - Tag relevant team members for review if known

5. Format your output as follows:
   <pull_request>
   <title>Your PR title here</title>
   <description>
   Your PR description here, formatted with Markdown for better readability
   </description>
   </pull_request>

Remember to be clear, concise, and informative in your pull request. Your goal is to make it easy for your team to understand and review your changes effectively.
"""


def main(compare_branch: str):
    # Get the current branch name
    curr_branch = subprocess.run(
        "git branch --show-current", shell=True, capture_output=True, check=True
    ).stdout.decode("utf-8")

    # Get the repo name
    repo_name = subprocess.run(
        "basename `git rev-parse --show-toplevel`",
        shell=True,
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")

    # Get the diff
    diffs = subprocess.run(
        f"git diff {curr_branch}..{compare_branch}",
        shell=True,
        capture_output=True,
        check=True,
    )
    return create_pr(diffs.stdout.decode("utf-8"), repo_name, curr_branch)


def create_pr(diff: str, repo_name: str, branch_name: str):
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
    )
    system_prompt = SYSTEM_PROMPT.replace("{{GIT_DIFF}}", diff)
    system_prompt = system_prompt.replace("{{REPO_NAME}}", repo_name)
    system_prompt = system_prompt.replace("{{BRANCH_NAME}}", branch_name)
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are tasked with creating a pull request based on a git diff, following best practices and effectively communicating the changes to your team. This is crucial for maintaining a smooth code review process and ensuring that your teammates understand the purpose and impact of your changes.\n\nYou will be provided with the following information:\n<git_diff>\n{{GIT_DIFF}}\n</git_diff>\n\n<repo_name>{{REPO_NAME}}</repo_name>\n\n<branch_name>{{BRANCH_NAME}}</branch_name>\n\nFollow these steps to create an effective pull request:\n\n1. Analyze the git diff:\n   - Identify the files that have been changed\n   - Determine the nature of the changes (e.g., bug fix, feature addition, refactoring)\n   - Note any significant additions, deletions, or modifications\n\n2. Create a concise yet descriptive pull request title:\n   - Start with a prefix that indicates the type of change (e.g., [FIX], [FEATURE], [REFACTOR])\n   - Briefly summarize the main purpose of the changes\n   - Keep the title under 72 characters if possible\n\n3. Write a comprehensive pull request description:\n   - Provide a high-level overview of the changes\n   - Explain the motivation behind the changes\n   - List the specific modifications made\n   - Mention any potential impact on other parts of the codebase\n   - Include any necessary setup or testing instructions\n\n4. Follow these best practices for pull requests:\n   - Keep the changes focused and atomic (i.e., address one concern per pull request)\n   - Ensure the code follows the project's style guide and conventions\n   - Include relevant unit tests or update existing tests if necessary\n   - Mention any related issues or pull requests\n   - Tag relevant team members for review if known\n\n5. Format your output as follows:\n   <pull_request>\n   <title>Your PR title here</title>\n   <description>\n   Your PR description here, formatted with Markdown for better readability\n   </description>\n   </pull_request>\n\nRemember to be clear, concise, and informative in your pull request. Your goal is to make it easy for your team to understand and review your changes effectively.",
                    }
                ],
            }
        ],
    )
    return message.content


if __name__ == "__main__":
    # args = sys.argv[1:]
    args = ["main"]
    print(main(args[0]))
