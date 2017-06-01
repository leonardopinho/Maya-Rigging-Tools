from src.ui.UIBase import UIBase
import maya.cmds as cmds
import maya.mel as mel

from src.scripts.curves.Curves import Curves
from src.extras.Constants import Constants
from src.ui.RenameUI import RenameUI
from src.utils.Utils import Utils


class MainUI(UIBase):
    __current_menu_item = None
    __win_name = None
    __dialog = None
    __path = None
    __x = None
    __y = None

    def __init__(self, path, x_pos=150, y_pos=1000):
        if path == None:
            raise Exception('Path is required')

        self.__win_name = 'MainWindow'
        self.__path = path
        self.__x = x_pos
        self.__y = y_pos

        self.config()

    def config(self):
        if cmds.window(self.__win_name, exists=True):
            cmds.deleteUI(self.__win_name, window=True)

        # url of ui file
        url = '%s/%s' % (self.__path, 'ui/main.ui')
        self.__dialog = cmds.loadUI(f=url)

        # buttons
        cmds.button('bt_about', edit=1, command=self.credits)
        cmds.button('bt_add', label='Create', edit=1, command=self.addCurve)
        cmds.button('bt_history', edit=1, command=self.clearHistory)
        cmds.button('bt_freeze', edit=1, command=self.freezeTransformation)
        cmds.button('bt_reset', edit=1, command=self.resetTransformation)
        cmds.button('bt_pivot', edit=1, command=self.centerPivot)
        cmds.button('bt_rename', edit=1, command=self.renameFiles)
        cmds.button('bt_outliner', edit=1, command=self.openOutliner)
        cmds.button('bt_node', edit=1, command=self.openNodeEditor)
        cmds.button('bt_component', edit=1, command=self.openComponentEditor)
        cmds.button('bt_set_driven', edit=1, command=self.openSetDrivenKey)
        cmds.button('bt_anim_graph', edit=1, command=self.getListOfCvPoints)
        cmds.button('bt_close', edit=1, command=self.close)

        # combobox
        cmds.optionMenu('curves_combobox', edit=1, changeCommand=self.changeMenuItem)
        cmds.menuItem(p='curves_combobox', label='')
        cmds.menuItem(p='curves_combobox', label=Constants.SQUARE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_CENTER_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.CUBE_BASE_PIVOT)
        cmds.menuItem(p='curves_combobox', label=Constants.MOVE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.FOOT_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.SPHERE_CONTROL)
        cmds.menuItem(p='curves_combobox', label=Constants.ARROW_180)
        # cmds.menuItem(p='curves_combobox', label=Constants.COG)

        # instance of Curves
        self.curves = Curves()

    def open(self):
        cmds.showWindow(self.__dialog)
        cmds.window(self.__dialog, edit=True, tlc=(self.__x, self.__y))

    def close(self, args):
        # close window
        cmds.deleteUI(self.__win_name, window=True)

    def changeMenuItem(self, item):
        # change type of curve
        self.__current_menu_item = item

    def credits(self, args):
        # more about me
        Utils.getUrl(Constants.getCreditsUrl())

    def clearHistory(self, args):
        # Clear the history of selected objects
        selection = cmds.ls(sl=1)
        for obj in selection:
            cmds.delete(obj, ch=1)

    def freezeTransformation(self, args):
        # Freeze all parameters of selected objetcs
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    def resetTransformation(self, args):
        print('resetTransformation')

    def centerPivot(self, args):
        mel.eval('CenterPivot;')

    def renameFiles(self, args):
        # rename ui
        ui = RenameUI(self.__path)
        ui.open()

    def openOutliner(self, args):
        mel.eval('ToggleOutliner;')

    def openNodeEditor(self, args):
        mel.eval('NodeEditorWindow;')

    def openComponentEditor(self, args):
        mel.eval('ComponentEditor;')

    def openSetDrivenKey(self, args):
        mel.eval('SetDrivenKeyOptions;')

    def openGraphEditor(self, args):
        print('openGraphEditor')

    def getListOfCvPoints(self, args):
        selecteds_curve = cmds.ls(selection=True)
        res = self.curves.getListOfCvPoints(selecteds_curve[0])
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
        self.curves.name = spline_name

        # zero out
        check = self.checkZeroOut()
        self.curves.zeroOut = check

        # create shape
        if self.__current_menu_item is not None:
            if self.__current_menu_item == Constants.CUBE_CENTER_PIVOT:
                self.curves.cube()
            elif self.__current_menu_item == Constants.CUBE_BASE_PIVOT:
                self.curves.cubeOnBase()
            elif self.__current_menu_item == Constants.MOVE_CONTROL:
                self.curves.moveControl()
            elif self.__current_menu_item == Constants.FOOT_CONTROL:
                self.curves.footControl()
            elif self.__current_menu_item == Constants.SPHERE_CONTROL:
                self.curves.sphere()
            elif self.__current_menu_item == Constants.SQUARE_CONTROL:
                self.curves.square()
            elif self.__current_menu_item == Constants.ARROW_180:
                self.curves.arrow180()
            elif self.__current_menu_item == Constants.COG:
                self.curves.cog()
