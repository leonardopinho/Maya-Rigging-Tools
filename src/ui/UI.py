import maya.cmds as cmds
from functools import partial
import src.curves.Curves as Curves
import src.constants.Constants as Constants
import webbrowser


class UI:
    __windowName = 'MainWindow'

    def __init__(self, path):
        self.__path = path
        self.__current_menu_item = None

    def getWindow(self):
        if cmds.window(self.__windowName, exists=True):
            cmds.deleteUI(self.__windowName, window=True)

        dialog = cmds.loadUI(f=self.__path + '/src/ui/main.ui')

        # buttons
        cmds.button('bt_about', edit=1, command=partial(self.credits))
        cmds.button('bt_add', label='Add', edit=1, command=partial(self.addCurve))
        cmds.button('bt_history', edit=1, command=partial(self.clearHistory, self))
        cmds.button('bt_freeze', edit=1, command=partial(self.freezeTransformation, self))
        cmds.button('bt_reset', edit=1, command=partial(self.resetTransformation, self))
        cmds.button('bt_pivot', edit=1, command=partial(self.centerPivot, self))
        cmds.button('bt_rename', edit=1, command=partial(self.renameFiles, self))
        cmds.button('bt_outliner', edit=1, command=partial(self.openOutliner, self))
        cmds.button('bt_node', edit=1, command=partial(self.openNodeEditor, self))
        cmds.button('bt_component', edit=1, command=partial(self.openComponentEditor, self))
        cmds.button('bt_set_driven', edit=1, command=partial(self.openSetDrivenKey, self))
        cmds.button('bt_anim_graph', edit=1, command=partial(self.openGraphEditor, self))
        cmds.button('bt_close', edit=1, command=partial(self.closeWindow, self))

        # combobox
        cmds.optionMenu('curves_combobox', edit=1, changeCommand=partial(self.changeMenuItem))
        cmds.menuItem(p='curves_combobox', label='Select type')
        cmds.menuItem(p='curves_combobox', label='Cube (center pivot)')
        cmds.menuItem(p='curves_combobox', label='Cube (base pivot)')
        cmds.menuItem(p='curves_combobox', label='Move control')
        cmds.menuItem(p='curves_combobox', label='Foot control')

        cmds.showWindow(dialog)
        cmds.window(dialog, edit=True, tlc=(150, 690))

    def changeMenuItem(self, item):
        self.__current_menu_item = item

    def closeWindow(self, *pArgs):
        cmds.deleteUI(self.__windowName, window=True)

    def credits(self, *pArgs):
        webbrowser.open(Constants.getCreditsUrl())

    def clearHistory(self, *pArgs):
        print('clear history')

    def freezeTransformation(self, *pArgs):
        print('freezeTransformation')

    def resetTransformation(self, *pArgs):
        print('resetTransformation')

    def centerPivot(self, *pArgs):
        print('centerPivot')

    def renameFiles(self, *pArgs):
        print('renameFiles')

    def openOutliner(self, *pArgs):
        print('outliner')

    def openNodeEditor(self, *pArgs):
        print('openNodeEditor')

    def openComponentEditor(self, *pArgs):
        print('openComponentEditor')

    def openSetDrivenKey(self, *pArgs):
        print('openSetDrivenKey')

    def openGraphEditor(self, *pArgs):
        print('openGraphEditor')

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
