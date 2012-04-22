'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from direct.showbase import DirectObject 
from pandac.PandaModules import Vec3,Vec2 
import math 
from gameModel.constants import MAX_CAMERA_DISTANCE, MAX_PLANET_RADIUS

class Camera(DirectObject.DirectObject): 
    def __init__(self, star):      
        '''
        @param star: the star the camera will be set at
        '''
     
        base.disableMouse() 
        # This disables the default mouse based camera control used by panda. This default control is awkward, and won't be used. 
        base.camera.setPos(star.position.x,star.position.y + 100,100)
        base.camera.lookAt(star.position.x,star.position.y,0) 
        self.mx,self.my=0,0
        # Sets up variables for storing the mouse coordinates 
         
        self.orbiting=False 
        # A boolean variable for specifying whether the camera is in orbiting mode. Orbiting mode refers to when the camera is being moved 
        # because the user is holding down the right mouse button. 
         
        self.target=Vec3() 
        # sets up a vector variable for the camera's target. The target will be the coordinates that the camera is currently focusing on. 
         
        self.camDist = 40 
        # A variable that will determine how far the camera is from it's target focus 
         
        self.panRateDivisor = 20 
        # This variable is used as a divisor when calculating how far to move the camera when panning. Higher numbers will yield slower panning 
        # and lower numbers will yield faster panning. This must not be set to 0. 
         
        self.panZoneSize = .05 
        # This variable controls how close the mouse cursor needs to be to the edge of the screen to start panning the camera. It must be less than 1, 
        # and I recommend keeping it less than .2 
         
        self.panLimitsX = Vec2(-MAX_CAMERA_DISTANCE*4/5, MAX_CAMERA_DISTANCE*4/5) 
        self.panLimitsY = Vec2(-MAX_CAMERA_DISTANCE*4/5, MAX_CAMERA_DISTANCE*4/5) 
        # These two vairables will serve as limits for how far the camera can pan, so you don't scroll away from the map.
        
        self.maxZoomOut = MAX_CAMERA_DISTANCE/3
        self.maxZoomIn = MAX_PLANET_RADIUS
        #These two variables set the max distance a person can zoom in or out

        self.setTarget(0,0,0) 
        # calls the setTarget function to set the current target position to the origin. 
         
        self.turnCameraAroundPoint(0,0) 
        # calls the turnCameraAroundPoint function with a turn amount of 0 to set the camera position based on the target and camera distance 
         
        self.accept("mouse3",self.startOrbit) 
        # sets up the camrea handler to accept a right mouse click and start the "drag" mode. 
         
        self.accept("mouse3-up",self.stopOrbit) 
        # sets up the camrea handler to understand when the right mouse button has been released, and ends the "drag" mode when 
        # the release is detected. 
         
        # The next pair of lines use lambda, which creates an on-the-spot one-shot function. 
         
        self.accept("wheel_up",self.zoomIn)
        # sets up the camera handler to detet when the mouse wheel is rolled upwards and uses a lambda function to call the
        # adjustCamDist function  with the argument 0.9 
         
        self.accept("wheel_down",self.zoomOut)
        # sets up the camera handler to detet when the mouse wheel is rolled upwards and uses a lambda function to call the
        # adjustCamDist function  with the argument 1.1 
                 
        taskMgr.add(self.camMoveTask,'camMoveTask') 
        # sets the camMoveTask to be run every frame 
         
        self._force = Vec2(0,0)
        self._last_force = Vec2(0,0)
        self._vel = Vec2(0,0)
        self.key_scroll_speed = 5.0
    
    def addForce(self, force):
        self._last_force.set(0,0)
        self._last_force = force
        self._force += force

    def zoomOut(self):
#        print "Zoom Out: " ,self.camDist
        if(self.camDist <= self.maxZoomOut):
            self.adjustCamDist(1.1)
        return True
        
    def zoomIn(self):
#        print "Zoom In:",self.camDist
        if(self.camDist >= self.maxZoomIn):
            self.adjustCamDist(0.9)
        return True
        
        
    def turnCameraAroundPoint(self,deltaX,deltaY): 
        # This function performs two important tasks. First, it is used for the camera orbital movement that occurs when the 
        # right mouse button is held down. It is also called with 0s for the rotation inputs to reposition the camera during the 
        # panning and zooming movements. 
        # The delta inputs represent the change in rotation of the camera, which is also used to determine how far the camera 
            # actually moves along the orbit. 
         
            newCamHpr = Vec3() 
            newCamPos = Vec3() 
            # Creates temporary containers for the new rotation and position values of the camera. 
             
            camHpr=base.camera.getHpr() 
            # Creates a container for the current HPR of the camera and stores those values. 
             
            newCamHpr.setX(camHpr.getX()+deltaX) 
            newCamHpr.setY(self.clamp(camHpr.getY()-deltaY, -85, -10)) 
            newCamHpr.setZ(camHpr.getZ()) 
            # Adjusts the newCamHpr values according to the inputs given to the function. The Y value is clamped to prevent
            # the camera from orbiting beneath the ground plane and to prevent it from reaching the apex of the orbit, which 
            # can cause a disturbing fast-rotation glitch. 
             
            base.camera.setHpr(newCamHpr) 
            # Sets the camera's rotation to the new values. 
             
            angleradiansX = newCamHpr.getX() * (math.pi / 180.0) 
            angleradiansY = newCamHpr.getY() * (math.pi / 180.0) 
            # Generates values to be used in the math that will calculate the new position of the camera. 
             
            newCamPos.setX(self.camDist*math.sin(angleradiansX)*math.cos(angleradiansY)+self.target.getX())
            newCamPos.setY(-self.camDist*math.cos(angleradiansX)*math.cos(angleradiansY)+self.target.getY()) 
            newCamPos.setZ(-self.camDist*math.sin(angleradiansY)+self.target.getZ()) 
            base.camera.setPos(newCamPos.getX(),newCamPos.getY(),newCamPos.getZ()) 
            # Performs the actual math to calculate the camera's new position and sets the camera to that position. 
            #Unfortunately, this math is over my head, so I can't fully explain it. 
                             
            base.camera.lookAt(self.target.getX(),self.target.getY(),self.target.getZ() ) 
            # Points the camera at the target location. 
             
    def setTarget(self,x,y,z):

        #This function is used to give the camera a new target position. 
        x = self.clamp(x, self.panLimitsX.getX(), self.panLimitsX.getY()) 
        self.target.setX(x) 
        y = self.clamp(y, self.panLimitsY.getX(), self.panLimitsY.getY()) 
        self.target.setY(y) 
        self.target.setZ(z)
        self.turnCameraAroundPoint(0,0)
        # Stores the new target position values in the target variable. The x and y values are clamped to the pan limits. 
         
    def setPanLimits(self,xMin, xMax, yMin, yMax): 
        # This function is used to set the limitations of the panning movement. 
         
        self.panLimitsX = (xMin, xMax) 
        self.panLimitsY = (yMin, yMax) 
        # Sets the inputs into the limit variables. 
         
    def clamp(self, val, minVal, maxVal): 
        # This function constrains a value such that it is always within or equal to the minimum and maximum bounds. 
         
        val = min( max(val, minVal), maxVal) 
        # This line first finds the larger of the val or the minVal, and then compares that to the maxVal, taking the smaller. This ensures 
        # that the result you get will be the maxVal if val is higher than it, the minVal if val is lower than it, or the val itself if it's 
        # between the two. 
         
        return val 
        # returns the clamped value 
         
    def startOrbit(self): 
        # This function puts the camera into orbiting mode. 
         
        self.orbiting=True 
        # Sets the orbiting variable to true to designate orbiting mode as on. 
         
    def stopOrbit(self): 
        # This function takes the camera out of orbiting mode. 
         
        self.orbiting=False 
        # Sets the orbiting variable to false to designate orbiting mode as off. 
         
    def adjustCamDist(self,distFactor): 
        # This function increases or decreases the distance between the camera and the target position to simulate zooming in and out. 
        # The distFactor input controls the amount of camera movement. 
            # For example, inputing 0.9 will set the camera to 90% of it's previous distance. 
         
        self.camDist=self.camDist*distFactor 
        # Sets the new distance into self.camDist. 
         
        self.turnCameraAroundPoint(0,0) 
        # Calls turnCameraAroundPoint with 0s for the rotation to reset the camera to the new position.
    
    def _move_x(self, angle, pan_factor):
        pan_rate = pan_factor * (self.camDist / self.panRateDivisor)
        tempX = self.target.getX()+self._vel.getX()-math.sin(angle)*pan_rate 
        tempX = self.clamp(tempX, self.panLimitsX.getX(), self.panLimitsX.getY()) 
        self.target.setX(tempX) 
        tempY = self.target.getY()+self._vel.getY()+math.cos(angle)*pan_rate 
        tempY = self.clamp(tempY, self.panLimitsY.getX(), self.panLimitsY.getY()) 
        self.target.setY(tempY)
        self.turnCameraAroundPoint(0,0)
    
    def _move_y(self, angle, pan_factor):
        pan_rate = pan_factor * (self.camDist / self.panRateDivisor)
        tempX = self.target.getX()+self._vel.getX()+math.sin(angle)*pan_rate 
        tempX = self.clamp(tempX, self.panLimitsX.getX(), self.panLimitsX.getY())
        self.target.setX(tempX) 
        tempY = self.target.getY()+self._vel.getY()-math.cos(angle)*pan_rate 
        tempY = self.clamp(tempY, self.panLimitsY.getX(), self.panLimitsY.getY())
        self.target.setY(tempY) 
        self.turnCameraAroundPoint(0,0) 
          
    def camMoveTask(self,task):
        if base.mouseWatcherNode.hasMouse(): 
            mpos = base.mouseWatcherNode.getMouse() 
            if self.orbiting: 
                self.turnCameraAroundPoint((self.mx-mpos.getX())*100,(self.my-mpos.getY())*100)          
            else: 
                angle = pan_factor = 0
                self._vel = self._vel + self._force
                self._vel = self._vel * 0.9
                vx, vy = self._vel.getX(), self._vel.getY()
                if abs(vx) > 0.01:
                    if self._last_force.getX() < 0: #right
                        angle = base.camera.getH() * (math.pi / 180.0)+math.pi*0.5
                        pan_factor = self.key_scroll_speed * vx
                    else:
                        angle = base.camera.getH() * (math.pi / 180.0)-math.pi*0.5 
                        pan_factor = -self.key_scroll_speed * vx
                    self._move_x(angle, pan_factor)
                    
                if abs(vy) > 0.01:
                    if self._last_force.getY() < 0: #up
                        angle = base.camera.getH() * (math.pi / 180.0) 
                        pan_factor = self.key_scroll_speed * vy
                    else:
                        angle = base.camera.getH() * (math.pi / 180.0)+math.pi 
                        pan_factor = - self.key_scroll_speed * vy
                    self._move_y(angle, pan_factor)
                
                # no keyboard motion, apply motion from hovering near borders
                if abs(vx) < 0.01 and abs(vy) < 0.01:
                    if self.mx > (1 - self.panZoneSize): #right
                        angle = base.camera.getH() * (math.pi / 180.0)+math.pi*0.5 
                        pan_factor = 1 - self.mx - self.panZoneSize
                        self._move_x(angle, pan_factor)
                    elif self.mx < (-1 + self.panZoneSize): #left
                        angle = base.camera.getH() * (math.pi / 180.0)-math.pi*0.5 
                        pan_factor = 1 + self.mx - self.panZoneSize
                        self._move_x(angle, pan_factor)
                    
                    if self.my > (1 - self.panZoneSize): #up
                        angle = base.camera.getH() * (math.pi / 180.0) 
                        pan_factor = 1 - self.my - self.panZoneSize
                        self._move_y(angle, pan_factor)
                    elif self.my < (-1 + self.panZoneSize): #down
                        angle = base.camera.getH() * (math.pi / 180.0)+math.pi 
                        pan_factor = 1 + self.my - self.panZoneSize
                        self._move_y(angle, pan_factor)

            self.mx=mpos.getX() 
            self.my=mpos.getY()
            self._force.set(0,0)
        return task.cont

