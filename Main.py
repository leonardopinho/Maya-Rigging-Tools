import sys

path = r'/Users/lpinho/Library/Preferences/Autodesk/maya/2017/scripts/RiggingTools'

if path not in sys.path:
    sys.path.append(path)

import src.ui.UI as UI

reload(UI)

from src.ui.UI import UI


def init():
    ui = UI(path)
    ui.getWindow()


init()
