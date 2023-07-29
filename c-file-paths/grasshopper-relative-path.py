"""
Set relative path in Grasshopper
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os

# set path
datapath = pathlib.Path(__file__).parent.absolute()
Path = os.path.join(datapath, Filename)
print(Path)