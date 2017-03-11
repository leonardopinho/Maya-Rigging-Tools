import maya.cmds as cmds

__current_action = None
__rename_window = 'RenameWindow'
__list = None

def getWindow(path, list):
    if cmds.window(__rename_window, exists=True):
        cmds.deleteUI(__rename_window, window=True)

    __list = list
    rename_dialog = cmds.loadUI(f=path + '/src/ui/rename.ui')
    #cmds.radioButton('renameRb', edit=True, da=1)
    cmds.showWindow(rename_dialog)
    cmds.window(rename_dialog, edit=True, tlc=(30, 735))

    # open ui
    # search_term = 'joint'
    # new_word = 'Pink'

    # new_list = Utils.renameListOfNames(list, new_word, 'L_', '_Jnt', '###')
    # for i, item in enumerate(list):
    #     cmds.rename(item, str(new_list[i]))

    # list = cmds.ls(selection=True)
    # new_list = Utils.renameListByChangingWord(list, search_term, new_word)
    # for i, item in enumerate(list):
    #     cmds.rename(item, str(new_list[i]))

def renameAll():
    pass
    #end action
    #__list = None
