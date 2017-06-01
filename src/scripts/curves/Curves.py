import SplinesList as splines
import maya.cmds as cmds


class Curves(object):
    __z_out = False
    __name = None

    def __init__(self):
        pass

    def cube(self):
        self.createSpline(splines.cube, 1)

    def cubeOnBase(self):
        self.createSpline(splines.cubeOnBase, 1)

    def footControl(self):
        self.createSpline(splines.foot_spline, 3)

    def sphere(self):
        self.createSpline(splines.sphere, 1)

    def square(self):
        self.createSpline(splines.square, 1)

    def arrow180(self):
        self.createSpline(splines.arrow_180, 3)

    def cog(self):
        self.createSpline(splines.cog, 1)

    def moveControl(self):
        list = []
        list.append(cmds.curve(p=splines.move_spline[0], per=False, d=3, k=[0, 0, 0, 1, 2, 2, 2]))
        list.append(cmds.curve(p=splines.move_spline[1], per=False, d=1, k=[0, 1, 2, 3, 4, 5]))
        list.append(cmds.curve(p=splines.move_spline[2], per=False, d=3, k=[0, 0, 0, 1, 2, 2, 2]))
        list.append(cmds.curve(p=splines.move_spline[3], per=False, d=3, k=[0, 0, 0, 1, 2, 2, 2]))
        list.append(cmds.curve(p=splines.move_spline[4], per=False, d=3, k=[0, 0, 0, 1, 2, 2, 2]))
        list.append(cmds.curve(p=splines.move_spline[5], per=False, d=1, k=[0, 1, 2, 3, 4, 5, 6]))
        list.append(cmds.curve(p=splines.move_spline[6], per=False, d=1, k=[0, 1, 2, 3, 4, 5, 6]))
        list.append(cmds.curve(p=splines.move_spline[7], per=False, d=1, k=[0, 1, 2, 3, 4, 5, 6]))
        list.append(cmds.curve(p=splines.move_spline[8], per=False, d=1, k=[0, 1]))
        self.mergeSpline(list)

    def getListOfCvPoints(self, selected_curve):
        """
        getListOfCvPoints
        Return cvs positions (x, y, z)
        @param selected_curve: name of selected curve
        @return: list of points for selection
        """
        curveCVs = cmds.ls('{0}.cv[:]'.format(selected_curve), fl=True)
        list = []

        for cv in curveCVs:
            pos = cmds.pointPosition(cv)
            list.append(pos)

        return list

    def createKnotVectorString(self, cvNum, degree):
        """
        @param int cvNum: number of CVs in constructing curve.
        @param int degree: degree of constructing curve.
        @return list
        """
        if cvNum <= degree:
            print "warning, number of CVs can't be less than degree + 1"
            return None
        tailsSize = degree
        knotsNum = cvNum + degree - 1
        knotsArray = [0] * knotsNum
        for i in range(0, len(knotsArray) - degree + 1):
            knotsArray[i + degree - 1] = i
        tailValue = knotsArray[-tailsSize - 1] + 1
        for i in range(1, tailsSize):
            knotsArray[-i] = tailValue
        return knotsArray

    def createSpline(self, data, degree):
        list = []
        knot = self.createKnotVectorString(len(data), degree)
        list.append(cmds.curve(p=data, per=False, d=degree, k=knot))
        self.mergeSpline(list)

    def mergeSpline(self, list):
        for x in range(len(list) - 1):
            cmds.makeIdentity(list[x + 1], apply=True, t=1, r=1, s=1, n=0)
            shapeNode = cmds.listRelatives(list[x + 1], shapes=True)
            cmds.parent(shapeNode, list[0], add=True, s=True)
            cmds.delete(list[x + 1])

        cmds.select(list[0])
        ctrl_name = cmds.ls(selection=True)[0]

        # set name
        if self.name != None:
            ctrl_name = '{0}_Ctrl'.format(self.name)
            cmds.rename(list[0], ctrl_name)
            cmds.select(ctrl_name)

        # create zero out group
        if self.zeroOut:
            grp_name = ctrl_name.replace('Ctrl', 'Grp')

            cmds.group(em=True, name=grp_name)
            cmds.parent(ctrl_name, grp_name)

    @property
    def zeroOut(self):
        return self.__z_out

    @zeroOut.setter
    def zeroOut(self, value):
        self.__z_out = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=None):
        self.__name = None if name == '' else name
