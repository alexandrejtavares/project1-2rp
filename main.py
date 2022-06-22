#!python3
# -*- coding: utf-8 -*-

import os
import time

while True:

    # Read TWORPTEST environment variable
    var_tworptest = os.getenv("TWORPTEST")

    if (var_tworptest):
        print(var_tworptest)
    else:
        print("TWORPTEST var is empty.")
    
    # Wait 20 secs to read again
    time.sleep(20) 