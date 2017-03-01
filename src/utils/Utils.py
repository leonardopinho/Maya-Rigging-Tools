import socket
import urllib
import re
from pymel import versions


def getMayaVersion():
    return ('{0}'.format(versions.current())[0:4])


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
