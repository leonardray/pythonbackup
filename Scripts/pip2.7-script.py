#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==8.1.1','console_scripts','pip2.7'
__requires__ = 'pip==8.1.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==8.1.1', 'console_scripts', 'pip2.7')()
    )
