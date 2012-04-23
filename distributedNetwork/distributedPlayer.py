'''
Created on 2012-04-23

@author: Eran-Tasker
'''

from direct.distributed.DistributedNode import DistributedNode
from pandac.PandaModules import *

class DistributedPlayer(DistributedNode):
    def __init__(self, cr):
        # you have to initialize NodePath.__init__() here because it is
        # not called in DistributedNode.__init__()
        DistributedNode.__init__(self, cr)
        NodePath.__init__(self, 'player')