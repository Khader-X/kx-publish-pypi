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
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## 🛠️ Development Setup

### Prerequisites

- Python 3.9+
- Git
- A code editor (VS Code recommended)

### Installing Development Dependencies

```bash
# Install the package in development mode with all extras
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

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
4. **Write tests** for new functionality
5. **Run the test suite**:
   ```bash
   pytest
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

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/kx_publish_pypi

# Run specific test file
pytest tests/test_specific_feature.py

# Run tests in verbose mode
pytest -v
```

### Writing Tests

- Write tests for all new features
- Use descriptive test names
- Follow the existing test structure
- Aim for high test coverage (>80%)

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

- 📧 **Email**: khader@example.com
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Khader-X/kx-publish-pypi/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Khader-X/kx-publish-pypi/issues)

## 🙏 Recognition

Contributors will be recognized in:
- The project's README.md
- Release notes
- Future documentation

Thank you for contributing to KX-Publish-PyPI! 🎉
