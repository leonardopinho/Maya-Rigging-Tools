"""
    Rigging Tools
    Version: 0.2
    Author: Leonardo Pinho
    Email: contato@leonardopinho.com
"""
import inspect, sys, os

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

if path not in sys.path:
    sys.path.append(path)

from src.ui.MainUI import MainUI

ui = MainUI(path)
ui.open()
