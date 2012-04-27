'''
Created on 2012-04-23

@author: Eran-Tasker
'''
from gameModel.player import Player

from direct.distributed.DistributedNode import DistributedNode
from pandac.PandaModules import *

import os

class DistributedPlayer(DistributedNode):
    def __init__(self, cr):
        # you have to initialize NodePath.__init__() here because it is
        # not called in DistributedNode.__init__()
        DistributedNode.__init__(self, cr)
        NodePath.__init__(self, 'player')
        
        self.player = Player(os.getenv('COMPUTERNAME'))
        
    def addStruct(self, structure):
        '''
        Change is applied locally.
        '''
        self.player.addStructure(structure)
        
    def d_addStruct(self, structure):
        '''
        Sends updates on the wire but does not apply it locally.
        '''
        self.sendUpdate('addStruct', [structure])
        
    def b_addStruct(self, structure):
        '''
        Change is applied locally and on the wire.
        '''
        self.addStruct(structure)
        self.d_addStruct(structure)
        
    def addunit(self, unit):
        '''
        Change is applied locally.
        '''
        self.player.addUnit(unit)
        
    def d_addUnit(self, unit):
        '''
        Change is applied on the wire.
        '''
        self.sendUpdate('addunit', [unit])
        
    def b_addUnit(self, unit):
        '''
        Change is applied locally and on the wire.
        '''
        self.addunit(unit)
        self.d_addUnit(unit)
        
        
    def generate(self):
        """ This method is called when the object is generated: when it
        manifests for the first time on a particular client, or when it
        is pulled out of the cache after a previous manifestation.  At
        the time of this call, the object has been created, but its
        required fields have not yet been filled in. """

        # Always call up to parent class
        DistributedNode.generate(self)
        
    def announceGenerate(self):
        """ This method is called after generate(), after all of the
        required fields have been filled in.  At the time of this call,
        the distributed object is ready for use. """

        DistributedNode.announceGenerate(self)

    def disable(self):
        """ This method is called when the object is removed from the
        scene, for instance because it left the zone.  It is balanced
        against generate(): for each generate(), there will be a
        corresponding disable().  Everything that was done in
        generate() or announceGenerate() should be undone in disable().

        After a disable(), the object might be cached in memory in case
        it will eventually reappear.  The DistributedObject should be
        prepared to receive another generate() for an object that has
        already received disable().

        Note that the above is only strictly true for *cacheable*
        objects.  Most objects are, by default, non-cacheable; you
        have to call obj.setCacheable(True) (usually in the
        constructor) to make it cacheable.  Until you do this, your
        non-cacheable object will always receive a delete() whenever
        it receives a disable(), and it will never be stored in a
        cache.
        """

        # Take it out of the scene graph.
        self.detachNode()

        DistributedNode.disable(self)

    def delete(self):
        """ This method is called after disable() when the object is to
        be completely removed, for instance because the other user
        logged off.  We will not expect to see this object again; it
        will not be cached.  This is stronger than disable(), and the
        object may remove any structures it needs to in order to allow
        it to be completely deleted from memory.  This balances against
        __init__(): every DistributedObject that is created will
        eventually get delete() called for it exactly once. """

        # Clean out self.model, so we don't have a circular reference.
        #self.model = None

        DistributedNode.delete(self)