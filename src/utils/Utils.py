import socket


def renameListOfNames(list, new_name, prefix=None, sufix=None, pattern=None):
    # list validation
    if len(list) == 0:
        raise Exception('The list can not be empty')

    # new_name validation
    if new_name == None or new_name == '':
        raise Exception('A new valid name is required.')

    new_list = []
    l_len = 1

    if pattern != None and '#' in pattern:
        l_len = sum((map(len, pattern)))

    for i, item in enumerate(list):

        result = ''

        # add counter, based in '#' pattern
        idx = '_{0}'.format(str(i + 1).zfill(l_len))

        # add prefix
        if prefix != None and prefix != '':
            result = prefix

        result = result + new_name

        # add sufix
        if sufix != None and sufix != '':
            result = result + idx + sufix

        new_list.append(result)

    return new_list


def renameListByChangingWord(list, old_word, new_word):
    pass


def getHostname():
    hostname = socket.gethostname()
    return hostname
