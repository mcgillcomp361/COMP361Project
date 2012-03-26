'''
Created on 26 mars 2012

@author: num3ric
'''
import math
from pandac.PandaModules import LineSegs, NodePath
from pandac.PandaModules import deg2Rad, rad2Deg 
from panda3d.core import Vec4


def makeArc(angleDegrees = 360, numSteps = 16): 
    ls = LineSegs() 
    ls.setColor(Vec4(0, 0, 0.3, 1.0))
    angleRadians = deg2Rad(angleDegrees) 

    for i in xrange(numSteps + 1): 
        a = angleRadians * i / numSteps 
        y = math.sin(a) 
        x = math.cos(a) 

        ls.drawTo(x, y, 0)
        ls.setThickness(2.0)
        ls.setColor(Vec4(0, 0, 0.3, 1.0))
    node = ls.create() 
    return NodePath(node)