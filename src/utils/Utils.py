try:
    import socket
    import maya.OpenMaya as om
    import webbrowser
    from pymel import versions
except Exception as e:
    print e


class Utils():
    @staticmethod
    def getUrl(url):
        # open browser
        if url != None:
            webbrowser.open(url)

    @staticmethod
    def renameListOfNames(list, new_name, prefix=None, suffix=None, pattern=None, end_jnt=False):
        """
        Rename list of items
        :param list:
        :param new_name:
        :param prefix:
        :param suffix:
        :param pattern:
        :param end_jnt:
        :return list:
        """

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

            result = '{0}{1}'.format(result, new_name)

            # add suffix
            if suffix != None and suffix != '':
                result = result + idx + suffix

            # end joint
            if end_jnt and i == (len(list) - 1):
                result = result.replace((idx + suffix), '_JEnd')

            new_list.append(result)

        return new_list

    @staticmethod
    def renameListByChangingWord(list, search_term, new_word):
        """
        Replace list of names with new word
        :param list:
        :param search_term:
        :param new_word:
        :return list:
        """

        new_list = []
        for item in list:
            if (search_term in item):
                new_list.append(item.replace(search_term, new_word))

        return new_list

    @staticmethod
    def getHostname():
        """
        Return hostname
        :return: str
        """
        return socket.gethostname()

    @staticmethod
    def getMayaVersion():
        return ('%s' % (versions.current())[0:4])

    @staticmethod
    def log(msg):
        if isinstance(msg, str):
            om.MGlobal.displayInfo(msg)

    @staticmethod
    def warn(msg):
        if isinstance(msg, str):
            om.MGlobal.displayWarning(msg)

    @staticmethod
    def error(msg):
        if isinstance(msg, str):
            om.MGlobal.displayError(msg)
