'''
Created on 7 janv. 2012

@author: num3ric
'''
from pandac.PandaModules import CollisionNode, CollisionSphere
#from pandac.PandaModules import Vec3, Point2
from panda3d.core import Vec3,Point2,BitMask32

class SphericalDraw(object):
    '''
    Information about a spherical object in the scene graph.
    It also encompasses a collision sphere of identical
    position and size.
    '''
    def __init__(self, SphericalBody, point_path=None):
        self.pos = Vec3(SphericalBody.position)
        self.vel = Vec3()
        self.size = 2*SphericalBody.radius
        
        # Dummy parent paths for both model & collision sphere
        #-----------------------------------------------------
        # root_path: This dummy node copying the parent position
        # is used as a center of orbit. The copy is necessary
        # so that the rotation of the orbiting body does not
        # affect the parent object.
        #
        # point_path: This dummy node path is only used to
        # displace the object, not to scale them. If we were to
        # scale them here, the scaling would propagate to child
        # nodes and make the sizes written set in the model very
        # strange. In short, the POSITIONS ARE RELATIVE but the
        # SCALING IS NOT. (Hence the "point" name.)
        #-----------------------------------------------------
        self.root_path = None
        if point_path == None:
            self.point_path = render.attachNewNode("sphere_node")
        else:
            self.root_path = point_path.attachNewNode("orbit_root_node")
            self.point_path = self.root_path.attachNewNode("sphere_node")
        self.point_path.setPos(self.pos)
        
        # Collision sphere for object picking
        #-----------------------------------------------------
        # As described in the Tut-Chessboard.py sample: "If this model was
        # any more complex than a single polygon, you should set up a collision
        # sphere around it instead."
        self.cnode = CollisionNode("coll_sphere_node")
        #We use no displacement (0,0,0) and no scaling factor (1)
        self.cnode.addSolid(CollisionSphere(0,0,0,1))
        self.cnode.setIntoCollideMask(BitMask32.bit(1))
        self.cnode_path = render.attachNewNode(self.cnode)
        #For temporary testing, display collision sphere.
#        self.cnode_path.show()

class StarDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d star object.
    '''
    
    def __init__(self, star):
        super(StarDraw, self).__init__(star)
        self.star = star
        #Models & textures
        self.star_path = loader.loadModel("../models/planet_sphere")
        self.star_tex = loader.loadTexture("../models/sun_1k_tex.jpg")
        self.star_path.setTexture(self.star_tex, 1)
        self.star_path.reparentTo(self.point_path)
        self.star_path.setScale(self.size)
        self.cnode.setTag('starTag', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the star perfectly.
        self.cnode_path.reparentTo(self.star_path)



class PlanetDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d planet object.
    '''
    
    def __init__(self, planet, star_point_path):
        super(PlanetDraw, self).__init__(planet, star_point_path)
        self.planet = planet
        self.orbital_velocity = planet.orbital_velocity
        #Models & textures
        self.planet_path = loader.loadModel("../models/planet_sphere")
        self.planet_tex = loader.loadTexture("../models/mars_1k_tex.jpg")
        self.planet_path.setTexture(self.planet_tex, 1)
        self.planet_path.reparentTo(self.point_path)
        self.planet_path.setScale(self.size)
        self.cnode.setTag('planetTag', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the planet perfectly.
        self.cnode_path.reparentTo(self.planet_path)
    
    
    def startSpin(self):
        self.day_period_mercury = self.planet_path.hprInterval(
                                    (59), Vec3(360, 0, 0))
        self.day_period_mercury.loop()
    
    def startOrbit(self):
        self.planet.orbital_velocity

        self.orbit_period_mercury = self.root_path.hprInterval(
                                    self.planet.orbital_velocity,
                                    Vec3(360, 0, 0))
        self.orbit_period_mercury.loop()
        


# KEEP => WILL BE USEFUL FOR MULTIPLE OBJECT SELECTION (CLICK & DRAG)!

#def is3dpointIn2dRegion(node, point1, point2, point3d): 
#    """This function takes a 2d selection box from the screen as defined by two corners 
#    and queries whether a given 3d point lies in that selection box 
#    Returns True if it is 
#    Returns False if it is not""" 
#    #node is the parent node- probably render or similar node
#    #point1 is the first 2d coordinate in the selection box
#    #point2 is the opposite corner 2d coordinate in the selection box
#    #point3d is the point in 3d space to test if that point lies in the 2d selection box
#    # Convert the point to the 3-d space of the camera
#    p3 = base.cam.getRelativePoint(node, point3d)
#
#    # Convert it through the lens to render2d coordinates
#    p2 = Point2()
#    if not base.camLens.project(p3, p2):
#        return False
#    
#    r2d = Point3(p2[0], 0, p2[1])
#    
#    # And then convert it to aspect2d coordinates
#    a2d = aspect2d.getRelativePoint(render2d, r2d)
#    
#    #Find out the biggest/smallest X and Y of the 2- 2d points provided.
#    if point1.getX() > point2.getX():
#        bigX = point1.getX()
#        smallX = point2.getX()
#    else:
#        bigX = point2.getX()
#        smallX = point1.getX()
#        
#    if point1.getY() > point2.getY():
#        bigY = point1.getY()
#        smallY = point2.getY()
#    else:
#        bigY = point2.getY()
#        smallY = point2.getY()
#    pX = a2d.getX()
#    pY = a2d.getZ()    #aspect2d is based on a point3 not a point2 like render2d.
#    
#    if pX < bigX and pX > smallX:
#        if pY < bigY and pY > smallY:
#                return True
#        else: return False
#    else: return False
#            
#def savemousePos():
#    pos = Point2(base.mouseWatcherNode.getMouse())
#    pos.setX(pos.getX() * 1.33)
#    return pos
