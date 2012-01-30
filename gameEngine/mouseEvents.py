'''
Created on Jan 15, 2012

@author: Bazibaz
'''
import sys
from direct.showbase import DirectObject 
from pandac.PandaModules import CollisionTraverser, CollisionHandlerQueue, CollisionRay 
from pandac.PandaModules import CollisionNode
from panda3d.core import BitMask32

class MouseEvents(DirectObject.DirectObject):
    
    def __init__(self):                
        # Initialize the traverser.
        self.myTraverser = CollisionTraverser()
 
        # Initialize the handler.
        self.myHandler = CollisionHandlerQueue()       
        self.accept("escape", sys.exit) #Exit the program when escape is pressed
        base.disableMouse()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
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
                if pickedObj.hasTag('star'):
                    pass
                    #self.activateSelected(pickedObj, 'star', 'pyStar')
                elif pickedObj.hasTag('planet'):
                    pass
                    #self.scaleSelected(pickedObj, 'planet', 'pyPlanet')
                elif pickedObj.hasTag('unit'):
                    pass
                    #self.scaleSelected(pickedObj, 'planet', 'pyPlanet')
                    
    def activateSelected(self, pickedObj, tag, python_tag):
        print 'You have selected '+ tag + ' ' + pickedObj.getTag(tag)
        model_path = pickedObj.getParent()
        graphic_obj = model_path.getPythonTag(python_tag)
        # Since the stardraw dstar is listening to the model
        # it will automatically get updated, idem for the
        # planet below.
        #graphic_obj.model.radius = 1.09 * graphic_obj.model.radius

