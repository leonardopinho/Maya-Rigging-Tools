import unittest
import logging

logging.basicConfig(
    filename="log/test.log",
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s,%(msecs)d %(levelname)-8s[%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S'
)

from src.extras.Constants import Constants
from src.utils.Utils import Utils


class UtilsTest(unittest.TestCase):
    def test_rename_list_of_object(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        suffix = '_Mesh'
        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix)
        self.assertEquals('L_cube_1_Mesh', new_list[0])
        logging.debug("test_rename_list_of_object: {} (${}) - {}".format('L_cube_1_Mesh', new_list[0],
                                                                         ('L_cube_1_Mesh' == new_list[0])))

    def test_rename_by_pattern(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        suffix = '_Mesh'

        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix, '#')
        self.assertEquals('L_cube_1_Mesh', new_list[0])

        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix, '##')
        self.assertEquals('L_cube_01_Mesh', new_list[0])

        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix, '###')
        self.assertEquals('L_cube_001_Mesh', new_list[0])

    def test_rename_list_by_changing_word(self):
        list = ['L_Middle_1_Jnt', 'L_Middle_2_Jnt', 'L_Middle_3_Jnt']
        search_term = 'Middle'
        new_name = 'Ring'
        new_list = Utils.renameListByChangingWord(list, search_term, new_name)
        self.assertEquals('L_Ring_1_Jnt', new_list[0])

    def test_create_end_joint_name(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        suffix = '_Mesh'

        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix, '#', True)
        self.assertEquals('L_cube_JEnd', new_list[2])


class ConstantsTest(unittest.TestCase):
    def test_constant_url(self):
        url = Constants.getCreditsUrl()
        self.assertEquals(url.split('/')[2], 'www.leonardopinho.com')


if __name__ == '__main__':
    unittest.main()
