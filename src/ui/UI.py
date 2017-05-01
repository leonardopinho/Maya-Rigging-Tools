import maya.cmds as cmds
from functools import partial
import src.curves.Curves as Curves
import src.constants.Constants as Constants
import src.utils.Utils as Utils
import src.ui.RenameUI as Rename
import webbrowser

reload(Curves)


class UI:
    __path = None
    __current_menu_item = None
    __main_window = 'MainWindow'
    __rename_window = 'RenameWindow'

    def __init__(self, path):
        self.__path = path

    def getWindow(self):
        if cmds.window(self.__main_window, exists=True):
            cmds.deleteUI(self.__main_window, window=True)

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
        cmds.button('bt_anim_graph', edit=1, command=partial(self.getListOfCvPoints, self))
        cmds.button('bt_close', edit=1, command=partial(self.closeWindow, self))

        # combobox
        cmds.optionMenu('curves_combobox', edit=1, changeCommand=partial(self.changeMenuItem))
        cmds.menuItem(p='curves_combobox', label='Select type')
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_CENTER_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_BASE_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.MOVE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.FOOT_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.SPHERE_CONTROL)

        cmds.showWindow(dialog)

        # window position
        cmds.window(dialog, edit=True, tlc=(30, 1000))

    def changeMenuItem(self, item):
        self.__current_menu_item = item

    def closeWindow(self, *pArgs):
        cmds.deleteUI(self.__main_window, window=True)

    def credits(self, *pArgs):
        webbrowser.open(Constants.getCreditsUrl())

    def clearHistory(self, *pArgs):
        selection = cmds.ls(sl=1)
        for obj in selection:
            cmds.delete(obj, ch=1)

    def freezeTransformation(self, *pArgs):
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    def resetTransformation(self, *pArgs):
        print('resetTransformation')

    def centerPivot(self, *pArgs):
        print('centerPivot')

    def renameFiles(self, *pArgs):
        # rename ui
        Rename.getWindow(self.__path)

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

    def getListOfCvPoints(self, *pArgs):
        selecteds_curve = cmds.ls(selection=True)
        res = Curves.getListOfCvPoints(selecteds_curve[0])
        print(res)

    def checkZeroOut(self):
        # checkbox
        check = cmds.checkBox('zeroOutCB', q=1, v=1)
        return check

    def addCurve(self, args):

        # zero out
        check = self.checkZeroOut()
        Curves.setZeroOut(check)

        if self.__current_menu_item is not None:
            if self.__current_menu_item == Constants.CUBE_CENTER_PIVOT:
                Curves.cube()
            elif self.__current_menu_item == Constants.CUBE_BASE_PIVOT:
                Curves.cubeOnBase()
            elif self.__current_menu_item == Constants.MOVE_CONTROL:
                Curves.moveControl()
            elif self.__current_menu_item == Constants.FOOT_CONTROL:
                Curves.footControl()
            elif self.__current_menu_item == Constants.SPHERE_CONTROL:
                Curves.sphere()
