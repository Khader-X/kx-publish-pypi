#!/usr/bin/env python3
"""
Example usage of the enhanced version detection API.

This demonstrates how to use the enhanced version detection system programmatically.
"""

from pathlib import Path
from kx_publish_pypi import detect_package_version, get_package_version


def example_usage():
    """Example of using the enhanced version detection API."""

    # Simple version detection (legacy interface)
    package_path = Path(".")
    version = get_package_version(package_path)
    print(f"Simple detection: {version}")

    # Enhanced version detection with full diagnostics
    result = detect_package_version(package_path)

    if result.version_info:
        info = result.version_info
        print(f"\n📦 Enhanced Detection Results:")
        print(f"   Version: {info.version}")
        print(f"   Source: {info.source}")
        print(f"   Method: {info.method}")
        print(f"   Dynamic: {info.is_dynamic}")
        print(f"   Backend: {info.build_backend}")
        print(f"   Confidence: {info.confidence}%")
    else:
        print(f"\n❌ Version detection failed")
        print(f"   Attempts: {', '.join(result.attempts)}")
        if result.errors:
            print(f"   Errors: {'; '.join(result.errors)}")


if __name__ == "__main__":
    example_usage()
