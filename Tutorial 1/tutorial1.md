# First Tutorial

1. Install Python

2. Do basic sorting exercise

# Things that I've learned

If you want to use a relative filepath cross-platform, you gotta use the __file__ variable to handle it

# Sample code

import os
this_folder = os.path.dirname(os.path.abspath(__file__))
id_list = os.path.join(this_folder, 'idlist.txt')
