try:

    import inspect
    import sys
    import os

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))

    print(path)

except Exception as e:
    print(e)

if path not in sys.path:
    sys.path.append(path)

import src.ui.UI as UI

reload(UI)

from src.ui.UI import UI


def init():
    ui = UI(path)
    ui.getWindow()


init()
