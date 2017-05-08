import maya.cmds as cmds
import maya.mel as mel
from functools import partial
import src.curves.Curves as Curves
import src.constants.Constants as Constants
import src.utils.Utils as Utils
import src.ui.RenameUI as Rename
import webbrowser

reload(Constants)
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
        cmds.button('bt_add', label='Create', edit=1, command=partial(self.addCurve))
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
        cmds.menuItem(p='curves_combobox', label='Select curve type')
        cmds.menuItem(p='curves_combobox', label=Constants.SQUARE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_CENTER_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_BASE_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.MOVE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.FOOT_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.SPHERE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.ARROW_180)
        #cmds.menuItem(p='curves_combobox', label=Constants.COG)

        cmds.showWindow(dialog)

        # window position
        cmds.window(dialog, edit=True, tlc=(150, 1000))

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
        mel.eval('ToggleOutliner;')

    def openNodeEditor(self, *pArgs):
        mel.eval('NodeEditorWindow;')

    def openComponentEditor(self, *pArgs):
        mel.eval('ComponentEditor;')

    def openSetDrivenKey(self, *pArgs):
        mel.eval('SetDrivenKeyOptions;')

    def openGraphEditor(self, *pArgs):
        print('openGraphEditor')

    def getListOfCvPoints(self, *pArgs):
        selecteds_curve = cmds.ls(selection=True)
        res = Curves.getListOfCvPoints(selecteds_curve[0])
        print(res)

    def checkZeroOut(self):
        # checkbox
        return cmds.checkBox('zeroOutCB', q=1, v=1)

    def checkCurveName(self):
        # textfield
        return cmds.textField('splineNameInput', query=True, text=True)

    def addCurve(self, args):
        # name
        spline_name = self.checkCurveName()
        Curves.setName(spline_name)

        # zero out
        check = self.checkZeroOut()
        Curves.setZeroOut(check)

        # create shape
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
            elif self.__current_menu_item == Constants.SQUARE_CONTROL:
                Curves.square()
            elif self.__current_menu_item == Constants.ARROW_180:
                Curves.arrow180()
            elif self.__current_menu_item == Constants.COG:
                Curves.cog()
