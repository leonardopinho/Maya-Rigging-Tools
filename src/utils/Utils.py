import socket


def renameListOfNames(list, new_name, prefix=None, sufix=None, pattern=None):
    if list.__len__() == 0:
        raise Exception('The list can not be empty')

    if new_name == None or new_name == '':
        raise Exception('A new valid name is required.')

    new_list = []
    len = 1

    if pattern != None and '#' in pattern:
        len = map(str, pattern).__len__()

    for i, item in enumerate(list):

        result = ''
        idx = '_{0}'.format(str(i + 1).zfill(len))

        # add prefix
        if prefix != None and prefix != '':
            result = prefix

        result = result + new_name

        # add sufix
        if sufix != None and sufix != '':
            result = result + idx + sufix

        new_list.append(result)

    return new_list


def getHostname():
    hostname = socket.gethostname()
    return hostname
