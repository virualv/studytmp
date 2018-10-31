# Author : virualv
# Time : 9/29/2018 10:24 PM

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mods import main
main.main()

print(__file__)