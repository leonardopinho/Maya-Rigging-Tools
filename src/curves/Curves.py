import splinesList as splines
import maya.cmds as cmds

reload(splines)

CUBE_CENTER_PIVOT = 'Cube (center pivot)'
CUBE_BASE_PIVOT = 'Cube (base pivot)'
MOVE_CONTROL = 'Move control'
FOOT_CONTROL = 'Foot control'
SPHERE_CONTROL = 'Sphere control'


def sphere():
    createSpline(splines.sphere, 1)


def cube():
    createSpline(splines.cube, 1)


def cubeOnBase():
    createSpline(splines.cubeOnBase, 1)


def footControl():
    createSpline(splines.foot_spline, 3)


def moveControl():
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
    mergeSpline(list)

def getListOfCvPoints(selected_curve):
    """
    getListOfCvPoints
    Return cvs positions (x, y, z)
    :param selected_curve: name of selected curve
    :return: list of points for selection
    """
    curveCVs = cmds.ls('{0}.cv[:]'.format(selected_curve), fl=True)
    list = []

    for cv in curveCVs:
        pos = cmds.pointPosition(cv)
        list.append(pos)

    return list


def createKnotVectorString(cvNum, degree):
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


def createSpline(data, degree):
    list = []
    knot = createKnotVectorString(len(data), degree)
    list.append(cmds.curve(p=data, per=False, d=degree, k=knot))
    mergeSpline(list)


def mergeSpline(list):
    for x in range(len(list) - 1):
        cmds.makeIdentity(list[x + 1], apply=True, t=1, r=1, s=1, n=0)
        shapeNode = cmds.listRelatives(list[x + 1], shapes=True)
        cmds.parent(shapeNode, list[0], add=True, s=True)
        cmds.delete(list[x + 1])
    cmds.select(list[0])
