"""
Used to get versions Python, Pandas, and TensorFlow.  Useful when you have
several python virtual environments and use pip to install packages under the
local user.

The script also shows dependancies called by for Pandas.  Not all packages are
required unless your program calls pandas functions requiring those functions.
########################################################################
"""
print(__doc__)

import sys
import pytest
import pandas as pd
import tensorflow as tf

print('Python Version')
print(sys.version)
print('\n')
print('Pandas Version')
print(pd.__version__)
print('\n')
print('Pandas Dependancy Packages Versions')
print(pd.show_versions(as_json=False))
print('\n')
print('TensorFlow Version')
print(tf.__version__)

"""The code below runs pytest on Pandas.  Will take some time.
The test showed 9186 tests passed and 3 failed with 1162 skipped
on my machine.  The failed tests were all timezone issues in the
dateutil module.  """

#print('\n')
#print('Test Pandas')
#print(pd.test())
