import maya.cmds as cmds
from src.Extras.Constants import Constants
from src.Utils.Utils import Utils
from src.UI.UIBase import UIBase


class RenameUI(UIBase):
    __current_action = Constants.RENAME_ACTION
    __win_name = None
    __dialog = None
    __pattern = None
    __path = None
    __x = None
    __y = None

    def __init__(self, path, x_pos=150, y_pos=700):
        '''
        Rename script for multiples selections of objects (mesh, group, joint, spline...)
        :param path: string
        :param x_pos: int
        :param y_pos: int
        '''
        if path == None:
            raise Exception('Path is required')

        self.__win_name = 'RenameWindow'
        self.__path = path
        self.__x = x_pos
        self.__y = y_pos

        self.config()

    def config(self):
        if cmds.window(self.__win_name, exists=True):
            cmds.deleteUI(self.__win_name, window=True)

        # url of UI file
        url = '%s/%s' % (self.__path, 'UI/rename.UI')
        self.__dialog = cmds.loadUI(f=url)

        # radio button
        cmds.radioButton('renameRb', edit=True, cc=self.changeAction)

        # buttons
        cmds.button('renameBt', edit=True, command=self.renameAll)
        cmds.button('closeBt', edit=True, command=self.close)

        # combobox
        cmds.optionMenu('patternCb', edit=1, changeCommand=self.changeMenuItem)
        cmds.menuItem(p='patternCb', label='#')
        cmds.menuItem(p='patternCb', label='##')
        cmds.menuItem(p='patternCb', label='###')
        cmds.menuItem(p='patternCb', label='####')

    def open(self):
        cmds.showWindow(self.__dialog)
        cmds.window(self.__dialog, edit=True, tlc=(self.__x, self.__y))

    def close(self, args):
        # close window
        cmds.deleteUI(self.__win_name, window=True)

    def changeAction(self, args):
        '''
        Set type of rename action (rename or replace)
        '''
        if (cmds.radioButton('renameRb', q=True, sl=True)):
            self.__current_action = Constants.RENAME_ACTION
        else:
            self.__current_action = Constants.REPLACE_ACTION

    def changeMenuItem(self, args):
        self.__pattern = param

    def renameAll(self, args):
        list = cmds.ls(selection=True)

        if len(list) == 0:
            Utils.warn('Select at least one item')
        else:
            if self.__current_action == Constants.RENAME_ACTION:

                prefix = cmds.textField('prefixTf', query=True, text=True)
                suffix = cmds.textField('suffixTf', query=True, text=True)
                new_word = cmds.textField('newNameTf', query=True, text=True)
                end_jnt = cmds.checkBox('endCb', q=1, v=1)

                new_list = Utils.renameListOfNames(list, new_word, prefix, suffix, self.__pattern, end_jnt)

                for i, item in enumerate(list):
                    cmds.rename(item, str(new_list[i]))

                cmds.select(cl=True)

            elif self.__current_action == Constants.REPLACE_ACTION:
                list = cmds.ls(selection=True)
                new_list = Utils.renameListByChangingWord(list, search_term, new_word)
                for i, item in enumerate(list):
                    cmds.rename(item, str(new_list[i]))
