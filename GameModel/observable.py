'''
Created on 25 janv. 2012

@author: Bazibaz
'''

#TODO: Could we actually move this to the __init__?
class Observable(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, event, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(event)