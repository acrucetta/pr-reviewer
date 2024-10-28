# Git PR Generator CLI

A command-line tool to help generate and manage pull requests.

## Prerequisites

Before installation, ensure you have:
- Python 3.12 or lower (3.13 not yet supported)
- pip (Python package installer)
- pipx (recommended for CLI tool installation)

## Quick Installation

```bash
# Install pipx if you haven't already
brew install pipx
pipx ensurepath

# Install the CLI tool
pipx install git+https://github.com/username/pr-reviewer.git
```

## Step-by-Step Installation Guide

1. **Install Python 3.12** (if not already installed)
   ```bash
   brew install python@3.12
   ```

2. **Install pipx** (recommended for CLI tools)
   ```bash
   brew install pipx
   pipx ensurepath
   ```
   
3. **Install the CLI tool**
   ```bash
   pipx install --python python3.12 git+https://github.com/username/pr-reviewer.git
   ```

4. **Verify installation**
   ```bash
   git-pr-generator --version
   ```

## Troubleshooting

### Python Version Issues
If you see an error about Python 3.13 or PyO3, ensure you're using Python 3.12:
```bash
# Check Python version
python3 --version

# If needed, install and use Python 3.12
brew install python@3.12
pipx install --python python3.12 git+https://github.com/username/pr-reviewer.git
```

### Permission Issues
If you encounter permission errors:
```bash
# Ensure pipx is properly installed
pipx ensurepath
source ~/.zshrc  # or source ~/.bashrc
```

### Installation Location Issues
If the command isn't found after installation:
```bash
# Add this to your ~/.zshrc or ~/.bashrc
export PATH="$PATH:$HOME/.local/bin"
source ~/.zshrc  # or source ~/.bashrc
```

## Updating the Tool

To update to the latest version:
```bash
pipx upgrade git-pr-generator
```

To uninstall:
```bash
pipx uninstall git-pr-generator
```

## Usage

After installation, you can use the tool by running:
```bash
git-pr-generator [options]
```

For detailed usage instructions, run:
```bash
git-pr-generator --help
```

## Development Setup

If you want to contribute or modify the tool:

1. Clone the repository
   ```bash
   git clone https://github.com/username/pr-reviewer.git
   cd pr-reviewer
   ```

2. Create a virtual environment
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies
   ```bash
   pip install -e .
   ```

## Support

If you encounter any issues, please:
1. Check the troubleshooting section above
2. Look through existing GitHub issues
3. Create a new issue if your problem isn't already reported
