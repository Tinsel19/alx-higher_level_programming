#!/usr/bin/python3
import os
import py_compile
import sys

# Get the filename from the environment variable
filename = os.environ.get('PYFILE')

# Compile the file using py_compile
py_compile.compile(filename)

# Set the output filename with .pyc extension
output_filename = filename + 'c'

# Rename the compiled file to the output filename
os.rename('__pycache__/' + filename + '.cpython-{}.pyc'.format(sys.version_info[0]), output_filename)

# Remove the __pycache__ directory
os.rmdir('__pycache__')
