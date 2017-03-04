import socket
import urllib
import re


def renameListOfNames(list, new_name, prefix=None, sufix=None, pattern=None):
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


def getLocalIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    lip = s.getsockname()[0]
    return lip


def getPublicIp():
    f = urllib.urlopen("http://www.canyouseeme.org/")
    html_doc = f.read()
    f.close()

    m = re.search(
        '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
        html_doc)
    pip = m.group(0)
    return pip
