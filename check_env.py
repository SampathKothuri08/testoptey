import sys
import setuptools
import pip
try:
    import cython
    cython_version = cython.__version__
except ImportError:
    cython_version = "Not installed"

print(f"Python Version: {sys.version}")
print(f"pip Version: {pip.__version__}")
print(f"setuptools Version: {setuptools.__version__}")
print(f"Cython Version: {cython_version}")
