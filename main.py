#!/usr/bin/python3

from love_letter import *
from main_platform import *

import sys

from PyQt5.QtWidgets import QApplication

def test_view(full):
    activity = MainActivity()
    activity.main()

def main(args):
    if '--test-view' in args:
        test_view("--full" in args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))



