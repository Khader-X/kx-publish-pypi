# Releasing KX-Publish-PyPI ✨

This guide outlines the process for releasing new versions of KX-Publish-PyPI.

## 🚀 Quick Release Process

For a standard release, use the tool itself:

```bash
# Bump version and release
kx-publish-pypi bump patch  # or minor/major
kx-publish-pypi run
```

## 📋 Detailed Release Checklist

### 1. Pre-Release Checks

- [ ] All tests passing locally and in CI
- [ ] Documentation is up to date
- [ ] CHANGELOG.md updated with new version
- [ ] No outstanding critical issues
- [ ] Version detection working correctly

### 2. Version Bumping

Choose the appropriate version bump:

```bash
# For bug fixes and small improvements
kx-publish-pypi bump patch    # 1.0.0 → 1.0.1

# For new features (backward compatible)
kx-publish-pypi bump minor    # 1.0.1 → 1.1.0

# For breaking changes
kx-publish-pypi bump major    # 1.1.0 → 2.0.0
```

### 3. Update CHANGELOG.md

Add a new section for the version being released:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Modified functionality

### Fixed
- Bug fixes
```

### 4. Pre-Publish Verification

Run comprehensive checks:

```bash
# Check package structure and version detection
kx-publish-pypi check

# Build and verify packages
python -m build
twine check dist/*
```

### 5. Test Release

Always test on TestPyPI first:

```bash
# Publish to TestPyPI
kx-publish-pypi publish-test

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ kx_publish_pypi
```

### 6. Production Release

Once TestPyPI release is verified:

```bash
# Publish to PyPI
kx-publish-pypi publish-prod
```

### 7. Post-Release Tasks

- [ ] Create GitHub release with changelog
- [ ] Update website documentation at [KhaderX.com](https://KhaderX.com/)
- [ ] Announce release on relevant channels
- [ ] Update any dependent projects

## 🔧 Manual Release Process

If you need to release manually without using the tool:

### Prerequisites

- Ensure `pyproject.toml` dynamic version points to `src/kx_publish_pypi/__version__.py`
- API tokens configured for TestPyPI and PyPI

### Steps

1. **Update Version**:
   ```bash
   # Edit src/kx_publish_pypi/__version__.py
   __version__ = "X.Y.Z"
   ```

2. **Build Package**:
   ```bash
   python -m build
   ```

3. **Upload to TestPyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   ```

4. **Test Installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ kx_publish_pypi==X.Y.Z
   ```

5. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

## 🔄 CI/CD Release Process

For automated releases via GitHub Actions:

### Setup

1. Add secrets to GitHub repository:
   - `TEST_PYPI_TOKEN`: TestPyPI API token
   - `PYPI_TOKEN`: PyPI API token

### Workflow Example

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install kx-publish-pypi
    
    - name: Publish to PyPI
      run: |
        kx-publish-pypi setup-tokens --test-token ${{ secrets.TEST_PYPI_TOKEN }} --prod-token ${{ secrets.PYPI_TOKEN }}
        kx-publish-pypi publish-prod
```

## 🏷️ Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

### Version Examples

- `1.0.0` - Initial stable release
- `1.0.1` - Bug fix release
- `1.1.0` - New features, backwards compatible
- `2.0.0` - Breaking changes

## 📝 Release Notes Guidelines

When writing release notes:

### Use Clear Categories
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Now removed features
- **Fixed**: Bug fixes
- **Security**: Vulnerability fixes

### Be Descriptive
- Explain the impact of changes
- Include code examples for new features
- Link to relevant issues/PRs

### Target Your Audience
- Write for developers using the tool
- Include migration instructions for breaking changes
- Highlight important new capabilities

## 🧪 Testing Releases

### Local Testing
```bash
# Build locally
python -m build

# Install locally
pip install dist/kx_publish_pypi-*.whl

# Test CLI
kx-publish-pypi --version
kx-publish-pypi check
```

### TestPyPI Testing
```bash
# After uploading to TestPyPI
pip install --index-url https://test.pypi.org/simple/ kx_publish_pypi

# Verify it works
kx-publish-pypi check
```

## 🆘 Troubleshooting

### Common Issues

**Version not detected properly**:
- Check `src/kx_publish_pypi/__version__.py` format
- Ensure `pyproject.toml` points to correct attribute

**Upload fails**:
- Verify API tokens are correct
- Check that version doesn't already exist
- Ensure package builds correctly

**Import errors after release**:
- Check package structure in built wheel
- Verify all dependencies are listed in `pyproject.toml`

### Getting Help

- 🐛 **Issues**: [GitHub Issues](https://github.com/Khader-X/kx-publish-pypi/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Khader-X/kx-publish-pypi/discussions)
- 🌐 **Website**: [KhaderX.com](https://KhaderX.com/)

---

<div align="center">
  <strong>🎉 Happy releasing! Made with ❤️ by <a href="https://KhaderX.com/">KhaderX</a></strong>
</div>