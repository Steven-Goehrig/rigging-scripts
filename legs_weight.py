import pymel.core as pm
import maya.api.OpenMaya as om
import math

class weightBalance(object):

    def __init__(self):
        self.weights = []
        self.legs = [['front_leg_C0_hip_jnt', 'front_leg_C0_4_jnt'],
        ['backLeft_leg_C0_hip_jnt', 'backLeft_leg_C0_4_jnt'],
        ['frontLeft_leg_C0_hip_jnt', 'frontLeft_leg_C0_4_jnt'],
        ['frontRight_leg_C0_0_jnt', 'frontRight_leg_C0_4_jnt'],
        ['backRight_leg_C0_hip_jnt', 'backRight_leg_C0_4_jnt']]
        self.weightTotal = None
        
    def getWeights(self):
        return self.weights
    
    def getWeightTotal(self):
        return self.weightTotal
        
    def updateWeights(self, *args):
                
        print('Recent findWeights call:')
        
        self.weightTotal = None
    
        for leg in self.legs:
            leg_base = om.MVector(pm.xform(pm.PyNode(leg[0]), t=1, q=1, ws=True))
            leg_end = om.MVector(pm.xform(pm.PyNode(leg[1]), t=1, q=1, ws=True))
            
            leg_vector = om.MVector(leg_end - leg_base)
            distance = leg_vector.length()
            angle = leg_vector.angle(om.MVector([0,-1,0])) #Don't convert to degrees
            weight = 1/math.sin(angle)*distance
            if self.weightTotal:
                self.weightTotal += weight
            else:
                self.weightTotal = weight
            self.weights.append(round(weight))
    
            print(leg[0])
            print('leg_base:', leg_base)
            print('leg_end:', leg_end)
            print('leg_vector:', leg_vector)
            print('distance:', distance)
            print('angle:', angle*180/math.pi) #Only convert to degrees here
            print('cos:', math.cos(angle))
            print('weight:', weight)
        
        percentageWeights = []
        for weight in self.getWeights():
            percentageWeights.append(round(weight*100/self.getWeightTotal()))
        self.weights = percentageWeights
            
        print(self.weights)
        self.showUI()

    def showUI(self):
        """Find Weights UI"""
    
        if pm.window("findWeightsUI_window", exists=True):
            pm.deleteUI("findWeightsUI_window")
    
        window = pm.window("findWeightsUI_window",
                           title="Find Leg Weights",
                           w=300,
                           h=50,
                           mxb=False,
                           sizeable=False)
                           
        pm.rowColumnLayout(numberOfColumns=1,
                           columnAttach=(1, 'both', 0),
                           columnWidth=(1, 300))
    
        pm.button(label="Refresh", command=self.updateWeights)
        pm.separator(h=10)
        pm.text(label="Instructions: Hit Refresh to find latest weights", align="center")
        pm.separator(h=10)
        if len(self.weights) != 0:
            pm.text(label="Red: " + str(self.getWeights().pop(0)) + '%', align="center")
            pm.text(label="Blue: " + str(self.getWeights().pop(0)) + '%', align="center")
            pm.text(label="Violet: " + str(self.getWeights().pop(0)) + '%', align="center")
            pm.text(label="Pink: " + str(self.getWeights().pop(0)) + '%', align="center")
            pm.text(label="Green: " + str(self.getWeights().pop(0)) + '%', align="center")
            pm.separator(h=10)
        pm.text(label="Defaults", align="center")
        pm.text(label="R: 20% | B: 21% | V: 19% | P: 21% | G: 20%", align="center")
        pm.separator(h=10)
        
        pm.showWindow()

jennifernWeight = weightBalance()
jennifernWeight.showUI()