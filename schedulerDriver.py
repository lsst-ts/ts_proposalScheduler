import time

from schedulerTarget import *

class schedulerDriver (object):
    def __init__ (self):

        self.time = 0.0

        self.targetId = 0

        self.newTarget = schedulerTarget()

        return

    def startSurvey(self):
    	return

    def endSurvey(self):
    	return

    def startNight(self):
        return

    def endNight(self):
        return

    def swapFilterIn(self):
        return

    def swapFilterOut(self):
        return

    def updateInternalConditions(self, topicTime):

        self.time = topicTime.timestamp

        return

    def updateExternalConditions(self, topicTime):
        return

    def selectNextTarget(self):

        self.targetId += 1

        time.sleep(0.025)

        self.newTarget.targetId = self.targetId
        self.newTarget.fieldId  = 1234
        self.newTarget.filter   = "z"
        self.newTarget.ra       = 10.0
        self.newTarget.dec      = 30.0
        self.newTarget.angle    = 45.0
        self.newTarget.num_exposures = 2

        return self.newTarget

    def registerObservation(self, topicObservation):
        return

