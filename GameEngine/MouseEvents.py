'''
Created on Jan 15, 2012

@author: Julie
'''

from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import CollisionTraverser, CollisionHandlerQueue, CollisionRay 
from pandac.PandaModules import CollisionNode
from direct.showbase import DirectObject
from panda3d.core import *
import sys

class MouseEvents(DirectObject.DirectObject):
    
    def __init__(self):

        # Initialize the traverser.
        self.myTraverser = CollisionTraverser()
 
 
        # Initialize the handler.
        self.myHandler = CollisionHandlerQueue()       
     
        self.accept("escape", sys.exit)        #Exit the program when escape is pressed
        
        base.disableMouse()
        
        
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
#        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.myTraverser.addCollider(self.pickerNP, self.myHandler)
        
        self.accept("mouse1", self.handleMouseClick)
        
    
    #Use Collision Detection 
    def handleMouseClick(self):
        if base.mouseWatcherNode.hasMouse():
            #get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
            # This makes the ray's origin the camera and makes the ray point 
            # to the screen coordinates of the mouse.
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            
            self.myTraverser.traverse(render)
            # Assume for simplicity's sake that myHandler is a CollisionHandlerQueue.
            if self.myHandler.getNumEntries() > 0:
                # This is so we get the closest object.
                self.myHandler.sortEntries()
                pickedObj = self.myHandler.getEntry(0).getIntoNodePath()
                
                #Check to see if the selected object is the star (to activate)
                pickedObj = pickedObj.findNetTag('starTag')
                if not pickedObj.isEmpty():
                    self.activateStar(pickedObj)
                pickedObj = pickedObj.findNetTag('planetTag')
                if not pickedObj.isEmpty():
                    print 'planet selected'
                    
    def activateStar(self, pickedObj):
        #Star is activated
        print "You selected the star"