import maya.cmds as cmds
import src.utils.Utils as Utils
import src.constants.Constants as Constants

reload(Utils)

__current_action = Constants.RENAME_ACTION
__rename_window = 'RenameWindow'
__pattern = None


def getWindow(path):
    if cmds.window(__rename_window, exists=True):
        cmds.deleteUI(__rename_window, window=True)

    rename_dialog = cmds.loadUI(f=path + '/src/ui/rename.ui')

    # radio button
    cmds.radioButton('renameRb', edit=True, cc=changeAction)

    # buttons
    cmds.button('renameBt', edit=True, command=renameAll)
    cmds.button('closeBt', edit=True, command=closeRenameUI)

    # combobox
    cmds.optionMenu('patternCb', edit=1, changeCommand=changeMenuItem)
    cmds.menuItem(p='patternCb', label='#')
    cmds.menuItem(p='patternCb', label='##')
    cmds.menuItem(p='patternCb', label='###')
    cmds.menuItem(p='patternCb', label='####')

    cmds.showWindow(rename_dialog)

    # window position
    cmds.window(rename_dialog, edit=True, tlc=(150, 900))


def changeAction(args):
    global __current_action

    if (cmds.radioButton('renameRb', q=True, sl=True)):
        __current_action = Constants.RENAME_ACTION
    else:
        __current_action = Constants.REPLACE_ACTION


def changeMenuItem(param):
    global __pattern
    __pattern = param


def renameAll(args):
    global __current_action, __pattern
    list = cmds.ls(selection=True)

    if len(list) == 0:
        Utils.warn('Select at least one item')
    else:
        if __current_action == Constants.RENAME_ACTION:

            prefix = cmds.textField('prefixTf', query=True, text=True)
            suffix = cmds.textField('suffixTf', query=True, text=True)
            new_word = cmds.textField('newNameTf', query=True, text=True)
            end_jnt = cmds.checkBox('endCb', q=1, v=1)

            new_list = Utils.renameListOfNames(list, new_word, prefix, suffix, __pattern, end_jnt)

            for i, item in enumerate(list):
                cmds.rename(item, str(new_list[i]))

            cmds.select(cl=True)

        elif __current_action == Constants.REPLACE_ACTION:
            list = cmds.ls(selection=True)
            new_list = Utils.renameListByChangingWord(list, search_term, new_word)
            for i, item in enumerate(list):
                cmds.rename(item, str(new_list[i]))


def closeRenameUI(args):
    cmds.deleteUI(__rename_window, window=True)
