"""
Set relative path in Grasshopper
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import os

# set path
datapath = os.path.dirname(ghdoc.Path)
Path = os.path.join(datapath, Filename)
print(Path)