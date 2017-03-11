import unittest
import src.constants.Constants as Constants
import src.utils.Utils as Utils


class UtilsTest(unittest.TestCase):
    def testRenameListOfObject(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        suffix = '_Mesh'
        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix)
        self.assertEquals('L_cube_1_Mesh', new_list[0])

    def testRenameByPattern(self):
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

    def testRenameListByChangingWord(self):
        list = ['L_Middle_1_Jnt', 'L_Middle_2_Jnt', 'L_Middle_3_Jnt']
        search_term = 'Middle'
        new_name = 'Ring'
        new_list = Utils.renameListByChangingWord(list, search_term, new_name)
        self.assertEquals('L_Ring_1_Jnt', new_list[0])

    def testCreateEndJointName(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        suffix = '_Mesh'

        new_list = Utils.renameListOfNames(list, new_name, prefix, suffix, '#', True)
        self.assertEquals('L_cube_JEnd', new_list[2])


class ConstantsTest(unittest.TestCase):
    def testConstantUrl(self):
        url = Constants.getCreditsUrl()
        self.assertEquals(url.split('/')[2], 'www.leonardopinho.com')


if __name__ == '__main__':
    unittest.main()
