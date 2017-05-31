from abc import ABCMeta, abstractmethod


class UIBase():
    '''
    Abstract class for ui
    '''
    __metaclass__ = ABCMeta

    def __init__(self, path, x_pos=0, y_pos=0):
        pass

    @abstractmethod
    def config(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass
