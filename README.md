# Git PR Generator

A command-line tool that automatically generates pull request descriptions by analyzing git diffs using Claude AI.

## Installation

```bash
pip install pr-generator
```

## Usage

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY='your-api-key'

# Generate PR description comparing current branch with main
git-pr main

# Or specify a different branch to compare against
git-pr feature/branch
```

## Features

- Automatically generates comprehensive PR descriptions
- Analyzes git diffs to identify key changes
- Creates well-formatted titles and descriptions
- Integrates with Claude AI for intelligent analysis

## Requirements

- Python 3.7+
- Git
- Anthropic API key