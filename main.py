#!/usr/bin/python3

from love_letter import *
from ui import *

import sys

from PyQt5.QtWidgets import QApplication

def test_view(full):
    app = QApplication([''])
    fen = MainWindow()
    fen.set_full_screen_mode(full)
    return app.exec()

def main(args):
    if '--test-view' in args:
        test_view("--full" in args)

if __name__ == "__main__":
    sys.exit(main(sys.argv))



