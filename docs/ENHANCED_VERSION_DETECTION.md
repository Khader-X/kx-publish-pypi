# Enhanced Version Detection System

## Overview

The `kx-publish-pypi` tool now includes a comprehensive **Enhanced Version Detection System** that robustly handles various build backends and dynamic versioning configurations used in modern Python packaging.

## 🚀 Key Features

### ✅ **Comprehensive Build Backend Support**
- **Static versions** in `pyproject.toml`
- **Setuptools** dynamic versioning (attr/file-based)
- **Scikit-build-core** with regex providers
- **Setuptools-scm** (git-based versioning)
- **Flit** module-based versioning
- **Hatchling** regex-based versioning

### ✅ **Intelligent Fallback System**
1. **Static version detection** from `pyproject.toml`
2. **Dynamic version resolution** from build backend configs
3. **Direct package import** attempts
4. **File parsing** of `__version__.py` files in common locations
5. **Setuptools-scm fallback** for git-based projects

### ✅ **Rich Diagnostic Information**
- **Detection method** used (e.g., `setuptools_dynamic_attr`, `scikit_build_regex`)
- **Source location** of the version
- **Build backend** identification
- **Confidence scoring** (0-100%)
- **Comprehensive error reporting**

## 📋 Supported Configurations

### 1. Static Version
```toml
[project]
name = "my-package"
version = "1.0.0"  # ← Direct static version
```
**Result**: `✅ v1.0.0 (static)`

### 2. Setuptools Dynamic (Attribute-based)
```toml
[project]
name = "my-package"
dynamic = ["version"]

[tool.setuptools.dynamic]
version = {attr = "my_package.__version__"}
```
**Result**: `✅ v1.0.0 (setuptools_dynamic_attr) dynamic backend:setuptools`

### 3. Setuptools Dynamic (File-based)
```toml
[project]
name = "my-package"
dynamic = ["version"]

[tool.setuptools.dynamic]
version = {file = "src/my_package/__version__.py"}
```
**Result**: `✅ v1.0.0 (setuptools_dynamic_file) dynamic backend:setuptools`

### 4. Scikit-build-core
```toml
[build-system]
requires = ["scikit-build-core"]
build-backend = "scikit_build_core.build"

[project]
name = "my-package"
dynamic = ["version"]

[tool.scikit-build.metadata.version]
provider = "scikit_build_core.metadata.regex"
input = "src/my_package/__version__.py"
```
**Result**: `✅ v1.0.0 (scikit_build_regex) dynamic backend:scikit-build-core`

### 5. Setuptools-scm
```toml
[build-system]
requires = ["setuptools-scm"]

[project]
name = "my-package"
dynamic = ["version"]

[tool.setuptools_scm]
```
**Result**: `✅ v1.0.0 (setuptools_scm) dynamic backend:setuptools-scm`

### 6. Flit
```toml
[build-system]
requires = ["flit_core"]
build-backend = "flit_core.buildapi"

[tool.flit.module]
name = "my_package"
```
**Result**: `✅ v1.0.0 (flit_module) dynamic backend:flit`

### 7. Hatchling
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
dynamic = ["version"]

[tool.hatch.version]
source = "regex"
path = "src/my_package/__version__.py"
```
**Result**: `✅ v1.0.0 (hatchling_regex) dynamic backend:hatchling`

## 🔍 Detection Process

The enhanced system follows a comprehensive detection strategy:

```python
def detect_version(package_path: Path) -> VersionDetectionResult:
    """Detection process in order of preference."""
    
    # 1. Static version (highest confidence)
    if static_version := get_static_version():
        return VersionInfo(confidence=100, method="static")
    
    # 2. Dynamic version from build backends
    if dynamic_version := get_dynamic_version():
        return VersionInfo(confidence=90-95, method="*_dynamic_*")
    
    # 3. Import package directly
    if import_version := try_import_version():
        return VersionInfo(confidence=85, method="import_package")
    
    # 4. Parse version files
    if parsed_version := parse_version_files():
        return VersionInfo(confidence=80, method="parse_version_file")
    
    # 5. Setuptools-scm fallback
    if scm_version := try_setuptools_scm():
        return VersionInfo(confidence=70, method="setuptools_scm_fallback")
    
    return None  # No version detected
```

## 🧪 Testing the Enhanced System

You can test the enhanced version detection with various package configurations:

```bash
# Test with your current package
kx-publish-pypi check

# Test with different build backends
kx-publish-pypi check path/to/scikit-build-package
kx-publish-pypi check path/to/setuptools-scm-package
```

The tool will show detailed information about how the version was detected:
```
🔢 Version .......................... ✅ (v1.0.0 (setuptools_dynamic_attr) dynamic backend:setuptools)
```

## 📊 Example Output

### Successful Detection
```
🔢 Version .......................... ✅ (v0.1.11 (setuptools_dynamic_attr) dynamic backend:setuptools)
```

### Failed Detection with Diagnostics
```
🔢 Version .......................... ❌ Failed to detect version. Tried: static_pyproject_version, dynamic_pyproject_version, import_package_version, parse_version_files. Errors: Import failed: No module named 'missing_package'
```

## 🛠️ Benefits for Package Authors

### **For Tool Users**
- **Robust detection** works with any modern Python package setup
- **Clear diagnostics** help troubleshoot version detection issues
- **No configuration needed** - works out of the box

### **For Package Maintainers**
- **Supports modern packaging** with dynamic versioning
- **Build backend agnostic** - works with setuptools, scikit-build-core, etc.
- **Future-proof** design accommodates new packaging approaches

## 🔧 Technical Implementation

The enhanced system is implemented in `src/kx_publish_pypi/version_detection.py` with:

- **`EnhancedVersionDetector`**: Main detection class
- **`VersionInfo`**: Rich version information with metadata
- **`VersionDetectionResult`**: Complete detection results with diagnostics
- **Pluggable detection methods** for different build backends

## 🎯 Confidence Scoring

The system provides confidence scores to help understand detection reliability:

- **100%**: Static version in pyproject.toml
- **95%**: Dynamic version via scikit-build-core regex
- **90%**: Dynamic version via setuptools attribute/file
- **85%**: Successful package import
- **80%**: Parsed from __version__.py files
- **70%**: Setuptools-scm fallback

## 🐛 Troubleshooting

### Common Issues and Solutions

1. **"Failed to detect version"**
   - Ensure `__version__` is properly exported in `__init__.py`
   - Check that version files are in expected locations
   - Verify dynamic version configuration in pyproject.toml

2. **"Invalid semver format"**
   - Use semantic versioning format: `MAJOR.MINOR.PATCH`
   - Examples: `1.0.0`, `2.1.3`, `0.1.0-alpha1`

3. **Import errors during detection**
   - Install package dependencies before running checks
   - Use virtual environments for isolated testing

## 🔮 Future Enhancements

The enhanced system is designed to be extensible for future packaging innovations:

- Support for new build backends
- Additional version file formats
- Custom detection plugins
- Advanced diagnostics and suggestions

---

This enhancement makes `kx-publish-pypi` compatible with the full spectrum of modern Python packaging approaches! 🎉
