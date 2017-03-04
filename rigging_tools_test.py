import unittest
import src.constants.Constants as Constants
import src.utils.Utils as Utils

class RiggingToolsTest(unittest.TestCase):

    def testRenameListOfObject(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        sufix = '_Mesh'
        new_list = Utils.renameListOfNames(list, new_name, prefix, sufix)
        self.assertEquals('L_cube_1_Mesh', new_list[0])

    def testRenameByPattern(self):
        list = ['obj1', 'obj2', 'obj3']
        new_name = 'cube'
        prefix = 'L_'
        sufix = '_Mesh'

        new_list = Utils.renameListOfNames(list, new_name, prefix, sufix, '#')
        self.assertEquals('L_cube_1_Mesh', new_list[0])

        new_list = Utils.renameListOfNames(list, new_name, prefix, sufix, '##')
        self.assertEquals('L_cube_01_Mesh', new_list[0])

        new_list = Utils.renameListOfNames(list, new_name, prefix, sufix, '###')
        self.assertEquals('L_cube_001_Mesh', new_list[0])


    def testConstantUrl(self):
        url = Constants.getCreditsUrl()
        self.assertEquals(url.split('/')[2], 'www.leonardopinho.com')

if __name__ == '__main__':
    unittest.main()