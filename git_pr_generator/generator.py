import anthropic
from .constants import SYSTEM_PROMPT

def create_pr_description(diff: str, repo_name: str, branch_name: str):
    """Generate a PR description using the Anthropic API."""
    client = anthropic.Anthropic()
    
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
                "content": system_prompt
            }
        ],
    )
    return message.content[0].text