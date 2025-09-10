# Contributing to KX-Publish-PyPI

Thank you for your interest in contributing to KX-Publish-PyPI! 🚀

We welcome contributions from the community and are grateful for any help you can provide.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Development Guidelines](#development-guidelines)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## 🤝 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/kx-publish-pypi.git
   cd kx-publish-pypi
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # On Windows PowerShell:
   .venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

**⚠️ Important**: Always work within the activated `.venv` environment for all development tasks.

## 🛠️ Development Setup

### Prerequisites

- Python 3.9+
- Git
- A code editor (VS Code recommended)

### Installing Development Dependencies

```bash
# Always activate the virtual environment first
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

# Install the package in development mode with all extras
pip install -e ".[dev]"

# Install pre-commit hooks (optional)
pre-commit install
```

### Development Workflow Requirements

- **Always use the sequential thinking tool** (`#sequentialthinking`) for planning and managing tasks
- **Always work within the `.venv` environment** - never install or run code outside it
- **Use structured to-do lists** for managing complex tasks
- **Plan ahead** and anticipate future needs when making changes

## 💡 How to Contribute

### Types of Contributions

- 🐛 **Bug fixes** - Fix existing issues
- ✨ **Features** - Add new functionality
- 📚 **Documentation** - Improve docs or examples
- 🧪 **Tests** - Add or improve test coverage
- 🎨 **UI/UX** - Improve user interface and experience

### Contribution Workflow

1. **Choose an issue** or create a new one
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number-description
   ```
3. **Make your changes**
4. **Write tests** for new functionality using `if __name__ == '__main__'` blocks
5. **Run the test suite**:
   ```bash
   # Run tests using Python's main block execution
   python src/kx_publish_pypi/module_to_test.py
   ```
6. **Format your code**:
   ```bash
   black src/
   isort src/
   ```
7. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
8. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
9. **Create a Pull Request**

## 📝 Development Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Write descriptive commit messages following [Conventional Commits](https://conventionalcommits.org/)

### Commit Message Format

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

### Naming Conventions

- **Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Files**: `snake_case.py`

### Code Quality Standards

- **Type Hints**: Always use comprehensive type annotations
- **Docstrings**: Provide docstrings for all functions, classes, and modules
- **Code Splitting**: Split code into multiple files when modules grow too large
- **Type Checking**: Never use `# type: ignore` comments or `from __future__ import annotations`
- **Forward Thinking**: Plan ahead and anticipate future needs when implementing features
- **Structured Development**: Use to-do lists and task management for complex changes

### Development Best Practices

- Break down complex tasks into manageable steps
- Suggest improvements and optimizations proactively
- Follow an encouraging, ideas-focused development approach
- Maintain high code quality and readability standards
- Consider performance, architecture, and maintainability in all changes

## 🧪 Testing

### Testing Philosophy

This project uses Python's built-in `if __name__ == '__main__'` blocks for testing instead of external testing frameworks. This approach:

- Keeps dependencies minimal
- Allows for quick, focused testing during development
- Supports unit, integration, and usage testing patterns
- Encourages test-driven development practices

### Running Tests

```bash
# Activate virtual environment first
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate   # macOS/Linux

# Run specific module tests
python src/kx_publish_pypi/checks.py
python src/kx_publish_pypi/version_detection.py

# Run example usage tests
python tests/example_api_usage.py
python tests/test_enhanced_version_detection.py
```

### Writing Tests

- **Unit Tests**: Test individual functions and classes using `if __name__ == '__main__'` blocks
- **Integration Tests**: Test module interactions and workflows
- **Usage Tests**: Test real-world usage scenarios and examples

Example test structure:
```python
def test_function_name():
    """Test description"""
    # Test implementation
    pass

if __name__ == '__main__':
    test_function_name()
    print("All tests passed!")
```

- Write tests for all new features
- Use descriptive test names and docstrings
- Follow the existing test patterns in the codebase
- Include both positive and negative test cases

## 🔄 Submitting Changes

### Pull Request Process

1. **Update the README.md** if needed
2. **Update documentation** for any new features
3. **Add tests** for new functionality
4. **Ensure CI passes** all checks
5. **Request review** from maintainers

### Pull Request Template

Please use the following template for your PR:

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] Commit messages are clear
```

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: Step-by-step instructions
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, etc.
- **Logs**: Any relevant error messages

### Feature Requests

For feature requests, please include:

- **Description**: What feature you'd like to see
- **Use case**: Why this feature would be useful
- **Implementation ideas**: Any thoughts on how to implement it

## 📞 Getting Help

If you need help or have questions:

- 📧 **Email**: abueltayef.khader@gmail.com
- 📧 **Email**: contact@khaderx.com
- 🌐 **Website**: https://KhaderX.com/
- 💬 **GitHub Discussions**: [GitHub Discussions](https://github.com/Khader-X/kx-publish-pypi/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Khader-X/kx-publish-pypi/issues)
- 📱 **Phone**: +32 483 817 658 (Belgium)

## 🙏 Recognition

Contributors will be recognized in:
- The project's README.md
- Release notes
- Future documentation

## 💡 Suggestions & Improvements

We encourage all contributors to:
- **Propose optimizations** for performance, architecture, or user experience
- **Suggest new features** that would benefit the community
- **Recommend best practices** for coding and development workflows
- **Identify opportunities** for code refactoring or modernization
- **Share innovative ideas** that push the project forward

Your suggestions help make KX-Publish-PyPI better for everyone! 🚀

Thank you for contributing to KX-Publish-PyPI! 🎉
