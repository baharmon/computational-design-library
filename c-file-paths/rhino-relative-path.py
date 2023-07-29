"""
Set path to file in parent directory using Rhino
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

import pathlib
import os

# set path
filename = 'file.txt'
datapath = pathlib.Path(__file__).parent.absolute()
data = os.path.join(datapath, filename)
print(data)