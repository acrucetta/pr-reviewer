import click
import os
from .git_utils import get_current_branch, get_diff, get_repo_name
from .generator import create_pr_description

@click.command()
@click.argument('compare_branch')
@click.option('--api-key', envvar='ANTHROPIC_API_KEY', 
              help='Anthropic API key. Can also be set via ANTHROPIC_API_KEY environment variable.')
def main(compare_branch, api_key):
    """Generate a pull request description comparing the current branch with COMPARE_BRANCH."""
    try:
        curr_branch = get_current_branch()
        repo_name = get_repo_name()
        diff = get_diff(curr_branch, compare_branch)
        
        click.echo("Generating the pull-request, it will take a few seconds...")
        pr_content = create_pr_description(diff, repo_name, curr_branch)
        click.echo(pr_content)
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)

if __name__ == '__main__':
    main()