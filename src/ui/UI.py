import maya.cmds as cmds
from functools import partial
import src.curves.Curves as Curves

reload(Curves)

class UI:
    def __init__(self, path):
        self.__windowName = 'MainWindow'
        self.__path = path
        self.__current_menu_item = None

    def getWindow(self):
        if cmds.window(self.__windowName, exists=True):
            cmds.deleteUI(self.__windowName, window=True)

        dialog = cmds.loadUI(f=self.__path + '/src/ui/main.ui')

        # buttons
        cmds.button('bt_history', label='', edit=1, command=partial(self.clearHistory, self))
        cmds.button('bt_add', label='Add', edit=1, command=partial(self.addCurve))

        # combobox
        cmds.optionMenu('curves_combobox', edit=1, changeCommand=partial(self.changeMenuItem))
        cmds.menuItem(p='curves_combobox', label=' ---- select type ---- ')
        cmds.menuItem(p='curves_combobox', label='Cube (center pivot)')
        cmds.menuItem(p='curves_combobox', label='Cube (base pivot)')
        cmds.menuItem(p='curves_combobox', label='Move control')
        cmds.menuItem(p='curves_combobox', label='Foot control')

        cmds.showWindow(dialog)

    def clearHistory(self, *pArgs):
        print('clear history')

    def changeMenuItem(self, item):
        self.__current_menu_item = item

    def addCurve(self, args):
        if self.__current_menu_item is not None:

            if self.__current_menu_item == 'Cube (center pivot)':
                Curves.cube()
            elif self.__current_menu_item == 'Cube (base pivot)':
                Curves.cubeOnBase()
            elif self.__current_menu_item == 'Move control':
                Curves.moveControl()
            elif self.__current_menu_item == 'Foot control':
                Curves.footControl()

    def closeWindow(self, *pArgs):
        cmds.deleteUI(self.__windowName, window=True)
