'''
Created on Jan 15, 2012

@author: Bazibaz
'''
import sys
from direct.showbase import DirectObject 
from pandac.PandaModules import CollisionTraverser, CollisionHandlerQueue, CollisionRay, TransparencyAttrib
from pandac.PandaModules import CollisionNode, CardMaker
from panda3d.core import BitMask32, Point2, Vec2, Vec3,Vec4

from direct.directtools.DirectGeometry import LineNodePath

class MouseEvents(DirectObject.DirectObject):
    
    def __init__(self): 
#        from gameEngine import moveUnitsNext, moveUnitsPrev
#        self.accept('arrow_down', moveUnitsNext )
#        self.accept('arrow_up', moveUnitsPrev )          
        self.accept('arrow_up-repeat', self.moveCameraUp)
        self.accept('arrow_up', self.moveCameraUp)
        self.accept('arrow_down-repeat', self.moveCameraDown)
        self.accept('arrow_down', self.moveCameraDown)
        self.accept('arrow_left-repeat', self.moveCameraLeft)
        self.accept('arrow_left', self.moveCameraLeft) 
        self.accept('arrow_right-repeat', self.moveCameraRight)
        self.accept('arrow_right', self.moveCameraRight)               
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
        ''' the player has to double click a star or planet in order to activate them '''
        self.accept("mouse1", self.handleLeftMouseClick)
        self.accept("mouse3", self.handleRightMouseClick)
        
        self.accept("mouse1-up", self.handleMouseDrag)
        self.mouseFirstPos = None
        
        cm = CardMaker('quad')
#        cm.setFrameFullscreenQuad()
        self.drag_rect_path = base.render2d.attachNewNode(cm.generate())
        self.drag_rect_path.setTransparency(TransparencyAttrib.MAlpha)
        self.drag_rect_path.setColor(Vec4(1,1,1,0.3))
        self.drag_rect_path.hide()
#        self.drag_rect_path = LineNodePath(base.render2d, thickness = 8.0)

    
    def selectionRectangle(self, task):
        if base.mouseWatcherNode.hasMouse():# and self.mouseFirstPos != None:
            mpos = base.mouseWatcherNode.getMouse()
            self.drag_rect_path.show()
            self.drag_rect_path.setSx(mpos.getX()-self.mouseFirstPos.getX()+0.0001)
            self.drag_rect_path.setSz(mpos.getY()-self.mouseFirstPos.getY()+0.0001)
            self.drag_rect_path.setPos(self.mouseFirstPos.getX(), 0, self.mouseFirstPos.getY())

#            self.drag_rect_path.drawLines([((self.mouseFirstPos.getX(),self.mouseFirstPos.getY()),(mpos.getX(), mpos.getY()))])
#            self.drag_rect_path.create()
#            base.win.makeDisplayRegion(self.mouseFirstPos.getX(), self.mouseFirstPos.getY(), mpos.getX(), mpos.getY())
        return task.cont
        
    def handleMouseDrag(self):
        if self.mouseFirstPos != None:
            mpos = base.mouseWatcherNode.getMouse()
            lvec = Vec2(self.mouseFirstPos) - Vec2(mpos)
            if lvec.length() > 0.01:
                scaled_pos = Point2(self.mouseFirstPos)
                scaled_pos.setX(scaled_pos.getX()*base.getAspectRatio())
                scaled_mpos = Point2(mpos)
                scaled_mpos.setX(scaled_mpos.getX()*base.getAspectRatio())
                for unit in self.player.selected_units:
                    unit.deselect()
                del self.player.selected_units[:]
                for unit in self.player.units:
                    if unit.is3dpointIn2dRegion(scaled_pos, scaled_mpos):
                        unit.select()
            self.mouseFirstPos = None
            self.drag_rect_path.hide()
            taskMgr.remove(self.rect_task)
        
    def setPlayer(self, player):
        self.player = player
    
    def setCamera(self, camera):
        self.camera = camera
        
    def moveCameraUp(self):
        self.camera.camera_direction = "moveUp"
        
    def moveCameraDown(self):  
        self.camera.camera_direction = "moveDown" 
    
    def moveCameraLeft(self):
        self.camera.camera_direction = "moveLeft"
    
    def moveCameraRight(self):
        self.camera.camera_direction = "moveRight"   
    
    def handleLeftMouseClick(self):
        if base.mouseWatcherNode.hasMouse():
            #get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
            self.savemousePos()
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
                    self.selected(pickedObj, 'star', 'pyStar', 'leftClick')
                elif pickedObj.hasTag('planet'):
                    self.selected(pickedObj, 'planet', 'pyPlanet', 'leftClick')
                elif pickedObj.hasTag('unit'):
                    self.selected(pickedObj, 'unit', 'pyUnit', 'leftClick')
                elif pickedObj.hasTag('testUnit'):
                    self.selected(pickedObj, 'testUnit', 'pyTestUnit', 'leftClick')
            
            self.rect_task = taskMgr.add(self.selectionRectangle, 'drag')

    def savemousePos(self): 
        self.mouseFirstPos = Point2(base.mouseWatcherNode.getMouse()) 
#        self.mouseFirstPos.setX(self.mouseFirstPos.getX()*1.33) 

              
    def handleRightMouseClick(self):
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
                #if pickedObj.hasTag('star'):
                #    self.selected(pickedObj, 'star', 'pyStar')
                if pickedObj.hasTag('planet'):
                    self.selected(pickedObj, 'planet', 'pyPlanet', 'rightClick')
                #elif pickedObj.hasTag('unit'):
                #    self.selected(pickedObj, 'unit', 'pyUnit')
                    
    def selected(self, pickedObj, tag, python_tag, click):
#        print 'Player has selected '+ tag + ' ' + pickedObj.getTag(tag)
        model_path = pickedObj.getParent()
        #model_path.notify("starSelected")
        model = model_path.getPythonTag(python_tag)
        if(click == 'rightClick'):
            model.selectRight(self.player)
        elif(click == 'leftClick' and tag == 'unit'):
            if(self.player == model.player):
                for unit in self.player.selected_units:
                    unit.deselect()
                del self.player.selected_units[:]
                model.select()
        else:
            model.select(self.player)
