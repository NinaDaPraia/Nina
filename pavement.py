import os
import sys

pwd = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(pwd, 'tasks'))

import test
