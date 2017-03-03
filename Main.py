"""
    Rigging Tools
    Version: 0.1
    Author: Leonardo Pinho
    Email: contato@leonardopinho.com
"""

try:

    import inspect
    import sys
    import os

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))

    if path not in sys.path:
        sys.path.append(path)

except Exception as e:
    print(e)

import src.ui.UI as UI

reload(UI)

from src.ui.UI import UI


def init():
    ui = UI(path)
    ui.getWindow()


init()
