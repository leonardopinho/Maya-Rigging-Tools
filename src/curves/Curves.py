import splinesList as splines
import maya.cmds as cmds

CUBE_CENTER_PIVOT = 'Cube (center pivot)'
CUBE_BASE_PIVOT = 'Cube (base pivot)'
MOVE_CONTROL = 'Move control'
FOOT_CONTROL = 'Foot control'


def cube():
    list = []
    data = splines.cube
    list.append(cmds.curve(p=data, per=False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    mergeSpline(list)


def cubeOnBase():
    list = []
    data = splines.cubeOnBase
    list.append(cmds.curve(p=data, per=False, d=1, k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    mergeSpline(list)


def footControl():
    list = []
    data = splines.foot_spline
    list.append(cmds.curve(p=data, per=True, d=3, k=[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    mergeSpline(list)


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


def mergeSpline(list):
    for x in range(len(list) - 1):
        cmds.makeIdentity(list[x + 1], apply=True, t=1, r=1, s=1, n=0)
        shapeNode = cmds.listRelatives(list[x + 1], shapes=True)
        cmds.parent(shapeNode, list[0], add=True, s=True)
        cmds.delete(list[x + 1])
    cmds.select(list[0])
