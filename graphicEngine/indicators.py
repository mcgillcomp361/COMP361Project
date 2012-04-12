'''
Created on 4 avr. 2012

@author: num3ric
'''
from direct.directtools.DirectGeometry import LineNodePath
from panda3d.core import Vec4


def drawProgressBar(self, time, task):
    '''
    Draw a progress bar above or below an object (planet).
    @param self: instance of the object associated with the progress bar 
    @param time: total duration
    @param above: True if the progress bar is displayed above
    @param red: Vec4 representing the first color
    @param green: Vec4 representing the second color
    @param task: Panda3d's task
    '''
    try:
        if self.green_progress_path:
                self.green_progress_path.setScale(task.time/float(time)*2.0)
                self.red_progress_path.setScale((1.0-task.time/float(time)+0.001)*2.0)
    except AttributeError:
        self.green_progress_path = LineNodePath(parent = self.point_path, thickness = 8.0, colorVec = Vec4(0,1.0,0,0.5))
        self.green_progress_path.setPos(0,0,-7)
        self.green_progress_path.drawLines([((0,0,0),(2, 0,0))])
        self.green_progress_path.create()
        self.green_progress_path.setBillboardPointEye()
        self.green_progress_path.setScale(0.01)
        
        self.red_progress_path = LineNodePath(parent = self.point_path, thickness = 8.0, colorVec = Vec4(1.0,0,0,0.5))
        self.red_progress_path.setPos(0, 0,-7)
        self.red_progress_path.drawLines([((0,0,0),(-2, 0,0))])
        self.red_progress_path.create()
        self.red_progress_path.setBillboardPointEye()
        self.red_progress_path.setScale(0.01)
        
    if task.time > time:
        self.green_progress_path.removeNode()
        self.red_progress_path.removeNode()
        del self.green_progress_path 
        del self.red_progress_path       
        return task.done
    return task.cont

def drawStarProgressBar(self, time, task):
    '''
    Draw a progress bar above or below an object (star).
    @param self: instance of the object associated with the progress bar 
    @param time: total duration
    @param above: True if the progress bar is displayed above
    @param red: Vec4 representing the first color
    @param green: Vec4 representing the second color
    @param task: Panda3d's task
    '''
    try:
        if self.green_progress_path:
                self.green_progress_path.setScale(task.time/float(time)*2.0)
                self.red_progress_path.setScale((1.0-task.time/float(time)+0.001)*2.0)
    except AttributeError:
        self.green_progress_path = LineNodePath(parent = self.point_path, thickness = 8.0, colorVec = Vec4(1.0,0.0,1.0,0.5))
        self.green_progress_path.setPos(-2,-2,9)
        self.green_progress_path.drawLines([((0,0,0),(2, 0,0))])
        self.green_progress_path.create()
        self.green_progress_path.setBillboardPointEye()
        self.green_progress_path.setScale(0.01)
        
        self.red_progress_path = LineNodePath(parent = self.point_path, thickness = 8.0, colorVec = Vec4(0.0,1.0,1.0,0.5))
        self.red_progress_path.setPos(-2, -2, 9)
        self.red_progress_path.drawLines([((0,0,0),(-2, 0,0))])
        self.red_progress_path.create()
        self.red_progress_path.setBillboardPointEye()
        self.red_progress_path.setScale(0.01)
        
    if task.time > time:
        self.green_progress_path.removeNode()
        self.red_progress_path.removeNode()
        del self.green_progress_path 
        del self.red_progress_path       
        return task.done
    return task.cont

def drawUnitProgressBar(self, time, task):
    '''
    Draw a progress bar above or below an object (planet).
    @param self: instance of the object associated with the progress bar 
    @param time: total duration
    @param above: True if the progress bar is displayed above
    @param red: Vec4 representing the first color
    @param green: Vec4 representing the second color
    @param task: Panda3d's task
    '''
    try:
        if self.yellow_progress_path:
                self.yellow_progress_path.setScale(task.time/float(time)*2.0)
                self.purple_progress_path.setScale((1.0-task.time/float(time)+0.001)*2.0)
    except AttributeError:
        self.yellow_progress_path = LineNodePath(parent = self.point_path, thickness = 16.0, colorVec = Vec4(1.0,1.0,0,0.5))
        self.yellow_progress_path.setPos(0,0,7)
        self.yellow_progress_path.drawLines([((0,0,0),(2, 0,0))])
        self.yellow_progress_path.create()
        self.yellow_progress_path.setBillboardPointEye()
        self.yellow_progress_path.setScale(0.01)
        
        self.purple_progress_path = LineNodePath(parent = self.point_path, thickness = 16.0, colorVec = Vec4(0.5,0,1.0,0.5))
        self.purple_progress_path.setPos(0, 0,7)
        self.purple_progress_path.drawLines([((0,0,0),(-2, 0,0))])
        self.purple_progress_path.create()
        self.purple_progress_path.setBillboardPointEye()
        self.purple_progress_path.setScale(0.01)
        
    if task.time > time:
        self.yellow_progress_path.removeNode()
        self.purple_progress_path.removeNode()
        del self.yellow_progress_path 
        del self.purple_progress_path       
        return task.done
    return task.cont

#def damageSphere(self, time, task):
#    try:
#        if self.damage_sphere_path:
#            pass
#    except AttributeError:
#        self.damage_sphere_path = loader.loadModel("models/stars/planet_sphere")
#        self.damage_sphere_path.reparentTo(self.model_path)
#        self.damage_sphere_path.setScale(2)
#        self.damage_sphere_path.setTextureOff()
#        self.damage_sphere_path.setColor(1,0,0,0.3)
#    if task.time > time:
#        self.yellow_progress_path.removeNode()
#        self.purple_progress_path.removeNode()
#        del self.damage_sphere_path 
#        return task.done
#    return task.cont