import maya.cmds as cmds
import src.utils.Utils as Utils
import src.constants.Constants as Constants

__current_action = Constants.RENAME_ACTION
__rename_window = 'RenameWindow'

def getWindow(path):
    if cmds.window(__rename_window, exists=True):
        cmds.deleteUI(__rename_window, window=True)

    rename_dialog = cmds.loadUI(f=path + '/src/ui/rename.ui')

    # radio button
    cmds.radioButton('renameRb', edit=True, cc=changeAction)

    # buttons
    cmds.button('renameBt', edit=True, command=renameAll)

    cmds.showWindow(rename_dialog)
    cmds.window(rename_dialog, edit=True, tlc=(30, 735))


def changeAction(args):

    global __current_action

    if (cmds.radioButton('renameRb', q=True, sl=True)):
        __current_action = Constants.RENAME_ACTION
    else:
        __current_action = Constants.REPLACE_ACTION


def renameAll(args):

    global __current_action
    list = cmds.ls(selection=True)

    if len(list) == 0:

        Utils.warn('Select at least one item')

    else:

        if __current_action == Constants.RENAME_ACTION:
            search_term = 'joint'
            new_word = 'Pink'

            new_list = Utils.renameListOfNames(list, new_word, 'L_', '_Jnt', '###')
            for i, item in enumerate(list):
                cmds.rename(item, str(new_list[i]))

        # list = cmds.ls(selection=True)
        # new_list = Utils.renameListByChangingWord(list, search_term, new_word)
        # for i, item in enumerate(list):
        #     cmds.rename(item, str(new_list[i]))
        __list = None
