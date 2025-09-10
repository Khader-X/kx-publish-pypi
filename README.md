<div align="center">
  <img src="logo/logo-2-1.png" alt="KX-Publish-PyPI Logo" width="200"/>
</div>

# KX-Publish-PyPI

[![PyPI version](https://badge.fury.io/py/kx_publish_pypi.svg)](https://pypi.org/project/kx_publish_pypi/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Khader-X/kx-publish-pypi/ci.yml)](https://github.com/Khader-X/kx-publish-pypi/actions)

> ✨ **A friendly CLI tool to check and publish Python packages to TestPyPI/PyPI in 30 seconds!** 🚀

**Version 1.0.0** | **Author: ABUELTAYEF Khader** | **Python 3.9+**

---

## 🚀 Installation

### ✅ Quick Install
```bash
pip install kx-publish-pypi
```

### ✅ Verify Installation
```bash
kx-publish-pypi --version
```

### Installation Demo
![Installation & Version Check](screenshots/kx-publish-pypi_video_installation_version.gif)

---

## � Account Setup & Token Generation

Before you can publish packages, you'll need to create accounts on PyPI and TestPyPI, and generate API tokens.

### 1. Create PyPI Account
1. Go to [pypi.org](https://pypi.org/)
2. Click "Register" in the top right
3. Fill out the registration form
4. Verify your email address

### 2. Create TestPyPI Account
1. Go to [test.pypi.org](https://test.pypi.org/)
2. Click "Register" in the top right
3. Fill out the registration form
4. Verify your email address

### 3. Generate API Tokens

#### For PyPI:
1. Log in to [pypi.org](https://pypi.org/)
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Give it a name (e.g., "kx-publish-pypi")
5. Copy the token (you won't see it again!)

#### For TestPyPI:
1. Log in to [test.pypi.org](https://test.pypi.org/)
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Give it a name (e.g., "kx-publish-pypi-test")
5. Copy the token

### 4. Store Tokens Securely
Use the CLI to store your tokens securely:
```bash
kx-publish-pypi setup-tokens
```

This will prompt you to enter your TestPyPI and PyPI tokens, which will be stored in your system's keyring.

---

## 🚀 Quick Start

### 1. Complete Guided Workflow (**Recommended**)
```bash
kx-publish-pypi run
```
This interactive command handles everything: checks, tokens, version bump, build, and publish.

### 2. Individual Commands
```bash
# Check your package before publishing
kx-publish-pypi check

# Setup API tokens securely
kx-publish-pypi setup-tokens

# Bump version (patch/minor/major)
kx-publish-pypi bump patch

# Publish to TestPyPI
kx-publish-pypi publish-test

# Publish to PyPI
kx-publish-pypi publish-prod
```

---

## ✨ Key Features

- 🎨 **Rich Interface** - Rich, colorful output with progress bars
- 🔍 **Smart Pre-checks** - Validates package structure and configuration
- 🔐 **Secure Token Storage** - Uses system keyring for API tokens
- 📦 **Enhanced Version Detection** - Supports all modern Python build backends
- 🔥 **Interactive Workflow** - Guided experience from check to publish
- 📈 **Version Management** - Intelligent version bumping
- 🛠️ **Build Integration** - Works with setuptools, flit, hatchling, etc.

---

## 🚀 Programmatic API

```python
from kx_publish_pypi import detect_package_version
from pathlib import Path

# Enhanced version detection
result = detect_package_version(Path("."))
if result.version_info:
    print(f"Version: {result.version_info.version}")
    print(f"Method: {result.version_info.method}")
```

---

<div align="center">

**Powered by [KhaderX](https://KhaderX.com/)** | 
**Founder [ABUELTAYEF Khader](https://github.com/KhaderX-com)**

[![GitHub](https://img.shields.io/badge/GitHub-Khader--X-blue)](https://github.com/Khader-X)
[![Website](https://img.shields.io/badge/Website-KhaderX.com-blue)](https://KhaderX.com/)
[![PyPI](https://img.shields.io/badge/PyPI-KhaderX-orange)](https://pypi.org/user/KhaderX/)

**⭐ Star this repo if you find it useful!**

</div>

<div align="center">
  <img src="logo/logo-2-1.png" alt="KX-Publish-PyPI Logo" width="200"/>
</div>